import numpy as _np
from rawgl import gl as _gl

from constants import blend_functions, blend_equations, depth_functions, draw_buffers, hints, provoking_vertices, logic_op_modes, provoke_modes, color_read_formats, color_read_types, read_buffers
from dtypes import bool8, int32, int64, float32, float64

# TODO with statements for state changes, e.g. with context.set(active_texture=0): ...
# TODO default context singleton

class Proxy(object):
    def __init__(self, getter=None, get_args=(), setter=None, set_args=(), dtype=None, shape=None):
        self._getter = getter
        self._get_args = get_args
        self._setter = setter
        self._set_args = set_args
        if dtype is None:
            dtype = {
                    "glGetBooleani_v": bool8,
                    "glGetBooleanv": bool8,
                    "glGetDoublev": float64,
                    "glGetFloatv": float32,
                    "glGetInteger64i_v": int64,
                    "glGetInteger64v": int64,
                    "glGetIntegeri_v": int32,
                    "glGetIntegerv": int32,
                    }[getter.__name__]

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

class Context(object): # TODO this should be bindable, but that is window system dependent
    def __enter__(self): pass
    def __exit__(self, type, value, traceback): pass

    #active_texture = ActiveTextureProxy(_gl.glGetIntegerv, [_gl.GL_ACTIVE_TEXTURE], _gl.glActiveTexture) # TODO subtract GL_TEXTURE0
    aliased_line_width_range = Proxy(_gl.glGetFloatv, [_gl.GL_ALIASED_LINE_WIDTH_RANGE], shape=2)
    array_buffer_binding = Proxy(_gl.glGetIntegerv, [_gl.GL_ARRAY_BUFFER_BINDING], _gl.glBindBuffer, [_gl.GL_ARRAY_BUFFER]) # TODO buffer obj
    blend = EnableDisableProxy(_gl.GL_BLEND)
    blend_color = Proxy(_gl.glGetFloatv, [_gl.GL_BLEND_COLOR], _gl.glBlendColor, shape=4)
    blend_dst_alpha = BlendFuncProxy(_gl.GL_BLEND_DST_ALPHA)
    blend_dst_rgb = BlendFuncProxy(_gl.GL_BLEND_DST_RGB)
    blend_src_alpha = BlendFuncProxy(_gl.GL_BLEND_SRC_ALPHA)
    blend_src_rgb = BlendFuncProxy(_gl.GL_BLEND_SRC_RGB)
    blend_equation_alpha = BlendEquationProxy(_gl.GL_BLEND_EQUATION_ALPHA)
    blend_equation_rgb = BlendEquationProxy(_gl.GL_BLEND_EQUATION_RGB)
    color_clear_value = Proxy(_gl.glGetFloatv, [_gl.GL_COLOR_CLEAR_VALUE], _gl.glClearColor, shape=4)
    color_logic_op = EnableDisableProxy(_gl.GL_COLOR_LOGIC_OP)
    color_write_mask = Proxy(_gl.glGetBooleanv, [_gl.GL_COLOR_WRITEMASK], _gl.glColorMask, shape=4) # TODO indexed variant
    # TODO GL_COMPRESSED_TEXTURE_FORMATS
    # TODO GL_CONTEXT_FLAGS
    cull_face = EnableDisableProxy(_gl.GL_CULL_FACE)
    current_program = Proxy(_gl.glGetIntegerv, [_gl.GL_CURRENT_PROGRAM], _gl.glUseProgram) # TODO program obj
    depth_clear_value = Proxy(_gl.glGetFloatv, [_gl.GL_DEPTH_CLEAR_VALUE], _gl.glClearDepth)
    depth_func = EnumProxy(depth_functions, _gl.GL_DEPTH_FUNC, _gl.glDepthFunc)
    depth_range = Proxy(_gl.glGetFloatv, [_gl.GL_DEPTH_RANGE], _gl.glDepthRange, shape=2)
    depth_test = EnableDisableProxy(_gl.GL_DEPTH_TEST)
    depth_write_mask = Proxy(_gl.glGetBooleanv, [_gl.GL_DEPTH_WRITEMASK], _gl.glDepthMask)
    dither = EnableDisableProxy(_gl.GL_DITHER)
    doublebuffer = Proxy(_gl.glGetBooleanv, [_gl.GL_DOUBLEBUFFER])
    draw_buffer = EnumProxy(draw_buffers, _gl.GL_DRAW_BUFFER, _gl.glDrawBuffer)
    # TODO GL_DRAW_BUFFERi
    # XXX draw_framebuffer_binding = Proxy(_gl.glGetIntegerv, [_gl.GL_DRAW_FRAMEBUFFER_BINDING], _gl.glBindFramebuffer, [_gl.GL_DRAW_FRAMEBUFFER]) # TODO buffer obj
    # XXX read_framebuffer_binding = Proxy(_gl.glGetIntegerv, [_gl.GL_READ_FRAMEBUFFER_BINDING], _gl.glBindFramebuffer, [_gl.GL_READ_FRAMEBUFFER]) # TODO buffer obj
    element_array_buffer_binding = Proxy(_gl.glGetIntegerv, [_gl.GL_ELEMENT_ARRAY_BUFFER_BINDING], _gl.glBindBuffer, [_gl.GL_ELEMENT_ARRAY_BUFFER]) # TODO buffer obj
    fragment_shader_derivative_hint = EnumProxy(hints, _gl.GL_FRAGMENT_SHADER_DERIVATIVE_HINT, _gl.glHint, [_gl.GL_FRAGMENT_SHADER_DERIVATIVE_HINT])
    implementation_color_read_format = EnumProxy(color_read_formats, _gl.GL_IMPLEMENTATION_COLOR_READ_FORMAT)
    implementation_color_read_type = EnumProxy(color_read_types, _gl.GL_IMPLEMENTATION_COLOR_READ_TYPE)
    line_smooth = EnableDisableProxy(_gl.GL_LINE_SMOOTH)
    line_smooth_hint = EnumProxy(hints, _gl.GL_LINE_SMOOTH_HINT, _gl.glHint, [_gl.GL_LINE_SMOOTH_HINT])
    line_width = Proxy(_gl.glGetFloatv, [_gl.GL_LINE_WIDTH], _gl.glLineWidth)
    layer_provoking_vertex = EnumProxy(provoking_vertices, _gl.GL_LAYER_PROVOKING_VERTEX)
    line_width_granularity = Proxy(_gl.glGetFloatv, [_gl.GL_LINE_WIDTH_GRANULARITY])
    line_width_range = Proxy(_gl.glGetFloatv, [_gl.GL_LINE_WIDTH_RANGE], shape=2)
    logic_op_mode = EnumProxy(logic_op_modes, _gl.GL_LOGIC_OP_MODE, _gl.glLogicOp)
    major_version = Proxy(_gl.glGetIntegerv, [_gl.GL_MAJOR_VERSION])
    max_3d_texture_size = Proxy(_gl.glGetIntegerv, [_gl.GL_MAX_3D_TEXTURE_SIZE])
    max_array_texture_layers = Proxy(_gl.glGetIntegerv, [_gl.GL_MAX_3D_TEXTURE_SIZE])
    max_clip_distances = Proxy(_gl.glGetIntegerv, [_gl.GL_MAX_CLIP_DISTANCES])
    max_color_texture_samples = Proxy(_gl.glGetIntegerv, [_gl.GL_MAX_COLOR_TEXTURE_SAMPLES])
    # XXX max_combined_atomic_counters = Proxy(_gl.glGetIntegerv, [_gl.GL_MAX_COMBINED_ATOMIC_COUNTERS])
    max_combined_fragment_uniform_components = Proxy(_gl.glGetIntegerv, [_gl.GL_MAX_COMBINED_FRAGMENT_UNIFORM_COMPONENTS])
    max_combined_geometry_uniform_components = Proxy(_gl.glGetIntegerv, [_gl.GL_MAX_COMBINED_GEOMETRY_UNIFORM_COMPONENTS])
    max_combined_texture_image_units = Proxy(_gl.glGetIntegerv, [_gl.GL_MAX_COMBINED_TEXTURE_IMAGE_UNITS])
    max_combined_uniform_blocks = Proxy(_gl.glGetIntegerv, [_gl.GL_MAX_COMBINED_UNIFORM_BLOCKS])
    max_combined_vertex_uniform_components = Proxy(_gl.glGetIntegerv, [_gl.GL_MAX_COMBINED_VERTEX_UNIFORM_COMPONENTS])
    max_cube_map_texture_size = Proxy(_gl.glGetIntegerv, [_gl.GL_MAX_CUBE_MAP_TEXTURE_SIZE])
    max_depth_texture_samples = Proxy(_gl.glGetIntegerv, [_gl.GL_MAX_DEPTH_TEXTURE_SAMPLES])
    max_draw_buffers = Proxy(_gl.glGetIntegerv, [_gl.GL_MAX_DRAW_BUFFERS])
    # XXX max_dualsource_draw_buffers = Proxy(_gl.glGetIntegerv, [_gl.GL_MAX_DUALSOURCE_DRAW_BUFFERS])
    max_elements_indices = Proxy(_gl.glGetIntegerv, [_gl.GL_MAX_ELEMENTS_INDICES])
    max_elements_vertices = Proxy(_gl.glGetIntegerv, [_gl.GL_MAX_ELEMENTS_VERTICES])
    # XXX max_fragment_atomic_counters = Proxy(_gl.glGetIntegerv, [_gl.GL_MAX_FRAGMENT_ATOMIC_COUNTERS])
    max_fragment_input_components = Proxy(_gl.glGetIntegerv, [_gl.GL_MAX_FRAGMENT_INPUT_COMPONENTS])
    max_fragment_uniform_components = Proxy(_gl.glGetIntegerv, [_gl.GL_MAX_FRAGMENT_UNIFORM_COMPONENTS])
    max_fragment_uniform_vectors = Proxy(_gl.glGetIntegerv, [_gl.GL_MAX_FRAGMENT_UNIFORM_VECTORS])
    max_fragment_uniform_blocks = Proxy(_gl.glGetIntegerv, [_gl.GL_MAX_FRAGMENT_UNIFORM_BLOCKS])
    # XXX max_geometry_atomic_counters = Proxy(_gl.glGetIntegerv, [_gl.GL_MAX_GEOMETRY_ATOMIC_COUNTERS])
    max_geometry_input_components = Proxy(_gl.glGetIntegerv, [_gl.GL_MAX_GEOMETRY_INPUT_COMPONENTS])
    max_geometry_output_components = Proxy(_gl.glGetIntegerv, [_gl.GL_MAX_GEOMETRY_OUTPUT_COMPONENTS])
    max_geometry_texture_image_units = Proxy(_gl.glGetIntegerv, [_gl.GL_MAX_GEOMETRY_TEXTURE_IMAGE_UNITS])
    max_geometry_uniform_blocks = Proxy(_gl.glGetIntegerv, [_gl.GL_MAX_GEOMETRY_UNIFORM_BLOCKS])
    max_geometry_uniform_components = Proxy(_gl.glGetIntegerv, [_gl.GL_MAX_GEOMETRY_UNIFORM_COMPONENTS])
    max_integer_samples = Proxy(_gl.glGetIntegerv, [_gl.GL_MAX_INTEGER_SAMPLES])
    # XXX min_map_buffer_alignment = Proxy(_gl.glGetIntegerv, [_gl.GL_MIN_MAP_BUFFER_ALIGNMENT])
    max_program_texel_offset = Proxy(_gl.glGetIntegerv, [_gl.GL_MAX_PROGRAM_TEXEL_OFFSET])
    min_program_texel_offset = Proxy(_gl.glGetIntegerv, [_gl.GL_MIN_PROGRAM_TEXEL_OFFSET])
    max_rectangle_texture_size = Proxy(_gl.glGetIntegerv, [_gl.GL_MAX_RECTANGLE_TEXTURE_SIZE])
    max_renderbuffer_size = Proxy(_gl.glGetIntegerv, [_gl.GL_MAX_RENDERBUFFER_SIZE])
    max_sample_mask_words = Proxy(_gl.glGetIntegerv, [_gl.GL_MAX_SAMPLE_MASK_WORDS])
    max_server_wait_timeout = Proxy(_gl.glGetIntegerv, [_gl.GL_MAX_SERVER_WAIT_TIMEOUT])
    # XXX max_tess_control_atomic_counters = Proxy(_gl.glGetIntegerv, [_gl.GL_MAX_TESS_CONTROL_ATOMIC_COUNTERS])
    # XXX max_tess_evaluation_atomic_counters = Proxy(_gl.glGetIntegerv, [_gl.GL_MAX_TESS_EVALUATION_ATOMIC_COUNTERS])
    max_texture_buffer_size = Proxy(_gl.glGetIntegerv, [_gl.GL_MAX_TEXTURE_BUFFER_SIZE])
    max_texture_image_units = Proxy(_gl.glGetIntegerv, [_gl.GL_MAX_TEXTURE_IMAGE_UNITS])
    max_texture_lod_bias = Proxy(_gl.glGetIntegerv, [_gl.GL_MAX_TEXTURE_LOD_BIAS])
    max_texture_size = Proxy(_gl.glGetIntegerv, [_gl.GL_MAX_TEXTURE_SIZE])
    max_uniform_buffer_bindings = Proxy(_gl.glGetIntegerv, [_gl.GL_MAX_UNIFORM_BUFFER_BINDINGS])
    max_uniform_block_size = Proxy(_gl.glGetIntegerv, [_gl.GL_MAX_UNIFORM_BLOCK_SIZE])
    # XXX max_varying_components = Proxy(_gl.glGetIntegerv, [_gl.GL_MAX_VARYING_COMPONENTS])
    max_varying_vectors = Proxy(_gl.glGetIntegerv, [_gl.GL_MAX_VARYING_VECTORS])
    # XXX max_varying_floats = Proxy(_gl.glGetIntegerv, [_gl.GL_MAX_VARYING_FLOATS])
    # XXX max_vertex_atomic_counters = Proxy(_gl.glGetIntegerv, [_gl.GL_MAX_VERTEX_ATOMIC_COUNTERS])
    max_vertex_attribs = Proxy(_gl.glGetIntegerv, [_gl.GL_MAX_VERTEX_ATTRIBS])
    max_vertex_texture_image_units = Proxy(_gl.glGetIntegerv, [_gl.GL_MAX_VERTEX_TEXTURE_IMAGE_UNITS])
    max_vertex_uniform_components = Proxy(_gl.glGetIntegerv, [_gl.GL_MAX_VERTEX_UNIFORM_COMPONENTS])
    max_vertex_uniform_vectors = Proxy(_gl.glGetIntegerv, [_gl.GL_MAX_VERTEX_UNIFORM_VECTORS])
    max_vertex_output_components = Proxy(_gl.glGetIntegerv, [_gl.GL_MAX_VERTEX_OUTPUT_COMPONENTS])
    max_vertex_uniform_blocks = Proxy(_gl.glGetIntegerv, [_gl.GL_MAX_VERTEX_UNIFORM_BLOCKS])
    max_viewport_dims = Proxy(_gl.glGetIntegerv, [_gl.GL_MAX_VIEWPORT_DIMS])
    max_viewports = Proxy(_gl.glGetIntegerv, [_gl.GL_MAX_VIEWPORTS])
    minor_version = Proxy(_gl.glGetIntegerv, [_gl.GL_MINOR_VERSION])
    num_compressed_texture_formats = Proxy(_gl.glGetIntegerv, [_gl.GL_NUM_COMPRESSED_TEXTURE_FORMATS])
    num_extensions = Proxy(_gl.glGetIntegerv, [_gl.GL_NUM_EXTENSIONS])
    num_program_binary_formats = Proxy(_gl.glGetIntegerv, [_gl.GL_NUM_PROGRAM_BINARY_FORMATS])
    num_shader_binary_formats = Proxy(_gl.glGetIntegerv, [_gl.GL_NUM_SHADER_BINARY_FORMATS])
    pack_alignment = Proxy(_gl.glGetIntegerv, [_gl.GL_PACK_ALIGNMENT])
    pack_image_height = Proxy(_gl.glGetIntegerv, [_gl.GL_PACK_IMAGE_HEIGHT])
    pack_lsb_first = Proxy(_gl.glGetBooleanv, [_gl.GL_PACK_LSB_FIRST], _gl.glPixelStorei, [_gl.GL_PACK_LSB_FIRST])
    pack_row_length = Proxy(_gl.glGetIntegerv, [_gl.GL_PACK_ROW_LENGTH], _gl.glPixelStorei, [_gl.GL_PACK_ROW_LENGTH])
    pack_skip_images = Proxy(_gl.glGetIntegerv, [_gl.GL_PACK_SKIP_IMAGES], _gl.glPixelStorei, [_gl.GL_PACK_SKIP_IMAGES])
    pack_skip_pixels = Proxy(_gl.glGetIntegerv, [_gl.GL_PACK_SKIP_PIXELS], _gl.glPixelStorei, [_gl.GL_PACK_SKIP_PIXELS])
    pack_skip_rows = Proxy(_gl.glGetIntegerv, [_gl.GL_PACK_SKIP_ROWS], _gl.glPixelStorei, [_gl.GL_PACK_SKIP_ROWS])
    pack_swap_bytes = Proxy(_gl.glGetBooleanv, [_gl.GL_PACK_SWAP_BYTES], _gl.glPixelStorei, [_gl.GL_PACK_SWAP_BYTES])
    pixel_pack_buffer_binding = Proxy(_gl.glGetIntegerv, [_gl.GL_PIXEL_PACK_BUFFER_BINDING], _gl.glBindBuffer, [_gl.GL_PIXEL_PACK_BUFFER]) # TODO buffer obj
    pixel_unpack_buffer_binding = Proxy(_gl.glGetIntegerv, [_gl.GL_PIXEL_UNPACK_BUFFER_BINDING], _gl.glBindBuffer, [_gl.GL_PIXEL_UNPACK_BUFFER]) # TODO buffer obj
    point_fade_threshold_size = Proxy(_gl.glGetFloatv, [_gl.GL_POINT_FADE_THRESHOLD_SIZE], _gl.glPointParameterf, [_gl.GL_POINT_FADE_THRESHOLD_SIZE])
    primitive_restart_index = Proxy(_gl.glGetIntegerv, [_gl.GL_PRIMITIVE_RESTART_INDEX], _gl.glPrimitiveRestartIndex)
    # TODO GL_PROGRAM_BINARY_FORMATS
    program_pipeline_binding = Proxy(_gl.glGetIntegerv, [_gl.GL_PROGRAM_PIPELINE_BINDING], _gl.glBindProgramPipeline)
    provoking_vertex = EnumProxy(provoke_modes, _gl.GL_PROVOKING_VERTEX, _gl.glProvokingVertex)
    point_size = Proxy(_gl.glGetFloatv, [_gl.GL_POINT_SIZE], _gl.glPointSize)
    point_size_granularity = Proxy(_gl.glGetFloatv, [_gl.GL_POINT_SIZE_GRANULARITY])
    point_size_range = Proxy(_gl.glGetFloatv, [_gl.GL_POINT_SIZE_RANGE], shape=2)
    # TODO glPolygonMode
    # TODO GL_POLYGON_OFFSET_FACTOR, GL_POLYGON_OFFSET_UNITS (glPolygonOffset)
    polygon_offset_fill = EnableDisableProxy(_gl.GL_POLYGON_OFFSET_FILL)
    polygon_offset_line = EnableDisableProxy(_gl.GL_POLYGON_OFFSET_LINE)
    polygon_offset_point = EnableDisableProxy(_gl.GL_POLYGON_OFFSET_POINT)
    polygon_smooth = EnableDisableProxy(_gl.GL_POLYGON_SMOOTH)
    polygon_smooth_hint = EnumProxy(hints, _gl.GL_POLYGON_SMOOTH_HINT, _gl.glHint, [_gl.GL_POLYGON_SMOOTH_HINT])
    read_buffer = EnumProxy(read_buffers, _gl.GL_READ_BUFFER, _gl.glReadBuffer)
    renderbuffer_binding = Proxy(_gl.glGetIntegerv, [_gl.GL_RENDERBUFFER_BINDING], _gl.glBindRenderbuffer, [_gl.GL_RENDERBUFFER]) # TODO renderbuffer obj
    sample_buffers = Proxy(_gl.glGetIntegerv, [_gl.GL_SAMPLE_BUFFERS])
    # TODO GL_SAMPLE_COVERAGE_VALUE, GL_SAMPLE_COVERAGE_INVERT (glSampleCoverage)
    sampler_binding = Proxy(_gl.glGetIntegerv, [_gl.GL_SAMPLER_BINDING]) # TODO setter: bind to active texture unit
    samples = Proxy(_gl.glGetIntegerv, [_gl.GL_SAMPLES])
    scissor_box = Proxy(_gl.glGetIntegerv, [_gl.GL_SCISSOR_BOX], _gl.glScissor, shape=4)
    scissor_test = EnableDisableProxy(_gl.GL_SCISSOR_TEST)
    shader_compiler = Proxy(_gl.glGetBooleanv, [_gl.GL_SHADER_COMPILER])
    smooth_line_width_range = Proxy(_gl.glGetFloatv, [_gl.GL_SMOOTH_LINE_WIDTH_RANGE], shape=2)
    smooth_line_width_granularity = Proxy(_gl.glGetFloatv, [_gl.GL_SMOOTH_LINE_WIDTH_GRANULARITY])
    # TODO GL_STENCIL_BACK_FAIL, GL_STENCIL_BACK_PASS_DEPTH_FAIL, GL_STENCIL_BACK_PASS_DEPTH_PASS,
    #      GL_STENCIL_FAIL, GL_STENCIL_PASS_DEPTH_FAIL, GL_STENCIL_PASS_DEPTH_PASS...
    # TODO GL_STENCIL_BACK_FUNC, GL_STENCIL_FUNC, 
    # TODO GL_STENCIL_BACK_REF, GL_STENCIL_REF, GL_STENCIL_BACK_VALUE_MASK, GL_STENCIL_BACK_WRITEMASK, GL_STENCIL_VALUE_MASK, GL_STENCIL_WRITEMASK
    stencil_clear_value = Proxy(_gl.glGetIntegerv, [_gl.GL_STENCIL_CLEAR_VALUE], _gl.glClearStencil)
    stencil_test = EnableDisableProxy(_gl.GL_STENCIL_TEST)
    stereo = Proxy(_gl.glGetBooleanv, [_gl.GL_STEREO])
    subpixel_bits = Proxy(_gl.glGetIntegerv, [_gl.GL_SUBPIXEL_BITS])
    texture_binding_1d = Proxy(_gl.glGetIntegerv, [_gl.GL_TEXTURE_BINDING_1D], _gl.glBindTexture, [_gl.GL_TEXTURE_1D]) # TODO texture obj
    texture_binding_1d_array = Proxy(_gl.glGetIntegerv, [_gl.GL_TEXTURE_BINDING_1D_ARRAY], _gl.glBindTexture, [_gl.GL_TEXTURE_1D_ARRAY]) # TODO texture obj
    texture_binding_2d = Proxy(_gl.glGetIntegerv, [_gl.GL_TEXTURE_BINDING_2D], _gl.glBindTexture, [_gl.GL_TEXTURE_2D]) # TODO texture obj
    texture_binding_2d_array = Proxy(_gl.glGetIntegerv, [_gl.GL_TEXTURE_BINDING_2D_ARRAY], _gl.glBindTexture, [_gl.GL_TEXTURE_2D_ARRAY]) # TODO texture obj
    texture_binding_2d_multisample = Proxy(_gl.glGetIntegerv, [_gl.GL_TEXTURE_BINDING_2D_MULTISAMPLE], _gl.glBindTexture, [_gl.GL_TEXTURE_2D_MULTISAMPLE]) # TODO texture obj
    texture_binding_2d_multisample_array = Proxy(_gl.glGetIntegerv, [_gl.GL_TEXTURE_BINDING_2D_MULTISAMPLE_ARRAY], _gl.glBindTexture, [_gl.GL_TEXTURE_2D_MULTISAMPLE_ARRAY]) # TODO texture obj
    texture_binding_3d = Proxy(_gl.glGetIntegerv, [_gl.GL_TEXTURE_BINDING_3D], _gl.glBindTexture, [_gl.GL_TEXTURE_3D]) # TODO texture obj
    texture_binding_buffer = Proxy(_gl.glGetIntegerv, [_gl.GL_TEXTURE_BINDING_BUFFER], _gl.glBindTexture, [_gl.GL_TEXTURE_BUFFER]) # TODO texture obj
    texture_binding_cube_map = Proxy(_gl.glGetIntegerv, [_gl.GL_TEXTURE_BINDING_CUBE_MAP], _gl.glBindTexture, [_gl.GL_TEXTURE_CUBE_MAP]) # TODO texture obj
    texture_binding_rectangle = Proxy(_gl.glGetIntegerv, [_gl.GL_TEXTURE_BINDING_RECTANGLE], _gl.glBindTexture, [_gl.GL_TEXTURE_RECTANGLE]) # TODO texture obj
    texture_compression_hint = EnumProxy(hints, _gl.GL_TEXTURE_COMPRESSION_HINT, _gl.glHint, [_gl.GL_TEXTURE_COMPRESSION_HINT]) # TODO texture obj
    # TODO texture_buffer_binding = Proxy(_gl.glGetIntegerv, [_gl.GL_TEXTURE_BUFFER_BINDING], _gl.glBindBuffer, [_gl.GL_TEXTURE_BUFFER]) # TODO buffer obj
    timestamp = Proxy(_gl.glGetInteger64v, [_gl.GL_TIMESTAMP])
    transform_feedback_buffer_binding = Proxy(_gl.glGetIntegerv, [_gl.GL_TRANSFORM_FEEDBACK_BUFFER_BINDING], _gl.glBindBuffer, [_gl.GL_TRANSFORM_FEEDBACK_BUFFER]) # TODO buffer obj TODO indexed variant
    # TODO indexed GL_TRANSFORM_FEEDBACK_BUFFER_START, GL_TRANSFORM_FEEDBACK_BUFFER_SIZE
    uniform_buffer_binding = Proxy(_gl.glGetIntegerv, [_gl.GL_UNIFORM_BUFFER_BINDING], _gl.glBindBuffer, [_gl.GL_UNIFORM_BUFFER]) # TODO buffer obj
    uniform_buffer_offset_alignment = Proxy(_gl.glGetIntegerv, [_gl.GL_UNIFORM_BUFFER_OFFSET_ALIGNMENT])
    # TODO indexed GL_UNIFORM_BUFFER_SIZE, GL_UNIFORM_BUFFER_START
    unpack_alignment = Proxy(_gl.glGetIntegerv, [_gl.GL_UNPACK_ALIGNMENT], _gl.glPixelStorei, [_gl.GL_UNPACK_ALIGNMENT])
    unpack_image_height = Proxy(_gl.glGetIntegerv, [_gl.GL_UNPACK_IMAGE_HEIGHT], _gl.glPixelStorei, [_gl.GL_UNPACK_IMAGE_HEIGHT])
    unpack_lsb_first = Proxy(_gl.glGetBooleanv, [_gl.GL_UNPACK_LSB_FIRST], _gl.glPixelStorei, [_gl.GL_UNPACK_LSB_FIRST])
    unpack_row_length = Proxy(_gl.glGetIntegerv, [_gl.GL_UNPACK_ROW_LENGTH], _gl.glPixelStorei, [_gl.GL_UNPACK_ROW_LENGTH])
    unpack_skip_images = Proxy(_gl.glGetIntegerv, [_gl.GL_UNPACK_SKIP_IMAGES], _gl.glPixelStorei, [_gl.GL_UNPACK_SKIP_IMAGES])
    unpack_skip_pixels = Proxy(_gl.glGetIntegerv, [_gl.GL_UNPACK_SKIP_PIXELS], _gl.glPixelStorei, [_gl.GL_UNPACK_SKIP_PIXELS])
    unpack_skip_rows = Proxy(_gl.glGetIntegerv, [_gl.GL_UNPACK_SKIP_ROWS], _gl.glPixelStorei, [_gl.GL_UNPACK_SKIP_ROWS])
    unpack_swap_bytes = Proxy(_gl.glGetBooleanv, [_gl.GL_UNPACK_SWAP_BYTES], _gl.glPixelStorei, [_gl.GL_UNPACK_SWAP_BYTES])
    vertex_program_point_size = EnableDisableProxy(_gl.GL_VERTEX_PROGRAM_POINT_SIZE)
    viewport = Proxy(_gl.glGetIntegerv, [_gl.GL_VIEWPORT], _gl.glViewport, shape=4) # TODO indexed variant
    viewport_bounds_range = Proxy(_gl.glGetIntegerv, [_gl.GL_VIEWPORT_BOUNDS_RANGE], shape=2)
    viewport_index_provoking_vertex = EnumProxy(provoking_vertices, _gl.GL_VIEWPORT_INDEX_PROVOKING_VERTEX)
    viewport_subpixel_bits = Proxy(_gl.glGetIntegerv, [_gl.GL_VIEWPORT_SUBPIXEL_BITS])


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

