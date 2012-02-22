from rawgl import gl as _gl

from dtypes import uint8, uint16, uint32, int8, int16, int32, float32
from util import Enum

texture_formats = [ # (_np dtype, number of color channels), OpenGL internal format, (OpenGL type, OpenGL format)
        ((uint8,   1), _gl.GL_R8UI,     (_gl.GL_UNSIGNED_BYTE,  _gl.GL_RED_INTEGER )),
        ((int8,    1), _gl.GL_R8I,      (_gl.GL_BYTE,           _gl.GL_RED_INTEGER )),
        ((uint16,  1), _gl.GL_R16UI,    (_gl.GL_UNSIGNED_SHORT, _gl.GL_RED_INTEGER )),
        ((int16,   1), _gl.GL_R16I,     (_gl.GL_SHORT,          _gl.GL_RED_INTEGER )),
        ((uint32,  1), _gl.GL_R32UI,    (_gl.GL_UNSIGNED_INT,   _gl.GL_RED_INTEGER )),
        ((int32,   1), _gl.GL_R32I,     (_gl.GL_INT,            _gl.GL_RED_INTEGER )),
        ((float32, 1), _gl.GL_R32F,     (_gl.GL_FLOAT,          _gl.GL_RED         )),
        ((uint8,   2), _gl.GL_RG8UI,    (_gl.GL_UNSIGNED_BYTE,  _gl.GL_RG_INTEGER  )),
        ((int8,    2), _gl.GL_RG8I,     (_gl.GL_BYTE,           _gl.GL_RG_INTEGER  )),
        ((uint16,  2), _gl.GL_RG16UI,   (_gl.GL_UNSIGNED_SHORT, _gl.GL_RG_INTEGER  )),
        ((int16,   2), _gl.GL_RG16I,    (_gl.GL_SHORT,          _gl.GL_RG_INTEGER  )),
        ((uint32,  2), _gl.GL_RG32UI,   (_gl.GL_UNSIGNED_INT,   _gl.GL_RG_INTEGER  )),
        ((int32,   2), _gl.GL_RG32I,    (_gl.GL_INT,            _gl.GL_RG_INTEGER  )),
        ((float32, 2), _gl.GL_RG32F,    (_gl.GL_FLOAT,          _gl.GL_RG          )),
        ((uint8,   3), _gl.GL_RGB8UI,   (_gl.GL_UNSIGNED_BYTE,  _gl.GL_RGB_INTEGER )),
        ((int8,    3), _gl.GL_RGB8I,    (_gl.GL_BYTE,           _gl.GL_RGB_INTEGER )),
        ((uint16,  3), _gl.GL_RGB16UI,  (_gl.GL_UNSIGNED_SHORT, _gl.GL_RGB_INTEGER )),
        ((int16,   3), _gl.GL_RGB16I,   (_gl.GL_SHORT,          _gl.GL_RGB_INTEGER )),
        ((uint32,  3), _gl.GL_RGB32UI,  (_gl.GL_UNSIGNED_INT,   _gl.GL_RGB_INTEGER )),
        ((int32,   3), _gl.GL_RGB32I,   (_gl.GL_INT,            _gl.GL_RGB_INTEGER )),
        ((float32, 3), _gl.GL_RGB32F,   (_gl.GL_FLOAT,          _gl.GL_RGB         )),
        ((uint8,   4), _gl.GL_RGBA8UI,  (_gl.GL_UNSIGNED_BYTE,  _gl.GL_RGBA_INTEGER)),
        ((int8,    4), _gl.GL_RGBA8I,   (_gl.GL_BYTE,           _gl.GL_RGBA_INTEGER)),
        ((uint16,  4), _gl.GL_RGBA16UI, (_gl.GL_UNSIGNED_SHORT, _gl.GL_RGBA_INTEGER)),
        ((int16,   4), _gl.GL_RGBA16I,  (_gl.GL_SHORT,          _gl.GL_RGBA_INTEGER)),
        ((uint32,  4), _gl.GL_RGBA32UI, (_gl.GL_UNSIGNED_INT,   _gl.GL_RGBA_INTEGER)),
        ((int32,   4), _gl.GL_RGBA32I,  (_gl.GL_INT,            _gl.GL_RGBA_INTEGER)),
        ((float32, 4), _gl.GL_RGBA32F,  (_gl.GL_FLOAT,          _gl.GL_RGBA        )),
        # TODO add internal formats GL_DEPTH_COMPONENT and GL_DEPTH_STENCIL
        ]
dtype_to_gl_iformat =   dict((x[0],    x[1]   ) for x in texture_formats)
gl_iformat_to_dtype =   dict((x[1],    x[0]   ) for x in texture_formats)
dtype_to_gl_format =    dict((x[0],    x[2][1]) for x in texture_formats)
gl_format_to_dtype =    dict((x[2][1], x[0]   ) for x in texture_formats)
gl_iformat_to_gl_type = dict((x[1],    x[2][0]) for x in texture_formats)

texture_compare_funcs = Enum(
        LEQUAL=_gl.GL_LEQUAL,
        GEQUAL=_gl.GL_GEQUAL,
        LESS=_gl.GL_LESS,
        GREATER=_gl.GL_GREATER,
        EQUAL=_gl.GL_EQUAL,
        NOTEQUAL=_gl.GL_NOTEQUAL,
        ALWAYS=_gl.GL_ALWAYS,
        NEVER=_gl.GL_NEVER,
        )

texture_compare_modes = Enum(
        COMPARE_REF_TO_TEXTURE=_gl.GL_COMPARE_REF_TO_TEXTURE,
        NONE=_gl.GL_NONE,
        )

texture_min_filters = Enum(
        NEAREST=_gl.GL_NEAREST,
        LINEAR=_gl.GL_LINEAR,
        NEAREST_MIPMAP_NEAREST=_gl.GL_NEAREST_MIPMAP_NEAREST,
        LINEAR_MIPMAP_NEAREST=_gl.GL_LINEAR_MIPMAP_NEAREST,
        NEAREST_MIPMAP_LINEAR=_gl.GL_NEAREST_MIPMAP_LINEAR,
        LINEAR_MIPMAP_LINEAR=_gl.GL_LINEAR_MIPMAP_LINEAR,
        )

texture_mag_filters = Enum(
        NEAREST=_gl.GL_NEAREST,
        LINEAR=_gl.GL_LINEAR,
        )

texture_swizzles = Enum(
        RED=_gl.GL_RED,
        GREEN=_gl.GL_GREEN,
        BLUE=_gl.GL_BLUE,
        ALPHA=_gl.GL_ALPHA,
        ZERO=_gl.GL_ZERO,
        ONE=_gl.GL_ONE,
        )

texture_wrapmodes = Enum(
        CLAMP_TO_EDGE=_gl.GL_CLAMP_TO_EDGE,
        CLAMP_TO_BORDER=_gl.GL_CLAMP_TO_BORDER,
        MIRRORED_REPEAT=_gl.GL_MIRRORED_REPEAT,
        REPEAT=_gl.GL_REPEAT,
        )

buffer_targets = [ # target, binding
        (_gl.GL_ARRAY_BUFFER,              _gl.GL_ARRAY_BUFFER_BINDING             ),
        (_gl.GL_ATOMIC_COUNTER_BUFFER,     _gl.GL_ATOMIC_COUNTER_BUFFER_BINDING    ),
        (_gl.GL_COPY_READ_BUFFER,          None                                    ), # XXX why is there no GL_COPY_READ_BUFFER_BINDING?
        (_gl.GL_COPY_WRITE_BUFFER,         None                                    ), # XXX why is there no GL_COPY_WRITE_BUFFER_BINING?
        (_gl.GL_DRAW_INDIRECT_BUFFER,      _gl.GL_DRAW_INDIRECT_BUFFER_BINDING     ),
        (_gl.GL_ELEMENT_ARRAY_BUFFER,      _gl.GL_ELEMENT_ARRAY_BUFFER_BINDING     ),
        (_gl.GL_PIXEL_PACK_BUFFER,         _gl.GL_PIXEL_PACK_BUFFER_BINDING        ),
        (_gl.GL_PIXEL_UNPACK_BUFFER,       _gl.GL_PIXEL_UNPACK_BUFFER_BINDING      ),
        (_gl.GL_TEXTURE_BUFFER,            None                                    ), # TODO use glGetTexLevelParameter with GL_TEXTURE_BUFFER_DATA_STORE_BINDING
        (_gl.GL_TRANSFORM_FEEDBACK_BUFFER, _gl.GL_TRANSFORM_FEEDBACK_BUFFER_BINDING),
        (_gl.GL_UNIFORM_BUFFER,            _gl.GL_UNIFORM_BUFFER_BINDING           ),
        ]
buffer_target_to_binding = dict((x[0], x[1]) for x in buffer_targets)

buffer_drawmodes = Enum(
        POINTS=_gl.GL_POINTS,
        LINE_STRIP=_gl.GL_LINE_STRIP,
        LINE_LOOP=_gl.GL_LINE_LOOP,
        LINES=_gl.GL_LINES,
        LINE_STRIP_ADJACENCY=_gl.GL_LINE_STRIP_ADJACENCY,
        LINES_ADJACENCY=_gl.GL_LINES_ADJACENCY,
        TRIANGLE_STRIP=_gl.GL_TRIANGLE_STRIP,
        TRIANGLE_FAN=_gl.GL_TRIANGLE_FAN,
        TRIANGLES=_gl.GL_TRIANGLES,
        TRIANGLE_STRIP_ADJACENCY=_gl.GL_TRIANGLE_STRIP_ADJACENCY,
        TRIANGLES_ADJACENCY=_gl.GL_TRIANGLES_ADJACENCY,
        PATCHES=_gl.GL_PATCHES,
        )

buffer_usages = Enum(
        STREAM_DRAW=_gl.GL_STREAM_DRAW,
        STREAM_READ=_gl.GL_STREAM_READ,
        STREAM_COPY=_gl.GL_STREAM_COPY,
        STATIC_DRAW=_gl.GL_STATIC_DRAW,
        STATIC_READ=_gl.GL_STATIC_READ,
        STATIC_COPY=_gl.GL_STATIC_COPY,
        DYNAMIC_DRAW=_gl.GL_DYNAMIC_DRAW,
        DYNAMIC_READ=_gl.GL_DYNAMIC_READ,
        DYNAMIC_COPY=_gl.GL_DYNAMIC_COPY,
        )

buffer_dimensions_to_primitive = {1: _gl.GL_POINTS, 2: _gl.GL_LINES, 3: _gl.GL_TRIANGLES}

framebuffer_attachment_names = Enum(
        DEPTH=_gl.GL_DEPTH_ATTACHMENT,
        STENCIL=_gl.GL_STENCIL_ATTACHMENT,
        DEPTH_STENCIL=_gl.GL_DEPTH_STENCIL_ATTACHMENT,
)

framebuffer_targets = [
        (_gl.GL_FRAMEBUFFER,      _gl.GL_FRAMEBUFFER_BINDING),
        (_gl.GL_DRAW_FRAMEBUFFER, None                      ), # XXX why is there no GL_DRAW_FRAMEBUFFER_BINDING?
        (_gl.GL_READ_FRAMEBUFFER, None                      ), # XXX why is there no GL_READ_FRAMEBUFFER_BINDING?
]
framebuffer_target_to_binding = dict((x[0], x[1]) for x in framebuffer_targets)

