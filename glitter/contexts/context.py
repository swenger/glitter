"""Base class for OpenGL contexts.

This module wraps large parts of per-context state.

@todo: Provide convenience setters for C{glBlendFunc} via C{blend_func=("SRC_ALPHA", "ONE_MINUS_SRC_ALPHA")}.
@todo: Add listing of all bound textures, buffers, etc.
@todo: Do we need indexed variants for C{glEnable}?
@todo: Wrap C{glPatchParameter}.
@todo: Implement multiple viewports using C{glViewportIndexed}, C{glViewportArray}, C{glScissorIndexed}, and C{glScissorArray}.
@todo: Wrap C{glSampleCoverage}, C{glSampleMaski}, C{glMinSampleShading}, C{GL_SAMPLE_COVERAGE_VALUE}, and C{GL_SAMPLE_COVERAGE_INVERT}.
@todo: Wrap C{glReadPixels} and related framebuffer copy functions.
@todo: Add indexed getters for C{GL_TRANSFORM_FEEDBACK_BUFFER_START},
C{GL_TRANSFORM_FEEDBACK_BUFFER_SIZE}, C{GL_UNIFORM_BUFFER_SIZE} and
C{GL_UNIFORM_BUFFER_START}.
@todo: Add getters for C{GL_CLIP_DISTANCEi}, C{GL_DEPTH_CLAMP},
C{GL_FRAMEBUFFER_SRGB}, C{GL_MULTISAMPLE}, C{GL_PRIMITIVE_RESTART}, 
C{GL_TEXTURE_CUBE_MAP_SEAMLESS}, C{GL_SAMPLE_ALPHA_TO_ONE},
C{GL_SAMPLE_ALPHA_TO_COVERAGE}, C{GL_SAMPLE_COVERAGE}, C{GL_SAMPLE_SHADING},
and C{GL_SAMPLE_MASK}.
@todo: Implement stencil buffers using C{GL_STENCIL_BACK_FUNC},
C{GL_STENCIL_FUNC}, C{GL_STENCIL_BACK_REF}, C{GL_STENCIL_REF},
C{GL_STENCIL_BACK_VALUE_MASK}, C{GL_STENCIL_BACK_WRITEMASK},
C{GL_STENCIL_VALUE_MASK}, C{GL_STENCIL_WRITEMASK}, C{GL_STENCIL_BACK_FAIL},
C{GL_STENCIL_BACK_PASS_DEPTH_FAIL}, C{GL_STENCIL_BACK_PASS_DEPTH_PASS},
C{GL_STENCIL_FAIL}, C{GL_STENCIL_PASS_DEPTH_FAIL},
C{GL_STENCIL_PASS_DEPTH_PASS}, etc.

@author: Stephan Wenger
@date: 2012-02-29
"""

from weakref import WeakValueDictionary

import glitter.raw as _gl
from glitter.utils import blend_functions, blend_equations, depth_functions, draw_buffers, hints, provoking_vertices, logic_op_modes, provoke_modes, color_read_formats, color_read_types, read_buffers, cull_face_modes, front_face_modes, polygon_modes, InstanceDescriptorMixin, State, StateMixin
from glitter.contexts.contextmanager import ContextManager
from glitter.contexts.proxies import BooleanProxy, FloatProxy, IntegerProxy, Integer64Proxy, EnableDisableProxy, EnumProxy, StringProxy, HintProxy, BindingProxy
from glitter.contexts.textures import TextureUnitList
from glitter.contexts.drawbuffers import DrawBufferList, ColorWritemaskList
from glitter.contexts.multiproxies import BlendFuncProxy, BlendEquationProxy, PolygonOffsetProxy

class GLObjectLibrary(object):
    def __init__(self, _context):
        self._context = _context
        self._objects = WeakValueDictionary()

    def __getitem__(self, key):
        return self._objects[key]

    def __str__(self):
        return str(dict(self._objects))

    def __repr__(self):
        return str(self)

class Context(InstanceDescriptorMixin, StateMixin):
    _frozen = False

    def __init__(self):
        self.texture_units = TextureUnitList(self)
        self.color_writemasks = ColorWritemaskList(self)
        self.draw_buffers = DrawBufferList(self)
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

        self._frozen = True

    def __setattr__(self, name, value):
        if self._frozen and not name.startswith("_") and not hasattr(self, name):
            raise AttributeError("'%s' object has no attribute '%s'" % (self.__class__.__name__, name))
        return super(Context, self).__setattr__(name, value)

    def _bind(self):
        """Make the context active.

        This should be overwritten appropriately by window system dependent subclasses.
        """

        raise NotImplementedError

    def bind(self):
        old_binding = ContextManager.current_context
        ContextManager.current_context = self
        return old_binding

    def __enter__(self):
        ContextManager._stack.append(self.bind())
        return self

    def __exit__(self, type, value, traceback):
        ContextManager.current_context = ContextManager._stack.pop()

    #{ Enums
    blend_functions = blend_functions
    blend_equations = blend_equations
    depth_functions = depth_functions
    draw_buffers = draw_buffers
    hints = hints
    provoking_vertices = provoking_vertices
    logic_op_modes = logic_op_modes
    provoke_modes = provoke_modes
    color_read_formats = color_read_formats
    color_read_types = color_read_types
    read_buffers = read_buffers
    cull_face_modes = cull_face_modes
    front_face_modes = front_face_modes
    polygon_modes = polygon_modes

    #{ Buffer bindings
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

    #{ Miscellaneous bindings
    program_pipeline_binding             = BindingProxy(_gl.glBindProgramPipeline, [                                   ])
    renderbuffer_binding                 = BindingProxy(_gl.glBindRenderbuffer,    [_gl.GL_RENDERBUFFER                ])
    vertex_array_binding                 = BindingProxy(_gl.glBindVertexArray,     [                                   ])
    draw_framebuffer_binding             = BindingProxy(_gl.glBindFramebuffer,     [_gl.GL_DRAW_FRAMEBUFFER            ])
    read_framebuffer_binding             = BindingProxy(_gl.glBindFramebuffer,     [_gl.GL_READ_FRAMEBUFFER            ])
    current_program                      = BindingProxy(_gl.glUseProgram,          [                                   ])
    active_texture                       = BindingProxy(_gl.glActiveTexture,       [                                   ])

    #{ Properties with separate getters but joint setters
    blend_dst_alpha = BlendFuncProxy(_gl.GL_BLEND_DST_ALPHA)
    blend_dst_rgb = BlendFuncProxy(_gl.GL_BLEND_DST_RGB)
    blend_src_alpha = BlendFuncProxy(_gl.GL_BLEND_SRC_ALPHA)
    blend_src_rgb = BlendFuncProxy(_gl.GL_BLEND_SRC_RGB)
    blend_equation_alpha = BlendEquationProxy(_gl.GL_BLEND_EQUATION_ALPHA)
    blend_equation_rgb = BlendEquationProxy(_gl.GL_BLEND_EQUATION_RGB)
    polygon_offset_factor = PolygonOffsetProxy(_gl.GL_POLYGON_OFFSET_FACTOR)
    polygon_offset_units = PolygonOffsetProxy(_gl.GL_POLYGON_OFFSET_UNITS)

    #{ Miscellaneous enumerations
    depth_func = EnumProxy(depth_functions, _gl.GL_DEPTH_FUNC, _gl.glDepthFunc)
    draw_buffer = EnumProxy(draw_buffers, _gl.GL_DRAW_BUFFER, _gl.glDrawBuffer)
    implementation_color_read_format = EnumProxy(color_read_formats, _gl.GL_IMPLEMENTATION_COLOR_READ_FORMAT)
    implementation_color_read_type = EnumProxy(color_read_types, _gl.GL_IMPLEMENTATION_COLOR_READ_TYPE)
    layer_provoking_vertex = EnumProxy(provoking_vertices, _gl.GL_LAYER_PROVOKING_VERTEX)
    logic_op_mode = EnumProxy(logic_op_modes, _gl.GL_LOGIC_OP_MODE, _gl.glLogicOp)
    provoking_vertex = EnumProxy(provoke_modes, _gl.GL_PROVOKING_VERTEX, _gl.glProvokingVertex)
    read_buffer = EnumProxy(read_buffers, _gl.GL_READ_BUFFER, _gl.glReadBuffer)
    viewport_index_provoking_vertex = EnumProxy(provoking_vertices, _gl.GL_VIEWPORT_INDEX_PROVOKING_VERTEX)
    cull_face_mode = EnumProxy(cull_face_modes, _gl.GL_CULL_FACE_MODE, _gl.glCullFace)
    front_face = EnumProxy(front_face_modes, _gl.GL_FRONT_FACE, _gl.glFrontFace)
    polygon_mode = EnumProxy(polygon_modes, _gl.GL_POLYGON_MODE, _gl.glPolygonMode, [_gl.GL_FRONT_AND_BACK])

    #{ Hints
    fragment_shader_derivative_hint = HintProxy(_gl.GL_FRAGMENT_SHADER_DERIVATIVE_HINT)
    line_smooth_hint = HintProxy(_gl.GL_LINE_SMOOTH_HINT)
    polygon_smooth_hint = HintProxy(_gl.GL_POLYGON_SMOOTH_HINT)
    texture_compression_hint = HintProxy(_gl.GL_TEXTURE_COMPRESSION_HINT)

    #{ Enabling and disabling
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

    #{ Boolean values
    color_writemask = BooleanProxy([_gl.GL_COLOR_WRITEMASK], _gl.glColorMask, shape=4)
    depth_writemask = BooleanProxy([_gl.GL_DEPTH_WRITEMASK], _gl.glDepthMask)
    doublebuffer = BooleanProxy([_gl.GL_DOUBLEBUFFER])
    pack_lsb_first = BooleanProxy([_gl.GL_PACK_LSB_FIRST], _gl.glPixelStorei, [_gl.GL_PACK_LSB_FIRST])
    pack_swap_bytes = BooleanProxy([_gl.GL_PACK_SWAP_BYTES], _gl.glPixelStorei, [_gl.GL_PACK_SWAP_BYTES])
    shader_compiler = BooleanProxy([_gl.GL_SHADER_COMPILER])
    stereo = BooleanProxy([_gl.GL_STEREO])
    unpack_lsb_first = BooleanProxy([_gl.GL_UNPACK_LSB_FIRST], _gl.glPixelStorei, [_gl.GL_UNPACK_LSB_FIRST])
    unpack_swap_bytes = BooleanProxy([_gl.GL_UNPACK_SWAP_BYTES], _gl.glPixelStorei, [_gl.GL_UNPACK_SWAP_BYTES])
    
    #{ Float values
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

    #{ Integer values
    major_version = IntegerProxy([_gl.GL_MAJOR_VERSION])
    max_3d_texture_size = IntegerProxy([_gl.GL_MAX_3D_TEXTURE_SIZE])
    max_array_texture_layers = IntegerProxy([_gl.GL_MAX_3D_TEXTURE_SIZE])
    max_clip_distances = IntegerProxy([_gl.GL_MAX_CLIP_DISTANCES])
    max_color_texture_samples = IntegerProxy([_gl.GL_MAX_COLOR_TEXTURE_SAMPLES])
    max_color_attachments = IntegerProxy([_gl.GL_MAX_COLOR_ATTACHMENTS])
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
    viewport = IntegerProxy([_gl.GL_VIEWPORT], _gl.glViewport, shape=4)
    viewport_bounds_range = IntegerProxy([_gl.GL_VIEWPORT_BOUNDS_RANGE], shape=2)
    viewport_subpixel_bits = IntegerProxy([_gl.GL_VIEWPORT_SUBPIXEL_BITS])

    #{ 64-bit integer values
    timestamp = Integer64Proxy([_gl.GL_TIMESTAMP])

    #{ Strings
    vendor = StringProxy(_gl.GL_VENDOR)
    renderer = StringProxy(_gl.GL_RENDERER)
    version = StringProxy(_gl.GL_VERSION)
    shading_language_version = StringProxy(_gl.GL_SHADING_LANGUAGE_VERSION)
    extensions = StringProxy(_gl.GL_EXTENSIONS, _gl.GL_NUM_EXTENSIONS)

    #{ Global actions

    def _perform_gl_clear(self, color=None, depth=None, stencil=None):
        """Call C{glClear} with appropriate arguments.

        @param color: Whether to clear the color buffer, and optionally, to which value.
        @type color: C{bool} or C{numpy.ndarray}.
        @param depth: Whether to clear the depth buffer, and optionally, to which value.
        @type depth: C{bool} or C{numpy.ndarray}.
        @param stencil: Whether to clear the stencil buffer, and optionally, to which value.
        @type stencil: C{bool} or C{numpy.ndarray}.

        If no parameters are given, color, depth and stencil are cleared with
        the current clear values.

        @todo: Wrap the C{glClear} call in C{with State()} to set and reset
        L{color_clear_value}, C{depth_clear_value} and C{stencil_clear_value}
        if these are given as C{numpy} arrays in C{color}, C{depth}, and
        C{stencil}, respectively.
        """

        if color is None and depth is None and stencil is None:
            color = depth = stencil = True
        _gl.glClear(
                (_gl.GL_COLOR_BUFFER_BIT if color else 0) |
                (_gl.GL_DEPTH_BUFFER_BIT if depth else 0) |
                (_gl.GL_STENCIL_BUFFER_BIT if stencil else 0)
                )

    def clear(self, color=None, depth=None, stencil=None):
        """Clear the default framebuffer.

        @param color: Whether to clear the color buffer, and optionally, to which value.
        @type color: C{bool} or C{numpy.ndarray}.
        @param depth: Whether to clear the depth buffer, and optionally, to which value.
        @type depth: C{bool} or C{numpy.ndarray}.
        @param stencil: Whether to clear the stencil buffer, and optionally, to which value.
        @type stencil: C{bool} or C{numpy.ndarray}.

        If no parameters are given, color, depth and stencil are cleared with
        the current clear values.
        """

        with self:
            with State(self, draw_framebuffer_binding=None):
                self._perform_gl_clear(color, depth, stencil)

    def finish(self):
        """Block until all GL execution is complete.

        C{finish} does not return until the effects of all previously called GL
        commands are complete. Such effects include all changes to GL state,
        all changes to connection state, and all changes to the frame buffer
        contents.
        """

        with self:
            _gl.glFinish()

    def flush(self):
        """Force execution of GL commands in finite time.

        Different GL implementations buffer commands in several different
        locations, including network buffers and the graphics accelerator
        itself. C{flush} empties all of these buffers, causing all issued
        commands to be executed as quickly as they are accepted by the actual
        rendering engine. Though this execution may not be completed in any
        particular time period, it does complete in finite time.

        Because any GL program might be executed over a network, or on an
        accelerator that buffers commands, all programs should call C{flush}
        whenever they count on having all of their previously issued commands
        completed. For example, call C{flush} before waiting for user input
        that depends on the generated image.

        C{flush} can return at any time. It does not wait until the execution
        of all previously issued GL commands is complete.
        """

        with self:
            _gl.glFlush()

    def release_shader_compiler(self):
        with self:
            _gl.glReleaseShaderCompiler()

    #}

__all__ = ["Context"]

