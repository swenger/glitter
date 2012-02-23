import itertools as _itertools
from weakref import WeakKeyDictionary, WeakValueDictionary
import numpy as _np
from rawgl import gl as _gl

from constants import blend_functions, blend_equations, depth_functions, draw_buffers, hints, provoking_vertices, logic_op_modes, provoke_modes, color_read_formats, color_read_types, read_buffers
from dtypes import bool8, int32, int64, float32

# TODO with statements for state changes, e.g. with context.set(active_texture=0): ...

class Proxy(object):
    def __init__(self, getter=None, get_args=(), setter=None, set_args=(), dtype=None, shape=None):
        self._getter = getter
        self._get_args = get_args
        self._setter = setter
        self._set_args = set_args
        self._dtype = dtype
        self._shape = None if shape is None else tuple(shape) if hasattr(shape, "__iter__") else (shape,)

    def __get__(self, obj, cls=None):
        _value = _np.empty(self._shape, dtype=self._dtype.as_numpy())
        args = list(self._get_args) + [_gl.cast(_value.ctypes, self._getter.argtypes[-1])]
        with obj:
            self._getter(*args)
        return _value.item() if _value.shape is () else _value

    def __set__(self, obj, value):
        if self._setter is None:
            raise AttributeError("can't set attribute")
        _value = _np.ascontiguousarray(value, dtype=self._dtype.as_numpy())
        if len(self._set_args) + len(_value) == len(self._setter.argtypes):
            args = list(self._set_args) + (list(_value) if _value.ndim == 1 else [x.ctypes for x in _value])
        elif len(self._set_args) + 1 == len(self._setter.argtypes):
            args = list(self._set_args) + [_value.ctypes]
        else:
            raise RuntimeError("no valid setter invocation found")
        with obj:
            self._setter(*args)

class BooleanProxy(Proxy):
    def __init__(self, get_args=(), setter=None, set_args=(), shape=None):
        super(BooleanProxy, self).__init__(_gl.glGetBooleanv, get_args, setter, set_args, bool8, shape)

class FloatProxy(Proxy):
    def __init__(self, get_args=(), setter=None, set_args=(), shape=None):
        super(FloatProxy, self).__init__(_gl.glGetFloatv, get_args, setter, set_args, float32, shape)

class IntegerProxy(Proxy):
    def __init__(self, get_args=(), setter=None, set_args=(), shape=None):
        super(IntegerProxy, self).__init__(_gl.glGetIntegerv, get_args, setter, set_args, int32, shape)

class Integer64Proxy(Proxy):
    def __init__(self, get_args=(), setter=None, set_args=(), shape=None):
        super(Integer64Proxy, self).__init__(_gl.glGetInteger64v, get_args, setter, set_args, int64, shape)

class EnableDisableProxy(object):
    def __init__(self, arg):
        self._arg = arg

    def __get__(self, obj, cls=None):
        with obj:
            return _gl.glIsEnabled(self._arg) == _gl.GL_TRUE

    def __set__(self, obj, value):
        with obj:
            _gl.glEnable(self._arg) if value else _gl.glDisable(self._arg)

class BlendFuncProxy(object): # TODO indexed variant
    def __init__(self, arg):
        self._arg = arg

    def __get__(self, obj, cls=None):
        _value = _gl.GLint()
        with obj:
            _gl.glGetIntegerv(self._arg, _gl.pointer(_value))
        return blend_functions[_value.value]

    def __set__(self, obj, value):
        src_rgb = value if self._arg == _gl.GL_BLEND_SRC_RGB else obj.blend_src_rgb
        dst_rgb = value if self._arg == _gl.GL_BLEND_DST_RGB else obj.blend_dst_rgb
        src_alpha = value if self._arg == _gl.GL_BLEND_SRC_ALPHA else obj.blend_src_alpha
        dst_alpha = value if self._arg == _gl.GL_BLEND_DST_ALPHA else obj.blend_dst_alpha
        with obj:
            _gl.glBlendFuncSeparate(src_rgb._value, dst_rgb._value, src_alpha._value, dst_alpha._value)

class BlendEquationProxy(object): # TODO indexed variant
    def __init__(self, arg):
        self._arg = arg

    def __get__(self, obj, cls=None):
        _value = _gl.GLint()
        with obj:
            _gl.glGetIntegerv(self._arg, _gl.pointer(_value))
        return blend_equations[_value.value]

    def __set__(self, obj, value):
        mode_rgb = value if self._arg == _gl.GL_BLEND_EQUATION_RGB else obj.blend_equation_rgb
        mode_alpha = value if self._arg == _gl.GL_BLEND_EQUATION_ALPHA else obj.blend_equation_alpha
        with obj:
            _gl.glBlendEquationSeparate(mode_rgb._value, mode_alpha._value)

class EnumProxy(object):
    def __init__(self, enum, arg, setter=None, set_args=()):
        self._enum = enum
        self._setter = setter
        self._arg = arg
        self._set_args = set_args

    def __get__(self, obj, cls=None):
        _value = _gl.GLint()
        with obj:
            _gl.glGetIntegerv(self._arg, _gl.pointer(_value))
        return self._enum[_value.value]

    def __set__(self, obj, value):
        if self._setter is None:
            raise AttributeError("can't set attribute")
        args = list(self._set_args) + [value._value]
        with obj:
            self._setter(*args)

class HintProxy(EnumProxy):
    def __init__(self, hint):
        super(HintProxy, self).__init__(hints, hint, _gl.glHint, [hint])

class StringProxy(object):
    def __init__(self, arg, index=None):
        self.arg = arg
        self.index = index

    def __get__(self, obj, cls=None):
        if self.index is None:
            with obj:
                return _gl.string_at(_gl.glGetString(self.arg))
        else:
            with obj:
                _n = _gl.GLint()
                _gl.glGetIntegerv(self.index, _gl.pointer(_n))
                return [_gl.string_at(_gl.glGetStringi(self.arg, i)) for i in range(_n.value)]

class BindingProxy(object):
    def __init__(self, setter, set_args=()):
        self.value = WeakKeyDictionary()
        self.setter = setter
        self.set_args = set_args

    def __get__(self, obj, cls=None):
        return self.value.get(obj, None)

    def __set__(self, obj, value=None):
        with obj:
            self.setter(*([getattr(obj, x) if isinstance(x, basestring) else x for x in self.set_args] + [0 if value is None else value._id]))
        self.value[obj] = value

class TextureUnit(object):
    def __init__(self, _context, _id):
        self._context = _context
        self._id = _id

    def __enter__(self):
        self._context.__enter__()

    def __exit__(self, type, value, traceback):
        self._context.__exit__(type, value, traceback)

    def activate(self):
        self._context.active_texture = self

    texture_binding_1d                   = BindingProxy(_gl.glBindTexture,         [_gl.GL_TEXTURE_1D                  ])
    texture_binding_1d_array             = BindingProxy(_gl.glBindTexture,         [_gl.GL_TEXTURE_1D_ARRAY            ])
    texture_binding_2d                   = BindingProxy(_gl.glBindTexture,         [_gl.GL_TEXTURE_2D                  ])
    texture_binding_2d_array             = BindingProxy(_gl.glBindTexture,         [_gl.GL_TEXTURE_2D_ARRAY            ])
    texture_binding_2d_multisample       = BindingProxy(_gl.glBindTexture,         [_gl.GL_TEXTURE_2D_MULTISAMPLE      ])
    texture_binding_2d_multisample_array = BindingProxy(_gl.glBindTexture,         [_gl.GL_TEXTURE_2D_MULTISAMPLE_ARRAY])
    texture_binding_3d                   = BindingProxy(_gl.glBindTexture,         [_gl.GL_TEXTURE_3D                  ])
    texture_binding_buffer               = BindingProxy(_gl.glBindTexture,         [_gl.GL_TEXTURE_BUFFER              ])
    texture_binding_cube_map             = BindingProxy(_gl.glBindTexture,         [_gl.GL_TEXTURE_CUBE_MAP            ])
    texture_binding_rectangle            = BindingProxy(_gl.glBindTexture,         [_gl.GL_TEXTURE_RECTANGLE           ])
    sampler_binding                      = BindingProxy(_gl.glBindSampler,         ["_unit"                            ])

class TextureUnitList(object):
    def __init__(self, _context):
        self._context = _context
        self._texture_units = [TextureUnit(_context, _gl.GL_TEXTURE0 + i) for i in range(_context.max_combined_texture_image_units)]
        self._context.active_texture = self[0]
        self._bound_textures = dict()

    def __getitem__(self, index):
        return self._texture_units[index]

    def bind(self, texture):
        """Bind `texture` to a free unit and return the unit id."""
        if texture in self._bound_textures:
            unit, refcount = self._bound_textures[texture]
            self._bound_textures[texture] = (unit, refcount + 1)
            return unit._id
        try:
            unit = _itertools.dropwhile(lambda x: getattr(x, texture._binding) is not None, self).next()
        except StopIteration:
            raise RuntimeError("no free texture units available")
        setattr(unit, texture._binding, texture)
        self._bound_textures[texture] = (unit, 1)
        return unit._id

    def release(self, texture):
        """Unbind `texture`."""
        unit, refcount = self._bound_textures[texture]
        if refcount == 1:
            setattr(unit, texture._binding, None)
            del self._bound_textures[texture]
        else:
            self._bound_textures[texture] = (unit, refcount - 1)

class GLObjectLibrary(object):
    def __init__(self, _context):
        self._context = _context
        self._objects = WeakValueDictionary()

    def __getitem__(self, key):
        return self._objects[key]

class Context(object):
    def __enter__(self): pass
    def __exit__(self, type, value, traceback): pass

    def __init__(self):
        self.texture_units = TextureUnitList(self)
        self.buffers = GLObjectLibrary(self)
        self.framebuffers = GLObjectLibrary(self)
        self.program_pipelines = GLObjectLibrary(self)
        self.queries = GLObjectLibrary(self)
        self.renderbuffers = GLObjectLibrary(self)
        self.samplers = GLObjectLibrary(self)
        self.shader_programs = GLObjectLibrary(self)
        self.shaders = GLObjectLibrary(self)
        self.textures = GLObjectLibrary(self)
        self.transform_feedbacks = GLObjectLibrary(self)
        self.vertex_arrays = GLObjectLibrary(self)

    # buffer bindings
    array_buffer_binding                 = BindingProxy(_gl.glBindBuffer,          [_gl.GL_ARRAY_BUFFER                ])
    atomic_counter_buffer_binding        = BindingProxy(_gl.glBindBuffer,          [_gl.GL_ATOMIC_COUNTER_BUFFER       ])
    copy_read_buffer_binding             = BindingProxy(_gl.glBindBuffer,          [_gl.GL_COPY_READ_BUFFER            ])
    copy_write_buffer_binding            = BindingProxy(_gl.glBindBuffer,          [_gl.GL_COPY_WRITE_BUFFER           ])
    draw_indirect_buffer_binding         = BindingProxy(_gl.glBindBuffer,          [_gl.GL_DRAW_INDIRECT_BUFFER        ])
    element_array_buffer_binding         = BindingProxy(_gl.glBindBuffer,          [_gl.GL_ELEMENT_ARRAY_BUFFER        ])
    pixel_pack_buffer_binding            = BindingProxy(_gl.glBindBuffer,          [_gl.GL_PIXEL_PACK_BUFFER           ])
    pixel_unpack_buffer_binding          = BindingProxy(_gl.glBindBuffer,          [_gl.GL_PIXEL_UNPACK_BUFFER         ])
    texture_buffer_binding               = BindingProxy(_gl.glBindBuffer,          [_gl.GL_TEXTURE_BUFFER              ])
    transform_feedback_buffer_binding    = BindingProxy(_gl.glBindBuffer,          [_gl.GL_TRANSFORM_FEEDBACK_BUFFER   ])
    uniform_buffer_binding               = BindingProxy(_gl.glBindBuffer,          [_gl.GL_UNIFORM_BUFFER              ])

    # miscellaneous bindings
    program_pipeline_binding             = BindingProxy(_gl.glBindProgramPipeline, [                                   ])
    renderbuffer_binding                 = BindingProxy(_gl.glBindRenderbuffer,    [_gl.GL_RENDERBUFFER                ])
    vertex_array_binding                 = BindingProxy(_gl.glBindVertexArray,     [                                   ])
    draw_framebuffer_binding             = BindingProxy(_gl.glBindFramebuffer,     [_gl.GL_DRAW_FRAMEBUFFER            ])
    read_framebuffer_binding             = BindingProxy(_gl.glBindFramebuffer,     [_gl.GL_READ_FRAMEBUFFER            ])
    current_program                      = BindingProxy(_gl.glUseProgram,          [                                   ])
    active_texture                       = BindingProxy(_gl.glActiveTexture,       [                                   ])

    # blend function and equation
    blend_dst_alpha = BlendFuncProxy(_gl.GL_BLEND_DST_ALPHA)
    blend_dst_rgb = BlendFuncProxy(_gl.GL_BLEND_DST_RGB)
    blend_src_alpha = BlendFuncProxy(_gl.GL_BLEND_SRC_ALPHA)
    blend_src_rgb = BlendFuncProxy(_gl.GL_BLEND_SRC_RGB)
    blend_equation_alpha = BlendEquationProxy(_gl.GL_BLEND_EQUATION_ALPHA)
    blend_equation_rgb = BlendEquationProxy(_gl.GL_BLEND_EQUATION_RGB)

    # miscellaneous enumerations
    depth_func = EnumProxy(depth_functions, _gl.GL_DEPTH_FUNC, _gl.glDepthFunc)
    draw_buffer = EnumProxy(draw_buffers, _gl.GL_DRAW_BUFFER, _gl.glDrawBuffer)
    implementation_color_read_format = EnumProxy(color_read_formats, _gl.GL_IMPLEMENTATION_COLOR_READ_FORMAT)
    implementation_color_read_type = EnumProxy(color_read_types, _gl.GL_IMPLEMENTATION_COLOR_READ_TYPE)
    layer_provoking_vertex = EnumProxy(provoking_vertices, _gl.GL_LAYER_PROVOKING_VERTEX)
    logic_op_mode = EnumProxy(logic_op_modes, _gl.GL_LOGIC_OP_MODE, _gl.glLogicOp)
    provoking_vertex = EnumProxy(provoke_modes, _gl.GL_PROVOKING_VERTEX, _gl.glProvokingVertex)
    read_buffer = EnumProxy(read_buffers, _gl.GL_READ_BUFFER, _gl.glReadBuffer)
    viewport_index_provoking_vertex = EnumProxy(provoking_vertices, _gl.GL_VIEWPORT_INDEX_PROVOKING_VERTEX)

    # hints
    fragment_shader_derivative_hint = HintProxy(_gl.GL_FRAGMENT_SHADER_DERIVATIVE_HINT)
    line_smooth_hint = HintProxy(_gl.GL_LINE_SMOOTH_HINT)
    polygon_smooth_hint = HintProxy(_gl.GL_POLYGON_SMOOTH_HINT)
    texture_compression_hint = HintProxy(_gl.GL_TEXTURE_COMPRESSION_HINT)

    # enabling and disabling
    blend = EnableDisableProxy(_gl.GL_BLEND)
    color_logic_op = EnableDisableProxy(_gl.GL_COLOR_LOGIC_OP)
    cull_face = EnableDisableProxy(_gl.GL_CULL_FACE)
    depth_test = EnableDisableProxy(_gl.GL_DEPTH_TEST)
    dither = EnableDisableProxy(_gl.GL_DITHER)
    line_smooth = EnableDisableProxy(_gl.GL_LINE_SMOOTH)
    polygon_offset_fill = EnableDisableProxy(_gl.GL_POLYGON_OFFSET_FILL)
    polygon_offset_line = EnableDisableProxy(_gl.GL_POLYGON_OFFSET_LINE)
    polygon_offset_point = EnableDisableProxy(_gl.GL_POLYGON_OFFSET_POINT)
    polygon_smooth = EnableDisableProxy(_gl.GL_POLYGON_SMOOTH)
    scissor_test = EnableDisableProxy(_gl.GL_SCISSOR_TEST)
    stencil_test = EnableDisableProxy(_gl.GL_STENCIL_TEST)
    vertex_program_point_size = EnableDisableProxy(_gl.GL_VERTEX_PROGRAM_POINT_SIZE)

    # boolean values
    color_write_mask = BooleanProxy([_gl.GL_COLOR_WRITEMASK], _gl.glColorMask, shape=4) # TODO indexed variant
    depth_write_mask = BooleanProxy([_gl.GL_DEPTH_WRITEMASK], _gl.glDepthMask)
    doublebuffer = BooleanProxy([_gl.GL_DOUBLEBUFFER])
    pack_lsb_first = BooleanProxy([_gl.GL_PACK_LSB_FIRST], _gl.glPixelStorei, [_gl.GL_PACK_LSB_FIRST])
    pack_swap_bytes = BooleanProxy([_gl.GL_PACK_SWAP_BYTES], _gl.glPixelStorei, [_gl.GL_PACK_SWAP_BYTES])
    shader_compiler = BooleanProxy([_gl.GL_SHADER_COMPILER])
    stereo = BooleanProxy([_gl.GL_STEREO])
    unpack_lsb_first = BooleanProxy([_gl.GL_UNPACK_LSB_FIRST], _gl.glPixelStorei, [_gl.GL_UNPACK_LSB_FIRST])
    unpack_swap_bytes = BooleanProxy([_gl.GL_UNPACK_SWAP_BYTES], _gl.glPixelStorei, [_gl.GL_UNPACK_SWAP_BYTES])
    
    # float values
    aliased_line_width_range = FloatProxy([_gl.GL_ALIASED_LINE_WIDTH_RANGE], shape=2)
    blend_color = FloatProxy([_gl.GL_BLEND_COLOR], _gl.glBlendColor, shape=4)
    color_clear_value = FloatProxy([_gl.GL_COLOR_CLEAR_VALUE], _gl.glClearColor, shape=4)
    depth_clear_value = FloatProxy([_gl.GL_DEPTH_CLEAR_VALUE], _gl.glClearDepth)
    depth_range = FloatProxy([_gl.GL_DEPTH_RANGE], _gl.glDepthRange, shape=2)
    line_width = FloatProxy([_gl.GL_LINE_WIDTH], _gl.glLineWidth)
    line_width_granularity = FloatProxy([_gl.GL_LINE_WIDTH_GRANULARITY])
    line_width_range = FloatProxy([_gl.GL_LINE_WIDTH_RANGE], shape=2)
    point_fade_threshold_size = FloatProxy([_gl.GL_POINT_FADE_THRESHOLD_SIZE], _gl.glPointParameterf, [_gl.GL_POINT_FADE_THRESHOLD_SIZE])
    point_size = FloatProxy([_gl.GL_POINT_SIZE], _gl.glPointSize)
    point_size_granularity = FloatProxy([_gl.GL_POINT_SIZE_GRANULARITY])
    point_size_range = FloatProxy([_gl.GL_POINT_SIZE_RANGE], shape=2)
    smooth_line_width_range = FloatProxy([_gl.GL_SMOOTH_LINE_WIDTH_RANGE], shape=2)
    smooth_line_width_granularity = FloatProxy([_gl.GL_SMOOTH_LINE_WIDTH_GRANULARITY])

    # integer values
    major_version = IntegerProxy([_gl.GL_MAJOR_VERSION])
    max_3d_texture_size = IntegerProxy([_gl.GL_MAX_3D_TEXTURE_SIZE])
    max_array_texture_layers = IntegerProxy([_gl.GL_MAX_3D_TEXTURE_SIZE])
    max_clip_distances = IntegerProxy([_gl.GL_MAX_CLIP_DISTANCES])
    max_color_texture_samples = IntegerProxy([_gl.GL_MAX_COLOR_TEXTURE_SAMPLES])
    max_combined_fragment_uniform_components = IntegerProxy([_gl.GL_MAX_COMBINED_FRAGMENT_UNIFORM_COMPONENTS])
    max_combined_geometry_uniform_components = IntegerProxy([_gl.GL_MAX_COMBINED_GEOMETRY_UNIFORM_COMPONENTS])
    max_combined_texture_image_units = IntegerProxy([_gl.GL_MAX_COMBINED_TEXTURE_IMAGE_UNITS])
    max_combined_uniform_blocks = IntegerProxy([_gl.GL_MAX_COMBINED_UNIFORM_BLOCKS])
    max_combined_vertex_uniform_components = IntegerProxy([_gl.GL_MAX_COMBINED_VERTEX_UNIFORM_COMPONENTS])
    max_cube_map_texture_size = IntegerProxy([_gl.GL_MAX_CUBE_MAP_TEXTURE_SIZE])
    max_depth_texture_samples = IntegerProxy([_gl.GL_MAX_DEPTH_TEXTURE_SAMPLES])
    max_draw_buffers = IntegerProxy([_gl.GL_MAX_DRAW_BUFFERS])
    max_elements_indices = IntegerProxy([_gl.GL_MAX_ELEMENTS_INDICES])
    max_elements_vertices = IntegerProxy([_gl.GL_MAX_ELEMENTS_VERTICES])
    max_fragment_input_components = IntegerProxy([_gl.GL_MAX_FRAGMENT_INPUT_COMPONENTS])
    max_fragment_uniform_components = IntegerProxy([_gl.GL_MAX_FRAGMENT_UNIFORM_COMPONENTS])
    max_fragment_uniform_vectors = IntegerProxy([_gl.GL_MAX_FRAGMENT_UNIFORM_VECTORS])
    max_fragment_uniform_blocks = IntegerProxy([_gl.GL_MAX_FRAGMENT_UNIFORM_BLOCKS])
    max_geometry_input_components = IntegerProxy([_gl.GL_MAX_GEOMETRY_INPUT_COMPONENTS])
    max_geometry_output_components = IntegerProxy([_gl.GL_MAX_GEOMETRY_OUTPUT_COMPONENTS])
    max_geometry_texture_image_units = IntegerProxy([_gl.GL_MAX_GEOMETRY_TEXTURE_IMAGE_UNITS])
    max_geometry_uniform_blocks = IntegerProxy([_gl.GL_MAX_GEOMETRY_UNIFORM_BLOCKS])
    max_geometry_uniform_components = IntegerProxy([_gl.GL_MAX_GEOMETRY_UNIFORM_COMPONENTS])
    max_integer_samples = IntegerProxy([_gl.GL_MAX_INTEGER_SAMPLES])
    max_program_texel_offset = IntegerProxy([_gl.GL_MAX_PROGRAM_TEXEL_OFFSET])
    min_program_texel_offset = IntegerProxy([_gl.GL_MIN_PROGRAM_TEXEL_OFFSET])
    max_rectangle_texture_size = IntegerProxy([_gl.GL_MAX_RECTANGLE_TEXTURE_SIZE])
    max_renderbuffer_size = IntegerProxy([_gl.GL_MAX_RENDERBUFFER_SIZE])
    max_sample_mask_words = IntegerProxy([_gl.GL_MAX_SAMPLE_MASK_WORDS])
    max_server_wait_timeout = IntegerProxy([_gl.GL_MAX_SERVER_WAIT_TIMEOUT])
    max_texture_buffer_size = IntegerProxy([_gl.GL_MAX_TEXTURE_BUFFER_SIZE])
    max_texture_image_units = IntegerProxy([_gl.GL_MAX_TEXTURE_IMAGE_UNITS])
    max_texture_lod_bias = IntegerProxy([_gl.GL_MAX_TEXTURE_LOD_BIAS])
    max_texture_size = IntegerProxy([_gl.GL_MAX_TEXTURE_SIZE])
    max_uniform_buffer_bindings = IntegerProxy([_gl.GL_MAX_UNIFORM_BUFFER_BINDINGS])
    max_uniform_block_size = IntegerProxy([_gl.GL_MAX_UNIFORM_BLOCK_SIZE])
    max_varying_vectors = IntegerProxy([_gl.GL_MAX_VARYING_VECTORS])
    max_vertex_attribs = IntegerProxy([_gl.GL_MAX_VERTEX_ATTRIBS])
    max_vertex_texture_image_units = IntegerProxy([_gl.GL_MAX_VERTEX_TEXTURE_IMAGE_UNITS])
    max_vertex_uniform_components = IntegerProxy([_gl.GL_MAX_VERTEX_UNIFORM_COMPONENTS])
    max_vertex_uniform_vectors = IntegerProxy([_gl.GL_MAX_VERTEX_UNIFORM_VECTORS])
    max_vertex_output_components = IntegerProxy([_gl.GL_MAX_VERTEX_OUTPUT_COMPONENTS])
    max_vertex_uniform_blocks = IntegerProxy([_gl.GL_MAX_VERTEX_UNIFORM_BLOCKS])
    max_viewport_dims = IntegerProxy([_gl.GL_MAX_VIEWPORT_DIMS])
    max_viewports = IntegerProxy([_gl.GL_MAX_VIEWPORTS])
    minor_version = IntegerProxy([_gl.GL_MINOR_VERSION])
    pack_alignment = IntegerProxy([_gl.GL_PACK_ALIGNMENT])
    pack_image_height = IntegerProxy([_gl.GL_PACK_IMAGE_HEIGHT])
    pack_row_length = IntegerProxy([_gl.GL_PACK_ROW_LENGTH], _gl.glPixelStorei, [_gl.GL_PACK_ROW_LENGTH])
    pack_skip_images = IntegerProxy([_gl.GL_PACK_SKIP_IMAGES], _gl.glPixelStorei, [_gl.GL_PACK_SKIP_IMAGES])
    pack_skip_pixels = IntegerProxy([_gl.GL_PACK_SKIP_PIXELS], _gl.glPixelStorei, [_gl.GL_PACK_SKIP_PIXELS])
    pack_skip_rows = IntegerProxy([_gl.GL_PACK_SKIP_ROWS], _gl.glPixelStorei, [_gl.GL_PACK_SKIP_ROWS])
    primitive_restart_index = IntegerProxy([_gl.GL_PRIMITIVE_RESTART_INDEX], _gl.glPrimitiveRestartIndex)
    sample_buffers = IntegerProxy([_gl.GL_SAMPLE_BUFFERS])
    samples = IntegerProxy([_gl.GL_SAMPLES])
    scissor_box = IntegerProxy([_gl.GL_SCISSOR_BOX], _gl.glScissor, shape=4)
    stencil_clear_value = IntegerProxy([_gl.GL_STENCIL_CLEAR_VALUE], _gl.glClearStencil)
    subpixel_bits = IntegerProxy([_gl.GL_SUBPIXEL_BITS])
    uniform_buffer_offset_alignment = IntegerProxy([_gl.GL_UNIFORM_BUFFER_OFFSET_ALIGNMENT])
    unpack_alignment = IntegerProxy([_gl.GL_UNPACK_ALIGNMENT], _gl.glPixelStorei, [_gl.GL_UNPACK_ALIGNMENT])
    unpack_image_height = IntegerProxy([_gl.GL_UNPACK_IMAGE_HEIGHT], _gl.glPixelStorei, [_gl.GL_UNPACK_IMAGE_HEIGHT])
    unpack_row_length = IntegerProxy([_gl.GL_UNPACK_ROW_LENGTH], _gl.glPixelStorei, [_gl.GL_UNPACK_ROW_LENGTH])
    unpack_skip_images = IntegerProxy([_gl.GL_UNPACK_SKIP_IMAGES], _gl.glPixelStorei, [_gl.GL_UNPACK_SKIP_IMAGES])
    unpack_skip_pixels = IntegerProxy([_gl.GL_UNPACK_SKIP_PIXELS], _gl.glPixelStorei, [_gl.GL_UNPACK_SKIP_PIXELS])
    unpack_skip_rows = IntegerProxy([_gl.GL_UNPACK_SKIP_ROWS], _gl.glPixelStorei, [_gl.GL_UNPACK_SKIP_ROWS])
    viewport = IntegerProxy([_gl.GL_VIEWPORT], _gl.glViewport, shape=4) # TODO indexed variant as float
    viewport_bounds_range = IntegerProxy([_gl.GL_VIEWPORT_BOUNDS_RANGE], shape=2)
    viewport_subpixel_bits = IntegerProxy([_gl.GL_VIEWPORT_SUBPIXEL_BITS])

    # 64-bit integer values
    timestamp = Integer64Proxy([_gl.GL_TIMESTAMP])

    # strings
    vendor = StringProxy(_gl.GL_VENDOR)
    renderer = StringProxy(_gl.GL_RENDERER)
    version = StringProxy(_gl.GL_VERSION)
    shading_language_version = StringProxy(_gl.GL_SHADING_LANGUAGE_VERSION)
    extensions = StringProxy(_gl.GL_EXTENSIONS, _gl.GL_NUM_EXTENSIONS)

    # TODO GL_DRAW_BUFFERi
    # TODO GL_POLYGON_OFFSET_FACTOR, GL_POLYGON_OFFSET_UNITS (glPolygonOffset)
    # TODO GL_SAMPLE_COVERAGE_VALUE, GL_SAMPLE_COVERAGE_INVERT (glSampleCoverage)
    # TODO indexed GL_TRANSFORM_FEEDBACK_BUFFER_START, GL_TRANSFORM_FEEDBACK_BUFFER_SIZE
    # TODO indexed GL_UNIFORM_BUFFER_SIZE, GL_UNIFORM_BUFFER_START

    # TODO stencil:
    # GL_STENCIL_BACK_FAIL, GL_STENCIL_BACK_PASS_DEPTH_FAIL, GL_STENCIL_BACK_PASS_DEPTH_PASS, GL_STENCIL_FAIL, GL_STENCIL_PASS_DEPTH_FAIL, GL_STENCIL_PASS_DEPTH_PASS...
    # GL_STENCIL_BACK_FUNC, GL_STENCIL_FUNC
    # GL_STENCIL_BACK_REF, GL_STENCIL_REF, GL_STENCIL_BACK_VALUE_MASK, GL_STENCIL_BACK_WRITEMASK, GL_STENCIL_VALUE_MASK, GL_STENCIL_WRITEMASK

def get_default_context(context=None):
    if context is None:
        context = Context() # TODO
    return context


# nosetests

def check_property(context, name):
    from util import EnumConstant
    value = getattr(context, name)
    try:
        if isinstance(value, EnumConstant):
            if name in ("draw_buffer", "read_buffer"):
                return # avoid problems with unavailable stereo buffers
            valid_values = value._enum._reverse_dict.values()
            for value in valid_values:
                setattr(context, name, value)
                assert _np.all(getattr(context, name) == value), "property %s is broken" % name
        else:
            if type(value) is float:
                value *= 0.5
                setattr(context, name, value)
                assert _np.all(getattr(context, name) == value), "property %s is broken" % name
                value += 0.5
                setattr(context, name, value)
                assert _np.all(getattr(context, name) == value), "property %s is broken" % name
    except AttributeError:
        pass # "AttributeError: can't set attribute" is okay for read-only attributes

def test_property_generator():
    context = Context()
    properties = [x for x in dir(context) if not x.startswith("_")]

    for p in properties:
        yield check_property, context, p

if __name__ == "__main__": # DEBUG
    from glut import GlutWindow
    GlutWindow()
    context = Context() 
    for x in dir(context):
        if not x.startswith("_"):
            print "%40s : %s" % (x, getattr(context, x))

