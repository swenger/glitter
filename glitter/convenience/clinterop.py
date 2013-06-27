"""Provides interoperability with PyOpenCL (including advanced data structures
such as CL/GL textures and array buffers.

@author: Kai Ruhl
@since: 2013-02"""

import sys
import numpy as np
import pyopencl as cl
mf = cl.mem_flags # @UndefinedVariable

from glitter.raw import gl
from glitter.convenience import grid
from glitter.arrays.arraybuffer import ArrayBuffer
from glitter.textures.texture import Texture2D

# -----------------------------------------------------------------------------

# Whether to be verbose.
flag_clinterop_verbose = False

# -----------------------------------------------------------------------------

def get_gl_context(option="g"):
    """Returns an OpenGL context. Options: g(lut), q(t)"""
    if "g" == option[0]:
        if flag_clinterop_verbose:
            print "Creating GLUT context."
        from glitter.contexts.glut import GlutWindow
        gl_context = GlutWindow(shape=(1, 1), hide=True)
    elif "q" == option[0]:
        if flag_clinterop_verbose:
            print "Creating QT context."
        from glitter.contexts.qt import QtWidget
        from PySide import QtGui
        app = QtGui.QApplication.instance()
        if app is None:
            app = QtGui.QApplication(sys.argv)
        gl_context = QtWidget(None)
        # sys.exit(app.exec_())
    else:
        raise Exception("Unknown option for creating OpenGL context: %s" % option)
    return gl_context


def get_cl_context(gl_context, device_index=None):
    """Creates a CL context, with or without given GL context
    
    A device index can be specified, otherwise all available GPUs share
    the same context."""
    # (1) Get platform and properties.
    if gl_context is not None: # ... with OpenGL interop?
        with gl_context:
            assert cl.have_gl(), "GL interoperability not enabled." # @UndefinedVariable
            from pyopencl.tools import get_gl_sharing_context_properties
            cl_platform = cl.get_platforms()[0] # @UndefinedVariable
            cl_properties = [(cl.context_properties.PLATFORM, cl_platform)] + get_gl_sharing_context_properties() # @UndefinedVariable
    else: # ... or in stand-alone mode, CL context without GL?
        cl_platform = cl.get_platforms()[0]  # @UndefinedVariable
        cl_properties = [(cl.context_properties.PLATFORM, cl_platform)] # @UndefinedVariable
    # (2) Now get the device and the context.
    use_all_devices = device_index is None and gl_context is None # 2 devices does not work with OpenGl.
    cl_devices = cl_platform.get_devices() if use_all_devices else [cl_platform.get_devices()[0 if device_index is None else device_index]]
    cl_context = cl.Context(properties=cl_properties, devices=cl_devices) # @UndefinedVariable
    return cl_context


# -----------------------------------------------------------------------------

def write_cl_texture(cl_context, cl_img, x, y, value, use_gl=None):
    """Takes an OpenCL texture and writes given value at given x/y coordinates.
    Assumes float texture and value.
    
    Coords are not normalized, so they depend on the image size and on which
    mipmap level the CLTexture has been created."""
    cl_source = """
    const sampler_t T_RAW_SAMPLER = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;
    
    __kernel void write(__write_only image2d_t img, uint x, uint y, float v) {
        int2 coord = (int2)(x, y);
        float4 value = (float4)(v, v, v, 1.0);
        write_imagef(img, coord, value);
    }
    """
    # Determine whether OpenGL sharing has been used.
    if use_gl is None:
        from pyopencl.tools import get_gl_sharing_context_properties
        use_gl = get_gl_sharing_context_properties()[0] in cl_context.properties
    # Make queue and program.
    cl_queue = cl.CommandQueue(cl_context) # @UndefinedVariable
    cl_program = cl.Program(cl_context, cl_source).build()
    if True: # usable in loop
        cl_gl_data = [cl_img]
        if use_gl:
            cl.enqueue_acquire_gl_objects(cl_queue, cl_gl_data) # @UndefinedVariable
        cl_args = [cl_img, np.uint32(x), np.uint32(y), np.float32(value)]; assert 4 == len(cl_args)
        cl_program.write(cl_queue, (1, 1), None, *cl_args)
        if use_gl:
            cl.enqueue_release_gl_objects(cl_queue, cl_gl_data) # @UndefinedVariable
        cl_queue.flush()
    cl_queue.finish()


def read_cl_texture(cl_context, cl_img, x, y, use_gl=None):
    """Takes an OpenCL texture and reads a value at given x/y coordinates.
    Assumes float texture and value.
    
    Coords are not normalized, so they depend on the image size and on which
    mipmap level the CLTexture has been created."""
    cl_source = """
    const sampler_t T_RAW_SAMPLER = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;
    
    __kernel void read(__read_only image2d_t img, uint x, uint y, __global float4* buf) {
        int2 coord = (int2)(x, y);
        float4 value = read_imagef(img, T_RAW_SAMPLER, coord);
        buf[0] = value;
    }
    """
    # Determine whether OpenGL sharing has been used.
    if use_gl is None:
        from pyopencl.tools import get_gl_sharing_context_properties
        use_gl = get_gl_sharing_context_properties()[0] in cl_context.properties
    # Make queue and program.
    tmp = np.zeros((1, 4), dtype=np.float32)
    cl_queue = cl.CommandQueue(cl_context) # @UndefinedVariable
    cl_program = cl.Program(cl_context, cl_source).build()
    cl_tmp = cl.Buffer(cl_context, cl.mem_flags.READ_WRITE | cl.mem_flags.COPY_HOST_PTR, hostbuf=tmp)  # @UndefinedVariable
    if True: # usable in loop
        cl_gl_data = [cl_img]
        if use_gl:
            cl.enqueue_acquire_gl_objects(cl_queue, cl_gl_data) # @UndefinedVariable
        cl_args = [cl_img, np.uint32(x), np.uint32(y), cl_tmp]; assert 4 == len(cl_args)
        cl_program.read(cl_queue, (1, 1), None, *cl_args)
        if use_gl:
            cl.enqueue_release_gl_objects(cl_queue, cl_gl_data) # @UndefinedVariable
        cl_queue.flush()
    cl.enqueue_read_buffer(cl_queue, cl_tmp, tmp).wait()
    cl_queue.finish()
    return tmp[0, 0]


def write_cl_buffer(cl_context, cl_buf, x, value, use_gl=None):
    """Takes an OpenCL buffer and writes given value at given x coordinate.
    Assumes float buffer and value."""
    cl_source = """
    __kernel void write(__global float4* buf, uint x, float v) {
        float4 value = (float4)(v, v, v, 1.0);
        buf[x] = value;
    }
    """
    # Determine whether OpenGL sharing has been used.
    if use_gl is None:
        from pyopencl.tools import get_gl_sharing_context_properties
        use_gl = get_gl_sharing_context_properties()[0] in cl_context.properties
    # Make queue and program.
    cl_queue = cl.CommandQueue(cl_context) # @UndefinedVariable
    cl_program = cl.Program(cl_context, cl_source).build()
    if True: # usable in loop
        cl_gl_data = [cl_buf]
        if use_gl:
            cl.enqueue_acquire_gl_objects(cl_queue, cl_gl_data) # @UndefinedVariable
        cl_args = [cl_buf, np.uint32(x), np.float32(value)]; assert 3 == len(cl_args)
        cl_program.write(cl_queue, (1, 1), None, *cl_args)
        if use_gl:
            cl.enqueue_release_gl_objects(cl_queue, cl_gl_data) # @UndefinedVariable
        cl_queue.flush()
    cl_queue.finish()


def read_cl_buffer(cl_context, cl_buf, x, use_gl=None):
    """Takes an OpenCL buffer and reads a value at given x coordinate.
    Assumes float buffer and value."""
    cl_source = """
    __kernel void read(__global float4* buf, uint x, __global float4* tmp) {
        float4 value = buf[x];
        tmp[0] = value;
    }
    """
    # Determine whether OpenGL sharing has been used.
    if use_gl is None:
        from pyopencl.tools import get_gl_sharing_context_properties
        use_gl = get_gl_sharing_context_properties()[0] in cl_context.properties
    # Make queue and program.
    tmp = np.zeros((1, 4), dtype=np.float32)
    cl_queue = cl.CommandQueue(cl_context) # @UndefinedVariable
    cl_program = cl.Program(cl_context, cl_source).build()
    cl_tmp = cl.Buffer(cl_context, cl.mem_flags.READ_WRITE | cl.mem_flags.COPY_HOST_PTR, hostbuf=tmp)  # @UndefinedVariable
    if True: # usable in loop
        cl_gl_data = [cl_buf]
        if use_gl:
            cl.enqueue_acquire_gl_objects(cl_queue, cl_gl_data) # @UndefinedVariable
        cl_args = [cl_buf, np.uint32(x), cl_tmp]; assert 3 == len(cl_args)
        cl_program.read(cl_queue, (1, 1), None, *cl_args)
        if use_gl:
            cl.enqueue_release_gl_objects(cl_queue, cl_gl_data) # @UndefinedVariable
        cl_queue.flush()
    cl.enqueue_read_buffer(cl_queue, cl_tmp, tmp).wait()
    cl_queue.finish()
    return tmp[0, 0]


# -----------------------------------------------------------------------------

class GLCLAbstractMipmap(object):
    """A mipmapped texture/buffer/something that holds or simulates an
    image pyramid, with OpenGL and OpenCL accessor objects."""

    def reset(self):
        """Resets all data to the original status."""
        raise NotImplementedError("Has not implemented reset().")

    def set_level(self, level, upsample_if_oneup=True):
        """Sets the active level. Mostly applicable for the CL objects,
        but may also be pertinent to the GL objects.
        
        Upsampling may be called if a level-up occurs."""
        raise NotImplementedError("Has not implemented set_level().")

    def get_level(self):
        """Returns the active level."""
        raise NotImplementedError("Has not implemented get_level().")

    def get_shape(self, level=None):
        """Returns the shape at given level, where 0 is the highest,
        full resolution level."""
        raise NotImplementedError("Has not implemented get_shape().")

    def set_data(self, data, level=None):
        """Sets the data with a 2D numpy array (4 channels), optionally at
        a given level of the image pyramid.
        The level may be ignored if not applicable."""
        raise NotImplementedError("Has not implemented set_data().")

    def get_data(self, level=None):
        """Returns the data as 2D numpy array (4 channels), optionally at
        a given level of the image pyramid.
        The level may be ignored if not applicable."""
        raise NotImplementedError("Has not implemented get_data().")

    def get_gl_object(self):
        """Returns the GL texture/buffer/object at current level."""
        raise NotImplementedError("Has not implemented get_gl_object().")

    def get_cl_object(self, rw="rw"):
        """Returns the CL texture/buffer/object at current level,
        optionally with read or write access only (applicable e.g. to
        CL textures)."""
        raise NotImplementedError("Has not implemented get_cl_object().")

    @property
    def gl(self):
        """Returns the GL object at current level."""
        return self.get_gl_object()

    @property
    def cl(self):
        """Returns the CL object at current level."""
        return self.get_cl_object()

    def release(self):
        """Releases all GPU memory."""
        raise NotImplementedError("Has not implemented get_cl_object().")


# -----------------------------------------------------------------------------

class GLCLMipmapTexture(GLCLAbstractMipmap):
    """A mipmapped GL texture with CL representatives for a given pyramid
    level where 0 is the full resolution.
    
    Warning: Works only with float32 data!"""

    _cl_upsample_mipmap_source = """
    const sampler_t T_RAW_SAMPLER = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;

    __kernel void upsample_mipmap(
                                  __read_only  image2d_t img1x,
                                  __write_only image2d_t img2x,
                                  uint wid, uint hei) {
        unsigned int row = get_global_id(0);
        unsigned int col = get_global_id(1);
        int2 coord_r = (int2) (min(col / 2, wid / 2 - 1), min(row / 2, hei / 2 -1 ));
        int2 coord_w = (int2) (col, row);
        float4 value = read_imagef(img1x, T_RAW_SAMPLER, coord_r);
        write_imagef(img2x, coord_w, value);
    }
    """

    def __init__(self, gl_context, cl_context, data, level=0, cl_access="rw", cl_queue=None):
        self.gl_context = gl_context
        self.cl_context = cl_context
        self.cl_queue = cl_queue # May be none, only needed for upsampling.
        self.shape = data.shape[:2]
        self.pixel_count = np.multiply(*self.shape)
        # Keep original data.
        self.initial_data = data
        self.initial_level = level
        # Create GL data.
        self.gl_texture = Texture2D(data, mipmap=True, context=self.gl_context);
        self.annotate_texture(self.gl_texture, mipmap=True)
        # Get GL/CL shapes per level.
        self.gl_shapes = []
        for i in range(1000):
            lvl_shape = self.gl_texture.get_shape(i)[:2]
            if lvl_shape[0] < 8:
                break
            self.gl_shapes.append(lvl_shape)
        # Determine whether CL write/read access is required.
        self.cl_access = cl_access
        self.is_cl_read = "r" in cl_access
        self.is_cl_writ = "w" in cl_access
        # Create CL data.
        self.level = self.cl_prev_level = level
        self.cl_texture_read = cl.GLTexture(self.cl_context, mf.READ_ONLY, gl.GL_TEXTURE_2D, level, self.gl_texture._id, 2) if self.is_cl_read else None # @UndefinedVariable
        self.cl_texture_writ = cl.GLTexture(self.cl_context, mf.WRITE_ONLY, gl.GL_TEXTURE_2D, level, self.gl_texture._id, 2) if self.is_cl_writ else None # @UndefinedVariable
        # Create CL programs (for upsampling).
        assert self.cl_context is not None, "Need CL context to compile upsampler."
        self._cl_upsample_mipmap_program = cl.Program(self.cl_context, self._cl_upsample_mipmap_source).build()

    def reset(self):
        """Resets all data to the original status.
        For textures, data is not deleted."""
        self.level = self.cl_prev_level = self.initial_level
        self._clear_cl_textures()
        self.cl_texture_read = cl.GLTexture(self.cl_context, mf.READ_ONLY, gl.GL_TEXTURE_2D, self.level, self.gl_texture._id, 2) if self.is_cl_read else None # @UndefinedVariable
        self.cl_texture_writ = cl.GLTexture(self.cl_context, mf.WRITE_ONLY, gl.GL_TEXTURE_2D, self.level, self.gl_texture._id, 2) if self.is_cl_writ else None # @UndefinedVariable

    def annotate_texture(self, gl_texture, mipmap=False):
        """Annotates a texture with standard information."""
        from glitter.utils.constants import texture_min_filters, texture_mag_filters, texture_wrapmodes
        gl_texture.min_filter = texture_min_filters.NEAREST_MIPMAP_NEAREST if mipmap else texture_min_filters.NEAREST # @UndefinedVariable
        gl_texture.mag_filter = texture_mag_filters.NEAREST # @UndefinedVariable
        gl_texture.wrap_s = texture_wrapmodes.CLAMP_TO_EDGE # @UndefinedVariable
        gl_texture.wrap_t = texture_wrapmodes.CLAMP_TO_EDGE # @UndefinedVariable

    def set_level(self, level, upsample_if_oneup=True):
        """Sets an OpenCL access level. If it is a classic upsample ("one up!"),
        then the content of the previous layers is upsampled too."""
        if level == self.level:
            return
        prev_level = self.level
        next_level = self.level = level
        next_shape = self.cl_shape = self.gl_texture.get_shape(next_level)[:2]
        upsampling_required = next_level == prev_level - 1 and upsample_if_oneup
        # (1) Create new buffers.
        if upsampling_required:
            next_texture_read = cl.GLTexture(self.cl_context, mf.READ_ONLY, gl.GL_TEXTURE_2D, next_level, self.gl_texture._id, 2) if self.is_cl_read else None # @UndefinedVariable
            next_texture_writ = cl.GLTexture(self.cl_context, mf.WRITE_ONLY, gl.GL_TEXTURE_2D, next_level, self.gl_texture._id, 2) if self.is_cl_writ else None # @UndefinedVariable
        # (2) Upsample if necessary.
        if upsampling_required:
            prev_texture_read = self.cl_texture_read
            prev_texture_miss = prev_texture_read is None
            next_texture_miss = next_texture_writ is None
            # (2.1) Create temporary CL textures if missing.
            if prev_texture_miss:
                prev_texture_read = cl.GLTexture(self.cl_context, mf.READ_ONLY, gl.GL_TEXTURE_2D, prev_level, self.gl_texture._id, 2) # @UndefinedVariable
            if next_texture_miss:
                next_texture_writ = cl.GLTexture(self.cl_context, mf.WRITE_ONLY, gl.GL_TEXTURE_2D, next_level, self.gl_texture._id, 2) # @UndefinedVariable
            # (2.2) Actually upsample.
            self._upsample_mipmap(prev_texture_read, next_texture_writ, *next_shape[::-1])
            # (2.3) Remove temporary CL textures.
            if prev_texture_miss:
                prev_texture_read.release(); prev_texture_read = None
            if next_texture_miss:
                next_texture_writ.release(); next_texture_writ = None
        # (3) Clear old stuff.
        self._clear_cl_textures()
        # (4) Set new stuff.
        if not upsampling_required: # (otherwise, this has been done above)
            next_texture_read = cl.GLTexture(self.cl_context, mf.READ_ONLY, gl.GL_TEXTURE_2D, next_level, self.gl_texture._id, 2) if self.is_cl_read else None # @UndefinedVariable
            next_texture_writ = cl.GLTexture(self.cl_context, mf.WRITE_ONLY, gl.GL_TEXTURE_2D, next_level, self.gl_texture._id, 2) if self.is_cl_writ else None # @UndefinedVariable
        self.cl_texture_read = next_texture_read
        self.cl_texture_writ = next_texture_writ

    def get_level(self):
        """Indicates the current level that the CL textures are on."""
        return self.level

    def get_shape(self, level=None):
        """Returns the shape at given level, where 0 is the highest,
        full resolution level."""
        if level is None:
            level = self.level
        return self.gl_shapes[level]

    def _clear_cl_textures(self):
        """Removes all CL references on the textures."""
        if self.cl_texture_read is not None:
            self.cl_texture_read.release()
            self.cl_texture_read = None
        if self.cl_texture_writ is not None:
            self.cl_texture_writ.release()
            self.cl_texture_writ = None

    def _upsample_mipmap(self, cl_img_r_1x, cl_img_w_2x, wid, hei):
        """Upsamples given 1x size (read) mipmap texture into 2x size (write)
        mipmap texture. Given width and height are for the target texture."""
        assert cl_img_r_1x is not None, "Must have (prev) image to upsample (read access)."
        assert cl_img_w_2x is not None, "Must have (next) image to upsample (write access)."
        # (1) Get a queue to start program.
        if self.cl_queue is None:
            self.cl_queue = cl.CommandQueue(self.cl_context) # @UndefinedVariable
        assert self.cl_queue is not None, "Must have CL queue to call upsampling."
        # (2) Lock and fire.
        cl_gl_data = [cl_img_r_1x, cl_img_w_2x]
        cl.enqueue_acquire_gl_objects(self.cl_queue, cl_gl_data) # @UndefinedVariable
        cl_args = cl_gl_data + [np.uint32(wid), np.uint32(hei)]; assert 4 == len(cl_args)
        cl_grid = (hei, wid)
        self._cl_upsample_mipmap_program.upsample_mipmap(self.cl_queue, cl_grid, None, *cl_args)
        cl.enqueue_release_gl_objects(self.cl_queue, cl_gl_data) # @UndefinedVariable
        # (3) Finish.
        self.cl_queue.flush()
        self.cl_queue.finish()

    def set_data(self, data, level=None):
        """Sets a new image as texture data. The GL level is always 0,
        and the given level denotes the CL level.
        
        All CL textures will be deleted and recreated. The GL texture stays
        the same.
        
        The new CL access level is either the given on or the last used one,
        when None is given."""
        if level is None:
            level = self.level # only for CL, GL level is always 0.
        assert 3 == len(data.shape), "Expected 2D, 4-channel image, but is: %s" % (str(data.shape))
        self._clear_cl_textures()
        self.gl_texture.set_data(data, mipmap=True); self.annotate_texture(self.gl_texture, mipmap=True)
        self.cl_texture_read = cl.GLTexture(self.cl_context, mf.READ_ONLY, gl.GL_TEXTURE_2D, level, self.gl_texture._id, 2) if self.is_cl_read else None # @UndefinedVariable
        self.cl_texture_writ = cl.GLTexture(self.cl_context, mf.WRITE_ONLY, gl.GL_TEXTURE_2D, level, self.gl_texture._id, 2) if self.is_cl_writ else None # @UndefinedVariable
        # Reset data and levels.
        self.initial_data = data
        self.initial_level = level
        self.level = self.cl_prev_level = level
        self.shape = data.shape[:2]
        self.pixel_count = np.multiply(*self.shape)
        # Get GL/CL shapes per level.
        self.gl_shapes = []
        for i in range(1000):
            lvl_shape = self.gl_texture.get_shape(i)[:2]
            if lvl_shape[0] < 8:
                break
            self.gl_shapes.append(lvl_shape)

    def get_data(self, level=None):
        """Returns the data at active or at given level."""
        if level is None:
            level = self.level
        return self.gl_texture.get_data(level)

    def get_gl_object(self):
        """Returns the GL texture, all mipmap levels in one."""
        return self.gl_texture

    def get_cl_object(self, rw="r"):
        """Returns the CL texture (either "r" or "w") of the current level."""
        if not rw in ["r", "w"]:
            raise Exception("Only r/w options for CL texture access, you requested '%s'" % (rw))
        cl_texture = self.cl_texture_read if "r" == rw else self.cl_texture_writ
        if cl_texture is None:
            raise Exception("No \"%s\" CL texture with previously defined CL access mode \"%s\"." % (rw, self.cl_access))
        return cl_texture

    def release(self):
        """Releases all GPU memory."""
        self._clear_cl_textures()
        self.gl_texture = None


# -----------------------------------------------------------------------------

class GLCLMipmapBuffer(GLCLAbstractMipmap):
    """A GL array buffer (aka VBO) with a CL representative, simulating an
    image pyramid. Usable only for 2D float images with 4 channels.
    
    Internally, the data is 1D with 4 channels. Conversion methods are provided.
    Upsampling methods for a simulated mipmap are also provided.
    
    Warning: Works only with float32 data!"""

    # Upsampling variant 1: As many threads as smaller image.
    _cl_upsample_buffer_source_1x = """
    __kernel void upsample_buffer(
                                  __global float4* img1x,
                                  __global float4* img2x,
                                  uint wid1x, uint hei1x,
                                  uint wid2x, uint hei2x) {
        uint pos_r = get_global_id(0);
        if (pos_r >= wid1x * hei1x) {
            return;
        }
        uint row = pos_r / wid1x;
        uint col = pos_r % wid1x;
        float4 value = img1x[pos_r];
        for (int i = 0; i < 3; i++) { // rows
            if (i == 2 && (row * 2 + i) != hei2x - 1) { // only at extended border.
                continue;
            }
            for (int j = 0; j < 3; j++) { // cols
                if (j == 2 && (col * 2 + j) != wid2x - 1) { // only at extended border.
                    continue;
                }
                uint pos_w = (row * 2 + i) * wid2x + (col * 2 + j);
                if (row * 2 + i < hei2x && col * 2 + j < wid2x && pos_w < wid2x * hei2x) {
                    img2x[pos_w] = value;
                }
            }
        }
    }
    """

    # Upsampling variant 2: As many threads as larger image.
    # Seems to be slightly faster than variant 1, on a 2K->4K image.
    _cl_upsample_buffer_source_2x = """
    __kernel void upsample_buffer(
                                  __global float4* img1x,
                                  __global float4* img2x,
                                  uint wid1x, uint hei1x,
                                  uint wid2x, uint hei2x) {
        uint pos_w = get_global_id(0);
        uint row_w = pos_w / wid2x;
        uint col_w = pos_w % wid2x;
        uint pos_r = min(row_w / 2, hei1x - 1) * wid1x + min(col_w / 2, wid1x - 1);
        if (pos_r < wid1x * hei1x && pos_w < wid2x * hei2x) {
            float4 value = img1x[pos_r];
            img2x[pos_w] = value;
        }
    }
    """

    def __init__(self, gl_context, cl_context, max_shape, data, level, cl_queue=None):
        self.gl_context = gl_context
        self.cl_context = cl_context
        self.cl_queue = cl_queue # May be none, only needed for upsampling.
        assert 3 == len(data.shape), "Assumed shape is hei x wid x 4, but was %s" % (str(data.shape))
        assert data.dtype == np.float32, "Assumed float32 data, but is: %s" % (str(data.dtype))
        self.level = level # assumed level of that buffer.
        self.shape = data.shape[:2] # shape is 2D, even if buffer data shape is 1D.
        self.pixel_count = np.multiply(*self.shape)
        # Set initial level separately so it can be restored later on.
        self.initial_level = level
        self.initial_data = data
        # Get GL/CL shapes per level.
        assert 2 == len(max_shape) or 4 == max_shape[2], "Maximum shape should be 2D (hei x wid) or 3D with 4 channels (hei x wid x 4), but is: %s" % (str(max_shape))
        self.max_shape = max_shape[:2]
        self.gl_shapes = []
        lvl_shape = self.max_shape
        while lvl_shape[0] >= 8:
            self.gl_shapes.append(lvl_shape)
            lvl_shape = (lvl_shape[0] / 2, lvl_shape[1] / 2) # is rounded down, just like mipmap.
        # Create GL and CL data.
        data1D = np.ascontiguousarray(data.reshape(-1, 4))
        assert (self.pixel_count, 4) == data1D.shape, "Buffer array should be %s, but is: %s" % (str((self.pixel_count, 4)), str(data1D.shape))
        self.gl_buffer = ArrayBuffer(data=data1D, usage="DYNAMIC_DRAW", context=self.gl_context);
        self.cl_buffer = cl.GLBuffer(self.cl_context, mf.READ_WRITE, self.gl_buffer._id) # @UndefinedVariable
        # Create CL programs (for upsampling).
        assert self.cl_context is not None, "Need CL context to compile."
        self._cl_upsample_variant = 2 # 1 = smaller image, 2 = larger image, 3 = cpu only.
        self._cl_upsample_buffer_program = cl.Program(self.cl_context, self._cl_upsample_buffer_source_1x if 1 == self._cl_upsample_variant else self._cl_upsample_buffer_source_2x).build()

    def reset(self):
        """Resets all data to the original status."""
        self.level = -1
        self.set_level(self.initial_level, upsample_if_oneup=False)

    def _upsample_buffer(self, cl_buf_1x, cl_buf_2x, wid_1x, hei_1x, wid_2x, hei_2x):
        """Upsamples given 1x size buffer into 2x size buffer. Since ratio
        might not be exactly 2x, old and new sizes must be given."""
        assert cl_buf_1x is not None, "Must have (prev) buffer to upsample."
        assert cl_buf_2x is not None, "Must have (next) buffer to upsample."
        # (1) Get a queue to start program.
        if self.cl_queue is None:
            self.cl_queue = cl.CommandQueue(self.cl_context) # @UndefinedVariable
        assert self.cl_queue is not None, "Must have CL queue to call upsampling."
        # (2) Lock and fire.
        cl_gl_data = [cl_buf_1x, cl_buf_2x]
        cl.enqueue_acquire_gl_objects(self.cl_queue, cl_gl_data) # @UndefinedVariable
        cl_args = cl_gl_data + [np.uint32(wid_1x), np.uint32(hei_1x), np.uint32(wid_2x), np.uint32(hei_2x)]; assert 6 == len(cl_args)
        cl_grid = (hei_1x * wid_1x,) if 1 == self._cl_upsample_variant else (hei_2x * wid_2x,)
        self._cl_upsample_buffer_program.upsample_buffer(self.cl_queue, cl_grid, None, *cl_args)
        cl.enqueue_release_gl_objects(self.cl_queue, cl_gl_data) # @UndefinedVariable
        # (3) Finish.
        self.cl_queue.flush()
        self.cl_queue.finish()

    def upsample_to_new(self, new_shape, level):
        """Upsamples the current buffer to given new shape (should be 2x the
        current shape, +1 pixel max).
        
        Takes around .15 seconds on a 2K->4K frame upsampling."""
        assert level == self.level - 1, "Level should be 1 less than current level (%d), but is: %d" % (self.level, level)
        assert 2 == len(new_shape), "Shape should be hei x wid, but is: %s" % (str(new_shape))
        assert 2 == new_shape[1] / self.shape[1], "New width (%d) should be 2x old width (%d)" % (new_shape[1], self.shape[1])
        assert 2 == new_shape[0] / self.shape[0], "New height (%d) should be 2x old height (%d)" % (new_shape[0], self.shape[0])
        # Rather on the CPU? Takes a bit longer, but is more GPU-mem efficient.
        if 3 == self._cl_upsample_variant:
            return self._upsample_to_new_cpu(new_shape, level)
        # Ok, so on the GPU.
        next_data = np.zeros(new_shape + (4,), dtype=np.float32)
        next_data1D = np.ascontiguousarray(next_data.reshape(-1, 4))
        pixel_count = np.multiply(*new_shape[:2])
        assert (pixel_count, 4) == next_data1D.shape, "Buffer array should be %s, but is: %s" % (str((pixel_count, 4)), str(next_data1D.shape))
        next_gl_buffer = ArrayBuffer(data=next_data1D, usage="DYNAMIC_DRAW", context=self.gl_context);
        next_cl_buffer = cl.GLBuffer(self.cl_context, mf.READ_WRITE, next_gl_buffer._id) # @UndefinedVariable
        wid_1x, hei_1x = self.shape[::-1]
        wid_2x, hei_2x = new_shape[::-1]
        assert wid_2x * hei_2x == np.multiply(*new_shape), "Should be %d pixels, but are: %d" % (wid_2x * hei_2x, np.multiply(new_shape[:2]))
        self._upsample_buffer(self.cl_buffer, next_cl_buffer, wid_1x, hei_1x, wid_2x, hei_2x)
        self.cl_buffer.release()
        self.cl_buffer = next_cl_buffer;
        self.gl_buffer = next_gl_buffer;
        self.level = level
        self.shape = new_shape
        self.pixel_count = np.multiply(*self.shape)

    def _upsample_to_new_cpu(self, new_shape, level):
        """Upsamples the current buffer to given new shape (should be 2x the
        current shape, +1 pixel max).
        
        Takes around .25 seconds on a 2K->4K frame upsampling."""
        assert level == self.level - 1, "Level should be 1 less than current level (%d), but is: %d" % (self.level, level)
        assert 2 == len(new_shape), "Shape should be hei x wid, but is: %s" % (str(new_shape))
        assert 2 == new_shape[1] / self.shape[1], "New width (%d) should be 2x old width (%d)" % (new_shape[1], self.shape[1])
        assert 2 == new_shape[0] / self.shape[0], "New height (%d) should be 2x old height (%d)" % (new_shape[0], self.shape[0])
        buf_1x = self.gl_buffer.get_data()
        shape_1x = self.shape + (4,)
        shape_2x = new_shape + (4,)
        # (1) Upsample core 2x area.
        ihei, iwid = np.array(shape_1x[:2]) * 2 # internal new size (exactly 2x, borders may be missing)
        prev_buf = buf_1x.reshape(shape_1x)
        next_buf = np.zeros(shape_2x, dtype=np.float32)
        next_buf[0:0 + ihei:2, 0:0 + iwid:2] = prev_buf; next_buf[1:1 + ihei:2, 0:0 + iwid:2] = prev_buf
        next_buf[1:1 + ihei:2, 1:1 + iwid:2] = prev_buf; next_buf[0:0 + ihei:2, 1:1 + iwid:2] = prev_buf
        # (2) Now do the +1 borders.
        if shape_2x[0] > 2 * shape_1x[0]: # height border
            next_buf[-1] = next_buf[-2]
        if shape_2x[1] > 2 * shape_1x[1]: # width border
            next_buf[:, -1] = next_buf[:, -2]
        # (3) Put new buffer into 1D shape.
        next_data1D = np.ascontiguousarray(next_buf.reshape(-1, 4))
        pixel_count = np.multiply(*new_shape[:2])
        assert (pixel_count, 4) == next_data1D.shape, "Buffer array should be %s, but is: %s" % (str((pixel_count, 4)), str(next_data1D.shape))
        # (4) Finally, re-create the buffers.
        self.cl_buffer.release()
        self.gl_buffer.set_data(next_data1D)
        self.cl_buffer = cl.GLBuffer(self.cl_context, mf.READ_WRITE, self.gl_buffer._id) # @UndefinedVariable
        self.level = level
        self.shape = new_shape
        self.pixel_count = np.multiply(*self.shape)

    def set_level(self, level, upsample_if_oneup=True):
        """Sets the active level. Mostly applicable for the CL objects,
        but may also be pertinent to the GL objects.
        
        Upsampling may be called if a level-up occurs."""
        if level == self.level:
            return
        new_shape = self.gl_shapes[level]
        if level == self.level - 1 and upsample_if_oneup:
            self.upsample_to_new(new_shape, level)
        elif level == self.initial_level:
            self.set_data(self.initial_data, level) # set_data() expects 2D data.
        else:
            self.set_data(np.zeros(new_shape + (4,), dtype=np.float32), level) # set_data() expects 2D data.
        # Remembering the next level is done in upsample() or set_data().

    def get_level(self):
        """Indicates the current level that the CL textures are on."""
        return self.level

    def get_shape(self, level=None):
        """Returns the shape at given level, where 0 is the highest,
        full resolution level."""
        if level is None:
            level = self.level
        return self.gl_shapes[level]

    def set_data(self, data, level=None):
        """Sets a new image as buffer data. All CL buffers will be deleted
        and recreated. The GL buffer stays the same.
        
        Data shape is assumed to be a 2D image with 4 channels."""
        if level is None:
            level = self.level
        assert 3 == len(data.shape), "Expected 2D, 4-channel image, but is: %s" % (str(data.shape))
        new_shape = data.shape[:2]
        assert new_shape == self.gl_shapes[level], "Level %d should be %s, but given data is: %s" % (level, str(self.gl_shapes[level]), str(new_shape))
        data1D = np.ascontiguousarray(data.reshape(-1, 4))
        pixel_count = np.multiply(*new_shape)
        assert (pixel_count, 4) == data1D.shape, "Buffer array should be %s, but is: %s" % (str((pixel_count, 4)), str(data1D.shape))
        self.cl_buffer.release()
        self.gl_buffer.set_data(data1D)
        self.cl_buffer = cl.GLBuffer(self.cl_context, mf.READ_WRITE, self.gl_buffer._id) # @UndefinedVariable
        self.level = level
        self.shape = new_shape
        self.pixel_count = np.multiply(*self.shape)

    def get_data(self, level=None):
        """Returns the data in image format, i.e. hei x wid x 4.
        The level parameter is ignored, possible is only the current level."""
        if level is not None and level != self.level:
            raise Exception("Can only get data from current level %d, but you wanted level %d") % (self.level, level)
        return self.gl_buffer.get_data().reshape(self.shape + (4,))

    def get_gl_object(self):
        """Returns the GL buffer."""
        return self.gl_buffer

    def get_cl_object(self):
        """Returns the CL buffer."""
        return self.cl_buffer

    def get_pos(self, x, y, out_of_bounds_exception=True):
        """Given an x and y coordinate, returns the position within the 1D
        array buffer."""
        wid = self.shape[1]
        pos = y * wid + x;
        if out_of_bounds_exception and pos >= np.multiply(*self.shape):
            raise Exception("Position %d (from coords x:%d, y:%d) exceeds image shape (%dx%d)" % (pos, x, y, self.shape[1], self.shape[0]))
        return pos

    def get_coord(self, pos, out_of_bounds_exception=True):
        """Given a 1D position returns the (x, y) coordinate."""
        wid = self.shape[1]
        x, y = pos % wid, pos / wid
        if out_of_bounds_exception and pos >= np.multiply(*self.shape):
            raise Exception("Position %d (equal to coords x:%d, y:%d) exceeds image shape (%dx%d)" % (pos, x, y, self.shape[1], self.shape[0]))
        return (x, y)

    def get_grid_pixels(self, normalize=False):
        """Returns a grid of pixel coordinates that fits to the current shape.
        Every pixel position in the range 0,0..wid,hei exists exactly once
        in the grid.
        
        The returned result has the shape (wid*hei, 2).
        If normalization is requested, the coords are from 0..1 instead of
        0..width, same for height.
        
        The result is immediately usable in an OpenGL VAO."""
        hei, wid = self.shape
        return grid.get_pixel_index_grid(wid, hei, ndim=2, normalize=normalize).reshape(-1, 2)

    def get_grid_triangle_indices(self):
        """Returns a grid of triangles that fits to the current shape.
        Each pixel in the range 0,0..wid,hei exists at least once on a corner
        point of a triangle.
        
        The returned result has the shape (wid*hei, 3).
        The result is immediately usable in an OpenGL VAO."""
        hei, wid = self.shape
        return grid.get_triangle_index_grid(wid, hei).reshape(-1, 3)

    def get_grid_point_indices(self):
        """Returns a grid of points that fits the current shape.
        Each pixel in the range 0,0..wid,hei exists exactly once as a point.
        
        The returned result has the shape (wid*hei, 1).
        The result is immediately usable in an OpenGL VAO."""
        hei, wid = self.shape
        return np.arange(wid * hei).reshape(-1, 1)

    def release(self):
        """Releases all GPU memory."""
        self.cl_buffer.release();
        self.cl_buffer = None
        self.gl_buffer = None


# -----------------------------------------------------------------------------

class GLCLOnemapBuffer(GLCLAbstractMipmap):
    """A GL array buffer (aka VBO) with a CL representative, simulating an
    image pyramid. Usable only for 2D float images with 4 channels.
    
    Unlike the GLCLMipmapBuffer, the one-map buffer has only the highest
    resolution as internal data, and lower resolutions stored at interleaved
    positions. This requires careful addressing of all clients
    
    Like the GLCLMipmapBuffer, the data is 1D with 4 channels.
    Warning: Works only with float32 data!"""

    _cl_upsample_buffer_source = """
    __kernel void upsample_buffer(
                                  __global float4* img,
                                  uint wid1x, uint hei1x,
                                  uint wid2x, uint hei2x,
                                  uint fwid, uint fhei) {
        uint row = get_global_id(0);
        uint col = get_global_id(1);
        if (row * col >= wid1x * hei1x) {
            return;
        }
        uint lea_r = fwid / wid1x; // rounded down.
        uint lea_w = fwid / wid2x; // rounded down.
        uint pos_r = (row * lea_r) * fwid + (col * lea_r);
        float4 value = img[pos_r];
        for (int i = 0; i < 3; i++) { // rows
            uint row_w = (row * 2 + i);
            if (i == 2 && row_w != hei2x - 1) { // only at extended border.
                continue;
            }
            for (int j = 0; j < 3; j++) { // cols
                uint col_w = (col * 2 + j);
                if (j == 2 && col_w != wid2x - 1) { // only at extended border.
                    continue;
                }
                uint pos_w = row_w * lea_w * fwid + col_w * lea_w;
                if (pos_w < fwid * fhei) {
                    img[pos_w] = value;
                }
            }
        }
    }
    """

    _cl_reset_to_zero_source = """
        __kernel void reset_to_zero(__global float4* img) {
            int idx = get_global_id(0);
            img[idx] = (float4)(0,0,0,0);
        }
    """

    def __init__(self, gl_context, cl_context, max_shape, data, level, cl_queue=None):
        self.gl_context = gl_context
        self.cl_context = cl_context
        self.cl_queue = cl_queue # May be none, only needed for upsampling.
        self.use_gl = self.gl_context is not None
        assert 3 == len(data.shape), "Assumed shape is hei x wid x 4, but was %s" % (str(data.shape))
        assert data.dtype == np.float32, "Assumed float32 data, but is: %s" % (str(data.dtype))
        self.level = level # assumed level of that buffer.
        self.shape = data.shape[:2] # shape is 2D, even if buffer data shape is 1D.
        self.pixel_count = np.multiply(*self.shape)
        # Set initial level separately so it can be restored later on.
        self.initial_level = level
        self.initial_data = data
        # Get GL/CL shapes per level.
        assert 2 == len(max_shape) or 4 == max_shape[2], "Maximum shape should be 2D (hei x wid) or 3D with 4 channels (hei x wid x 4), but is: %s" % (str(max_shape))
        self.max_shape = max_shape[:2]
        self.gl_shapes = []
        lvl_shape = self.max_shape
        while lvl_shape[0] >= 8:
            self.gl_shapes.append(lvl_shape)
            lvl_shape = (lvl_shape[0] / 2, lvl_shape[1] / 2) # is rounded down, just like mipmap.
        # Create GL and CL data.
        self.interleave = lea = max_shape[1] / self.shape[1] # is rounded down.
        self.real_data = np.zeros(self.max_shape + (4,), dtype=np.float32)
        self.real_data[:self.shape[0] * lea:lea, :self.shape[1] * lea:lea, :] = data
        data1D = np.ascontiguousarray(self.real_data.reshape(-1, 4))
        if self.use_gl:
            self.gl_buffer = ArrayBuffer(data=data1D, usage="DYNAMIC_DRAW", context=self.gl_context);
            self.cl_buffer = cl.GLBuffer(self.cl_context, mf.READ_WRITE, self.gl_buffer._id) # @UndefinedVariable
        else:
            self.gl_buffer = None
            self.cl_buffer = cl.Buffer(self.cl_context, mf.READ_WRITE | mf.COPY_HOST_PTR, hostbuf=data1D) # @UndefinedVariable
        # Create CL programs (for upsampling).
        assert self.cl_context is not None, "Need CL context to compile."
        self._cl_upsample_buffer_program = cl.Program(self.cl_context, self._cl_upsample_buffer_source).build()
        self._cl_reset_to_zero_program = cl.Program(self.cl_context, self._cl_reset_to_zero_source).build()


    def reset(self):
        """Resets all data to the original status."""
        self.level = -1
        self.set_level(self.initial_level, upsample_if_oneup=False)

    def reset_to_zero(self):
        """Resets all values in the entire buffer to zero, without changing
        the actual level."""
        cl_grid = (self.shape[1] * self.shape[0],)
        if self.cl_queue is None:
            self.cl_queue = cl.CommandQueue(self.cl_context) # @UndefinedVariable
        cl_gl_data = [self.cl_buffer]
        if self.use_gl:
            cl.enqueue_acquire_gl_objects(self.cl_queue, cl_gl_data) # @UndefinedVariable
        self._cl_reset_to_zero_program.reset_to_zero(self.cl_queue, cl_grid, None, *cl_gl_data)
        if self.use_gl:
            cl.enqueue_release_gl_objects(self.cl_queue, cl_gl_data) # @UndefinedVariable
        self.cl_queue.flush()
        self.cl_queue.finish()

    def _upsample_buffer(self, cl_buf, wid_1x, hei_1x, wid_2x, hei_2x, wid_max, hei_max):
        """Upsamples given 1x content into 2x content, using the same buffer
        (where the data is stored interleaved).
        Since ratio might not be exactly 2x, old and new sizes must be given."""
        assert cl_buf is not None, "Must have buffer to upsample."
        # (1) Get a queue to start program.
        if self.cl_queue is None:
            self.cl_queue = cl.CommandQueue(self.cl_context) # @UndefinedVariable
        assert self.cl_queue is not None, "Must have CL queue to call upsampling."
        # (2) Lock and fire.
        cl_gl_data = [cl_buf]
        if self.use_gl:
            cl.enqueue_acquire_gl_objects(self.cl_queue, cl_gl_data) # @UndefinedVariable
        cl_args = cl_gl_data + [np.uint32(wid_1x), np.uint32(hei_1x), np.uint32(wid_2x), np.uint32(hei_2x), np.uint32(wid_max), np.uint32(hei_max)]; assert 7 == len(cl_args)
        cl_grid = (hei_1x, wid_1x)
        self._cl_upsample_buffer_program.upsample_buffer(self.cl_queue, cl_grid, None, *cl_args)
        if self.use_gl:
            cl.enqueue_release_gl_objects(self.cl_queue, cl_gl_data) # @UndefinedVariable
        # (3) Finish.
        self.cl_queue.flush()
        self.cl_queue.finish()

    def upsample_to_new(self, new_shape, level):
        """Upsamples the current buffer to given new shape (should be 2x the
        current shape, +1 pixel max).
        
        Takes around .15 seconds on a 2K->4K frame upsampling."""
        assert level == self.level - 1, "Level should be 1 less than current level (%d), but is: %d" % (self.level, level)
        assert 2 == len(new_shape), "Shape should be hei x wid, but is: %s" % (str(new_shape))
        assert 2 == new_shape[1] / self.shape[1], "New width (%d) should be 2x old width (%d)" % (new_shape[1], self.shape[1])
        assert 2 == new_shape[0] / self.shape[0], "New height (%d) should be 2x old height (%d)" % (new_shape[0], self.shape[0])
        wid_1x, hei_1x = self.shape[::-1]
        wid_2x, hei_2x = new_shape[::-1]
        wid_max, hei_max = self.max_shape[::-1]
        self._upsample_buffer(self.cl_buffer, wid_1x, hei_1x, wid_2x, hei_2x, wid_max, hei_max)
        self.level = level
        self.shape = new_shape
        self.pixel_count = np.multiply(*self.shape)
        self.interleave = self.max_shape[1] / new_shape[1] # rounded down.

    def set_level(self, level, upsample_if_oneup=True):
        """Sets the active level. Mostly applicable for the CL objects,
        but may also be pertinent to the GL objects.
        
        Upsampling may be called if a level-up occurs."""
        if level == self.level:
            return
        new_shape = self.gl_shapes[level]
        if level == self.level - 1 and upsample_if_oneup:
            self.upsample_to_new(new_shape, level)
        elif level == self.initial_level:
            self.set_data(self.initial_data, level) # set_data() expects 2D data.
        else:
            self.set_data(np.zeros(new_shape + (4,), dtype=np.float32), level) # set_data() expects 2D data.
        # Remembering the level is done in upsample() or set_data().

    def get_level(self):
        """Indicates the current level that the CL textures are on."""
        return self.level

    def get_shape(self, level=None):
        """Returns the shape at given level, where 0 is the highest,
        full resolution level."""
        if level is None:
            level = self.level
        return self.gl_shapes[level]

    def _set_max_data(self, max_data):
        """Internal. Sets the entire data array."""
        data1D = np.ascontiguousarray(max_data.reshape(-1, 4))
        if self.cl_queue is None:
            self.cl_queue = cl.CommandQueue(self.cl_context) # @UndefinedVariable
        if self.use_gl:
            # self.cl_buffer.release()
            # self.gl_buffer.set_data(data1D)
            # self.cl_buffer = cl.GLBuffer(self.cl_context, mf.READ_WRITE, self.gl_buffer._id) # @UndefinedVariable
            cl_gl_data = [self.cl_buffer]
            if self.use_gl:
                cl.enqueue_acquire_gl_objects(self.cl_queue, cl_gl_data) # @UndefinedVariable
            cl.enqueue_copy(self.cl_queue, self.cl_buffer, data1D)
            if self.use_gl:
                cl.enqueue_release_gl_objects(self.cl_queue, cl_gl_data) # @UndefinedVariable
        else:
            cl.enqueue_copy(self.cl_queue, self.cl_buffer, data1D)
            self.cl_queue.flush()
            self.cl_queue.finish()

    def _get_max_data(self):
        """Internal. Returns the entire data array, already reshaped to 2D."""
        if self.use_gl:
            max_data = self.gl_buffer.get_data()
        else:
            if self.cl_queue is None:
                self.cl_queue = cl.CommandQueue(self.cl_context) # @UndefinedVariable
            max_data = np.zeros_like(self.real_data.reshape(-1, 4))
            cl.enqueue_copy(self.cl_queue, max_data, self.cl_buffer)
            self.cl_queue.flush()
            self.cl_queue.finish()
        return max_data.reshape(self.max_shape + (4,))

    def set_data(self, data, level=None):
        """Sets a new image as buffer data. All CL buffers will be deleted
        and recreated. The GL buffer stays the same.
        
        Data shape is assumed to be a 2D image with 4 channels."""
        if level is None:
            level = self.level
        assert 3 == len(data.shape), "Expected 2D, 4-channel image, but is: %s" % (str(data.shape))
        new_shape = data.shape[:2]
        assert new_shape == self.gl_shapes[level], "Level %d should be %s, but given data is: %s" % (level, str(self.gl_shapes[level]), str(new_shape))
        lea = self.max_shape[1] / new_shape[1] # rounded down.
        # Create zeros in full shape and fill with data.
        max_data = self._get_max_data()
        max_data[:new_shape[0] * lea:lea, :new_shape[1] * lea:lea, :] = data
        self._set_max_data(max_data)
        self.level = level
        self.shape = new_shape
        self.pixel_count = np.multiply(*self.shape)
        self.interleave = lea

    def get_data(self, level=None):
        """Returns the data in image format, i.e. hei x wid x 4."""
        if level is None:
            level = self.level
        max_data = self._get_max_data()
        assert 3 == max_data.ndim, "Should be 2D, 4-channel shape, but is: %s" % (str(max_data.shape))
        shape = self.gl_shapes[level]
        lea = self.max_shape[1] / shape[1]
        data = max_data[::lea, ::lea, :][:shape[0], :shape[1], :]
        assert shape == data.shape[:2], "GLCL buffer data on level %d should be %s, but is %s" % (self.level, str(self.shape), str(data.shape[:2]))
        return data

    def get_gl_object(self):
        """Returns the GL buffer."""
        return self.gl_buffer

    def get_cl_object(self):
        """Returns the CL buffer."""
        return self.cl_buffer

    def get_pos(self, x, y, out_of_bounds_exception=True):
        """Given an x and y coordinate, returns the position within the 1D
        array buffer (at the current level)."""
        wid, lea = self.max_shape[1], self.interleave
        pos = (y * lea) * wid + (x * lea);
        if out_of_bounds_exception and pos >= np.multiply(*self.max_shape):
            raise Exception("Position %d (from coords x:%d, y:%d) exceeds image shape (%dx%d)" % (pos, x, y, self.shape[1], self.shape[0]))
        return pos

    def get_coord(self, pos, out_of_bounds_exception=True):
        """Given a 1D position returns the (x, y) coordinate
         (at the current level)."""
        wid, lea = self.max_shape[1], self.interleave
        x, y = (pos % (wid * lea)) / lea, (pos / (wid * lea)) / lea
        if out_of_bounds_exception and not (0 <= x < self.shape[1] and 0 <= y < self.shape[0]):
            raise Exception("Position %d (equal to coords x:%d, y:%d) exceeds image shape (%dx%d)" % (pos, x, y, self.shape[1], self.shape[0]))
        return (x, y)

    def get_data_pos(self, x, y, level=None):
        """Given an x and y coordinate, returns the internal 2D position within
        the array buffer data.
        
        If you call get_data(0) instead of the currnt level, and want its
        content at some arbitrary level, call this method.
        Switch of x/y to row/col order is also here."""
        if level is None:
            level = self.level
        lea = self.max_shape[1] / self.gl_shapes[level][1]
        return y * lea, x * lea

    def get_grid_pixels(self, normalize=False):
        """Returns a grid of pixel coordinates that fits to the maximum shape.
        Every pixel position in the range 0,0..wid,hei exists exactly once
        in the grid.
        
        The returned result has the shape (max_wid*max_hei, 2).
        If normalization is requested, the coords are from 0..1 instead of
        0..width, same for height.
        
        The result is immediately usable in an OpenGL VAO.
        Elements/indices are responsible for omitting pixels not available
        in the current resolution."""
        hei, wid = self.max_shape
        return grid.get_pixel_index_grid(wid, hei, ndim=2, normalize=normalize).reshape(-1, 2)

    def get_grid_triangle_indices(self):
        """Returns a grid of triangles that fits to the current shape.
        Each pixel in the range 0,0..wid,hei exists at least once on a corner
        point of a triangle.
        
        The returned result has the shape (wid*hei, 3).
        The result is immediately usable in an OpenGL VAO."""
        fhei, fwid = self.max_shape
        mhei, mwid = self.shape
        lea = fwid / mwid # rounded down, same as self.interleave
        max_points2d = np.arange(fwid * fhei).reshape(fhei, fwid)
        lvl_points2d = max_points2d[:mhei * lea:lea, :mwid * lea:lea]
        xy = lvl_points2d[:-1, :-1] # omit -1 so we can do +1 below.
        I = np.dstack((xy, xy + lea, xy + (fwid * lea), xy + lea, xy + (fwid * lea) + lea, xy + (fwid * lea)))
        I = I.reshape(mhei - 1, (mwid - 1) * 2, 3) # triangles
        return I.reshape(-1, 3)

    def get_grid_point_indices(self):
        """Returns a grid of points that fits the current shape.
        Each pixel in the range 0,0..wid,hei exists exactly once as a point.
        
        The returned result has the shape (wid*hei, 1).
        The result is immediately usable in an OpenGL VAO."""
        fhei, fwid = self.max_shape
        mhei, mwid = self.shape
        lea = fwid / mwid # rounded down, same as self.interleave
        max_points2d = np.arange(fwid * fhei).reshape(fhei, fwid)
        lvl_points2d = max_points2d[:mhei * lea:lea, :mwid * lea:lea]
        return lvl_points2d.reshape(-1, 1)

    def release(self):
        """Releases all GPU memory."""
        self.cl_buffer.release();
        self.cl_buffer = None
        self.gl_buffer = None
