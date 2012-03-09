"""Constants and enums.

@todo: Add internal formats GL_DEPTH_COMPONENT and GL_DEPTH_STENCIL to C{texture_formats}.

@author: Stephan Wenger
@date: 2012-02-29
"""

import glitter.raw as _gl
from glitter.utils.dtypes import uint8, uint16, uint32, int8, int16, int32, float32
from glitter.utils.enum import Enum

texture_formats = [
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
        ]
"""Mapping between C{numpy} types and OpenGL types.

First column: C{numpy} datatype, number of color channels
Second column: OpenGL internal format
Third column: OpenGL type, OpenGL format
"""

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

primitive_types = Enum(
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

buffer_dimensions_to_primitive = {1: primitive_types.POINTS, 2: primitive_types.LINES, 3: primitive_types.TRIANGLES}
primitive_to_buffer_dimensions = {primitive_types.POINTS: 1, primitive_types.LINES: 2, primitive_types.TRIANGLES: 3}

blend_functions = Enum(
        ZERO=_gl.GL_ZERO,
        ONE=_gl.GL_ONE,
        SRC_COLOR=_gl.GL_SRC_COLOR,
        ONE_MINUS_SRC_COLOR=_gl.GL_ONE_MINUS_SRC_COLOR,
        DST_COLOR=_gl.GL_DST_COLOR,
        ONE_MINUS_DST_COLOR=_gl.GL_ONE_MINUS_DST_COLOR,
        SRC_ALPHA=_gl.GL_SRC_ALPHA,
        ONE_MINUS_SRC_ALPHA=_gl.GL_ONE_MINUS_SRC_ALPHA,
        DST_ALPHA=_gl.GL_DST_ALPHA,
        ONE_MINUS_DST_ALPHA=_gl.GL_ONE_MINUS_DST_ALPHA,
        CONSTANT_COLOR=_gl.GL_CONSTANT_COLOR,
        ONE_MINUS_CONSTANT_COLOR=_gl.GL_ONE_MINUS_CONSTANT_COLOR,
        CONSTANT_ALPHA=_gl.GL_CONSTANT_ALPHA,
        ONE_MINUS_CONSTANT_ALPHA=_gl.GL_ONE_MINUS_CONSTANT_ALPHA,
        SRC_ALPHA_SATURATE=_gl.GL_SRC_ALPHA_SATURATE,
)

blend_equations = Enum(
        ADD=_gl.GL_FUNC_ADD,
        SUBTRACT=_gl.GL_FUNC_SUBTRACT,
        REVERSE_SUBTRACT=_gl.GL_FUNC_REVERSE_SUBTRACT,
        MIN=_gl.GL_MIN,
        MAX=_gl.GL_MAX,
)

depth_functions = Enum(
        NEVER=_gl.GL_NEVER,
        LESS=_gl.GL_LESS,
        EQUAL=_gl.GL_EQUAL,
        LEQUAL=_gl.GL_LEQUAL,
        GREATER=_gl.GL_GREATER,
        NOTEQUAL=_gl.GL_NOTEQUAL,
        GEQUAL=_gl.GL_GEQUAL,
        ALWAYS=_gl.GL_ALWAYS,
)

draw_buffers = Enum(
        NONE=_gl.GL_NONE,
        FRONT_LEFT=_gl.GL_FRONT_LEFT,
        FRONT_RIGHT=_gl.GL_FRONT_RIGHT,
        BACK_LEFT=_gl.GL_BACK_LEFT,
        BACK_RIGHT=_gl.GL_BACK_RIGHT,
        FRONT=_gl.GL_FRONT,
        BACK=_gl.GL_BACK,
        LEFT=_gl.GL_LEFT,
        RIGHT=_gl.GL_RIGHT,
        FRONT_AND_BACK=_gl.GL_FRONT_AND_BACK,
)
for key, value in _gl.__dict__.items():
    if key.startswith("GL_COLOR_ATTACHMENT"):
        draw_buffers._add(key[3:], value)

hints = Enum(
        FASTEST=_gl.GL_FASTEST,
        NICEST=_gl.GL_NICEST,
        DONT_CARE=_gl.GL_DONT_CARE,
)

provoking_vertices = Enum(
        PROVOKING=_gl.GL_PROVOKING_VERTEX,
        FIRST=_gl.GL_FIRST_VERTEX_CONVENTION,
        LAST=_gl.GL_LAST_VERTEX_CONVENTION,
        UNDEFINED=_gl.GL_UNDEFINED_VERTEX,
)

logic_op_modes = Enum(
        CLEAR=_gl.GL_CLEAR,
        SET=_gl.GL_SET,
        COPY=_gl.GL_COPY,
        COPY_INVERTED=_gl.GL_COPY_INVERTED,
        NOOP=_gl.GL_NOOP,
        INVERT=_gl.GL_INVERT,
        AND=_gl.GL_AND,
        NAND=_gl.GL_NAND,
        OR=_gl.GL_OR,
        NOR=_gl.GL_NOR,
        XOR=_gl.GL_XOR,
        EQUIV=_gl.GL_EQUIV,
        AND_REVERSE=_gl.GL_AND_REVERSE,
        AND_INVERTED=_gl.GL_AND_INVERTED,
        OR_REVERSE=_gl.GL_OR_REVERSE,
        OR_INVERTED=_gl.GL_OR_INVERTED,
)

provoke_modes = Enum(
        FIRST_VERTEX_CONVENTION=_gl.GL_FIRST_VERTEX_CONVENTION,
        LAST_VERTEX_CONVENTION=_gl.GL_LAST_VERTEX_CONVENTION,
)

color_read_formats = Enum(
        STENCIL_INDEX=_gl.GL_STENCIL_INDEX,
        DEPTH_COMPONENT=_gl.GL_DEPTH_COMPONENT,
        DEPTH_STENCIL=_gl.GL_DEPTH_STENCIL,
        RED=_gl.GL_RED,
        GREEN=_gl.GL_GREEN,
        BLUE=_gl.GL_BLUE,
        RGB=_gl.GL_RGB,
        BGR=_gl.GL_BGR,
        RGBA=_gl.GL_RGBA,
        BGRA=_gl.GL_BGRA,
)

color_read_types = Enum(
        UNSIGNED_BYTE=_gl.GL_UNSIGNED_BYTE,
        BYTE=_gl.GL_BYTE,
        UNSIGNED_SHORT=_gl.GL_UNSIGNED_SHORT,
        SHORT=_gl.GL_SHORT,
        UNSIGNED_INT=_gl.GL_UNSIGNED_INT,
        INT=_gl.GL_INT,
        HALF_FLOAT=_gl.GL_HALF_FLOAT,
        FLOAT=_gl.GL_FLOAT,
        UNSIGNED_BYTE_3_3_2=_gl.GL_UNSIGNED_BYTE_3_3_2,
        UNSIGNED_BYTE_2_3_3_REV=_gl.GL_UNSIGNED_BYTE_2_3_3_REV,
        UNSIGNED_SHORT_5_6_5=_gl.GL_UNSIGNED_SHORT_5_6_5,
        UNSIGNED_SHORT_5_6_5_REV=_gl.GL_UNSIGNED_SHORT_5_6_5_REV,
        UNSIGNED_SHORT_4_4_4_4=_gl.GL_UNSIGNED_SHORT_4_4_4_4,
        UNSIGNED_SHORT_4_4_4_4_REV=_gl.GL_UNSIGNED_SHORT_4_4_4_4_REV,
        UNSIGNED_SHORT_5_5_5_1=_gl.GL_UNSIGNED_SHORT_5_5_5_1,
        UNSIGNED_SHORT_1_5_5_5_REV=_gl.GL_UNSIGNED_SHORT_1_5_5_5_REV,
        UNSIGNED_INT_8_8_8_8=_gl.GL_UNSIGNED_INT_8_8_8_8,
        UNSIGNED_INT_8_8_8_8_REV=_gl.GL_UNSIGNED_INT_8_8_8_8_REV,
        UNSIGNED_INT_10_10_10_2=_gl.GL_UNSIGNED_INT_10_10_10_2,
        UNSIGNED_INT_2_10_10_10_REV=_gl.GL_UNSIGNED_INT_2_10_10_10_REV,
        UNSIGNED_INT_24_8=_gl.GL_UNSIGNED_INT_24_8,
        UNSIGNED_INT_10F_11F_11F_REV=_gl.GL_UNSIGNED_INT_10F_11F_11F_REV,
        UNSIGNED_INT_5_9_9_9_REV=_gl.GL_UNSIGNED_INT_5_9_9_9_REV,
        FLOAT_32_UNSIGNED_INT_24_8_REV=_gl.GL_FLOAT_32_UNSIGNED_INT_24_8_REV,
)

read_buffers = Enum(
        NONE=_gl.GL_NONE,
        FRONT_LEFT=_gl.GL_FRONT_LEFT,
        FRONT_RIGHT=_gl.GL_FRONT_RIGHT,
        BACK_LEFT=_gl.GL_BACK_LEFT,
        BACK_RIGHT=_gl.GL_BACK_RIGHT,
        FRONT=_gl.GL_FRONT,
        BACK=_gl.GL_BACK,
        LEFT=_gl.GL_LEFT,
        RIGHT=_gl.GL_RIGHT,
)
for key, value in _gl.__dict__.items():
    if key.startswith("GL_COLOR_ATTACHMENT"):
        read_buffers._add(key[3:], value)

transform_feedback_buffer_modes = Enum(
        SEPARATE_ATTRIBS=_gl.GL_SEPARATE_ATTRIBS,
        INTERLEAVED_ATTRIBS=_gl.GL_INTERLEAVED_ATTRIBS,
)

client_wait_sync_returns = Enum(
        ALREADY_SIGNALED=_gl.GL_ALREADY_SIGNALED,
        TIMEOUT_EXPIRED=_gl.GL_TIMEOUT_EXPIRED,
        CONDITION_SATISFIED=_gl.GL_CONDITION_SATISFIED,
        WAIT_FAILED=_gl.GL_WAIT_FAILED,
)

framebuffer_status = Enum(
    COMPLETE=_gl.GL_FRAMEBUFFER_COMPLETE,
    UNDEFINED=_gl.GL_FRAMEBUFFER_UNDEFINED,
    UNSUPPORTED=_gl.GL_FRAMEBUFFER_UNSUPPORTED,
    INCOMPLETE_ATTACHMENT=_gl.GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT,
    INCOMPLETE_MISSING_ATTACHMENT=_gl.GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT,
    INCOMPLETE_DRAW_BUFFER=_gl.GL_FRAMEBUFFER_INCOMPLETE_DRAW_BUFFER,
    INCOMPLETE_READ_BUFFER=_gl.GL_FRAMEBUFFER_INCOMPLETE_READ_BUFFER,
    INCOMPLETE_MULTISAMPLE=_gl.GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE,
    INCOMPLETE_LAYER_TARGETS=_gl.GL_FRAMEBUFFER_INCOMPLETE_LAYER_TARGETS,
)

cull_face_modes = Enum(
    FRONT=_gl.GL_FRONT,
    BACK=_gl.GL_BACK,
    FRONT_AND_BACK=_gl.GL_FRONT_AND_BACK,
)

front_face_modes = Enum(
    CW=_gl.GL_CW,
    CCW=_gl.GL_CCW,
)

polygon_modes = Enum(
    POINT=_gl.GL_POINT,
    LINE=_gl.GL_LINE,
    FILL=_gl.GL_FILL,
)

__all__ = [
    "texture_formats",
    "dtype_to_gl_iformat",
    "gl_iformat_to_dtype",
    "dtype_to_gl_format",
    "gl_format_to_dtype",
    "gl_iformat_to_gl_type",
    "texture_compare_funcs",
    "texture_compare_modes",
    "texture_min_filters",
    "texture_mag_filters",
    "texture_swizzles",
    "texture_wrapmodes",
    "primitive_types",
    "buffer_usages",
    "buffer_dimensions_to_primitive",
    "primitive_to_buffer_dimensions",
    "blend_functions",
    "blend_equations",
    "depth_functions",
    "draw_buffers",
    "hints",
    "provoking_vertices",
    "logic_op_modes",
    "provoke_modes",
    "color_read_formats",
    "color_read_types",
    "read_buffers",
    "transform_feedback_buffer_modes",
    "client_wait_sync_returns",
    "framebuffer_status",
    "cull_face_modes",
    "front_face_modes",
    "polygon_modes",
]

