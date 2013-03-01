"""Provides interoperability with PyOpenCL (including advanced data structures
such as CL/GL textures and array buffers.

@author: Kai Ruhl
@since: 2013-02"""

import sys
import numpy as np
import pyopencl as cl
mf = cl.mem_flags # @UndefinedVariable

from glitter.raw import gl
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


def get_cl_context(gl_context):
    """Creates a CL context, with or without given GL context."""
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
    cl_devices = [cl_platform.get_devices()[-1]]  # Only one is allowed!
    cl_context = cl.Context(properties=cl_properties, devices=cl_devices) # @UndefinedVariable
    return cl_context


# -----------------------------------------------------------------------------

def write_cl_texture(cl_context, cl_img, x, y, value):
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
    cl_queue = cl.CommandQueue(cl_context) # @UndefinedVariable
    cl_program = cl.Program(cl_context, cl_source).build()
    if True: # usable in loop
        cl_gl_data = [cl_img]
        cl.enqueue_acquire_gl_objects(cl_queue, cl_gl_data) # @UndefinedVariable
        cl_args = [cl_img, np.uint32(x), np.uint32(y), np.float32(value)]; assert 4 == len(cl_args)
        cl_program.write(cl_queue, (1, 1), None, *cl_args)
        cl.enqueue_release_gl_objects(cl_queue, cl_gl_data) # @UndefinedVariable
        cl_queue.flush()
    cl_queue.finish()


def read_cl_texture(cl_context, cl_img, x, y):
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
    tmp = np.zeros((1, 4), dtype=np.float32)
    cl_queue = cl.CommandQueue(cl_context) # @UndefinedVariable
    cl_program = cl.Program(cl_context, cl_source).build()
    cl_tmp = cl.Buffer(cl_context, cl.mem_flags.READ_WRITE | cl.mem_flags.COPY_HOST_PTR, hostbuf=tmp)  # @UndefinedVariable
    if True: # usable in loop
        cl_gl_data = [cl_img]
        cl.enqueue_acquire_gl_objects(cl_queue, cl_gl_data) # @UndefinedVariable
        cl_args = [cl_img, np.uint32(x), np.uint32(y), cl_tmp]; assert 4 == len(cl_args)
        cl_program.read(cl_queue, (1, 1), None, *cl_args)
        cl.enqueue_release_gl_objects(cl_queue, cl_gl_data) # @UndefinedVariable
        cl_queue.flush()
    cl.enqueue_read_buffer(cl_queue, cl_tmp, tmp).wait()
    cl_queue.finish()
    return tmp[0, 0]


def write_cl_buffer(cl_context, cl_buf, x, value):
    """Takes an OpenCL buffer and writes given value at given x coordinate.
    Assumes float buffer and value."""
    cl_source = """
    __kernel void write(__global float4* buf, uint x, float v) {
        float4 value = (float4)(v, v, v, 1.0);
        buf[x] = value;
    }
    """
    cl_queue = cl.CommandQueue(cl_context) # @UndefinedVariable
    cl_program = cl.Program(cl_context, cl_source).build()
    if True: # usable in loop
        cl_gl_data = [cl_buf]
        cl.enqueue_acquire_gl_objects(cl_queue, cl_gl_data) # @UndefinedVariable
        cl_args = [cl_buf, np.uint32(x), np.float32(value)]; assert 3 == len(cl_args)
        cl_program.write(cl_queue, (1, 1), None, *cl_args)
        cl.enqueue_release_gl_objects(cl_queue, cl_gl_data) # @UndefinedVariable
        cl_queue.flush()
    cl_queue.finish()


def read_cl_buffer(cl_context, cl_buf, x):
    """Takes an OpenCL buffer and reads a value at given x coordinate.
    Assumes float buffer and value."""
    cl_source = """
    __kernel void read(__global float4* buf, uint x, __global float4* tmp) {
        float4 value = buf[x];
        tmp[0] = value;
    }
    """
    tmp = np.zeros((1, 4), dtype=np.float32)
    cl_queue = cl.CommandQueue(cl_context) # @UndefinedVariable
    cl_program = cl.Program(cl_context, cl_source).build()
    cl_tmp = cl.Buffer(cl_context, cl.mem_flags.READ_WRITE | cl.mem_flags.COPY_HOST_PTR, hostbuf=tmp)  # @UndefinedVariable
    if True: # usable in loop
        cl_gl_data = [cl_buf]
        cl.enqueue_acquire_gl_objects(cl_queue, cl_gl_data) # @UndefinedVariable
        cl_args = [cl_buf, np.uint32(x), cl_tmp]; assert 3 == len(cl_args)
        cl_program.read(cl_queue, (1, 1), None, *cl_args)
        cl.enqueue_release_gl_objects(cl_queue, cl_gl_data) # @UndefinedVariable
        cl_queue.flush()
    cl.enqueue_read_buffer(cl_queue, cl_tmp, tmp).wait()
    cl_queue.finish()
    return tmp[0, 0]


# -----------------------------------------------------------------------------

def annotate_texture(gl_texture, mipmap=False):
    """Annotates a texture with standard information."""
    from glitter.utils.constants import texture_min_filters, texture_mag_filters, texture_wrapmodes
    gl_texture.min_filter = texture_min_filters.NEAREST_MIPMAP_NEAREST if mipmap else texture_min_filters.NEAREST # @UndefinedVariable
    gl_texture.mag_filter = texture_mag_filters.NEAREST # @UndefinedVariable
    gl_texture.wrap_s = texture_wrapmodes.CLAMP_TO_EDGE # @UndefinedVariable
    gl_texture.wrap_t = texture_wrapmodes.CLAMP_TO_EDGE # @UndefinedVariable


# -----------------------------------------------------------------------------

class GLCLMipmapTexture(object):
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
        int2 coord_r = (int2) (col / 2, row / 2);
        int2 coord_w = (int2) (col, row);
        float4 value = read_imagef(img1x, T_RAW_SAMPLER, coord_r);
        write_imagef(img2x, coord_w, value);
    }
    """

    def __init__(self, gl_context, cl_context, data, cl_level=0, cl_access="rw", cl_queue=None):
        self.gl_context = gl_context
        self.cl_context = cl_context
        self.cl_queue = cl_queue # May be none, only needed for upsampling.
        self.shape = data.shape
        # Create GL data.
        self.gl_texture = Texture2D(data, mipmap=True, context=self.gl_context);
        annotate_texture(self.gl_texture, mipmap=True)
        # Determine whether CL write/read access is required.
        self.cl_access = cl_access
        self.is_cl_read = "r" in cl_access
        self.is_cl_writ = "w" in cl_access
        # Create CL data.
        self.cl_level = self.cl_prev_level = cl_level
        self.cl_texture_read = None
        self.cl_texture_writ = None
        self.set_cl_level(cl_level)
        # Create CL programs (for upsampling).
        assert self.cl_context is not None, "Need CL context to compile upsampler."
        self._cl_upsample_mipmap_program = cl.Program(self.cl_context, self._cl_upsample_mipmap_source).build()

    def set_cl_level(self, cl_level, upsample_if_oneup=True):
        """Sets an OpenCL access level. If it is a classic upsample ("one up!"),
        then the content of the previous layers is upsampled too."""
        prev_level = self.cl_level
        next_level = self.cl_level = cl_level
        next_shape = self.cl_shape = self.gl_texture.get_shape(next_level)[:2]
        # (1) Create new buffers.
        next_texture_read = cl.GLTexture(self.cl_context, mf.READ_ONLY, gl.GL_TEXTURE_2D, next_level, self.gl_texture._id, 2) if self.is_cl_read else None # @UndefinedVariable
        next_texture_writ = cl.GLTexture(self.cl_context, mf.WRITE_ONLY, gl.GL_TEXTURE_2D, next_level, self.gl_texture._id, 2) if self.is_cl_writ else None # @UndefinedVariable
        # (2) Upsample if necessary.
        if next_level == prev_level - 1 and upsample_if_oneup:
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
        self.cl_texture_read = next_texture_read
        self.cl_texture_writ = next_texture_writ

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
        self._cl_upsample_mipmap_program.upsample_mipmap(self.cl_queue, (hei, wid), None, *cl_args)
        cl.enqueue_release_gl_objects(self.cl_queue, cl_gl_data) # @UndefinedVariable
        # (3) Finish.
        self.cl_queue.flush()
        self.cl_queue.finish()

    def set_data(self, data, cl_level=None):
        """Sets a new image as texture data. All CL textures will be deleted
        and recreated. The GL texture stays the same.
        
        The new CL access level is either the given on or the last used one,
        when None is given."""
        if cl_level is None:
            cl_level = self.cl_level
        self._clear_cl_textures()
        self.gl_texture.set_data(data, mipmap=True); annotate_texture(self.gl_texture, mipmap=True)
        self.cl_texture_read = cl.GLTexture(self.cl_context, mf.READ_ONLY, gl.GL_TEXTURE_2D, cl_level, self.gl_texture._id, 2) if self.is_cl_read else None # @UndefinedVariable
        self.cl_texture_writ = cl.GLTexture(self.cl_context, mf.WRITE_ONLY, gl.GL_TEXTURE_2D, cl_level, self.gl_texture._id, 2) if self.is_cl_read else None # @UndefinedVariable
        self.shape = data.shape

    def get_data(self, level=0):
        """Returns the data at given level."""
        return self.gl_texture.get_data(level)

    def get_cl_level(self):
        """Indicates the current level that the CL textures are on."""
        return self.cl_level

    def get_gl_texture(self):
        """Returns the GL texture, all mipmap levels in one."""
        return self.gl_texture

    def get_cl_texture(self, rw="r"):
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

class GLCLMipmapBuffer(object):
    """A GL array buffer (aka VBO) with a CL representative, simulating an
    image pyramid. Usable only for 2D float images with 4 channels.
    
    Internally, the data is 1D with 4 channels. Conversion methods are provided.
    Upsampling methods for a simulated mipmap are also provided.
    
    Warning: Works only with float32 data!"""

    _cl_upsample_buffer_source = """
    __kernel void upsample_buffer(
                                  __global float4* img1x,
                                  __global float4* img2x,
                                  uint wid1x, uint hei1x,
                                  uint wid2x, uint hei2x) {
        uint pos_w = get_global_id(0);
        uint row = pos_w / wid2x;
        uint col = pos_w % wid2x;
        uint pos_r = (row / 2) * wid1x + (col / 2);
        if (pos_r < wid1x * hei1x && pos_w < wid2x * hei2x) {
            float4 value = img1x[pos_r];
            img2x[pos_w] = value;
        }
    }
    """

    def __init__(self, gl_context, cl_context, data, level, cl_queue=None):
        self.gl_context = gl_context
        self.cl_context = cl_context
        self.cl_queue = cl_queue # May be none, only needed for upsampling.
        assert 3 == len(data.shape), "Assumed shape is hei x wid x 4, but was %s" % (str(data.shape))
        assert data.dtype == np.float32, "Assumed float32 data, but is: %s" % (str(data.dtype))
        self.level = level # assumed level of that buffer.
        self.shape = data.shape[:2] # shape is 2D, even if buffer data shape is 1D.
        # Create GL and CL data.
        data1D = np.ascontiguousarray(data.reshape(-1, 4))
        pixel_count = np.multiply(*self.shape)
        assert (pixel_count, 4) == data1D.shape, "Buffer array should be %s, but is: %s" % (str((pixel_count, 4)), str(data1D.shape))
        self.gl_buffer = ArrayBuffer(data=data1D, usage="DYNAMIC_DRAW", context=self.gl_context);
        self.cl_buffer = cl.GLBuffer(self.cl_context, mf.READ_WRITE, self.gl_buffer._id) # @UndefinedVariable
        # Create CL programs (for upsampling).
        assert self.cl_context is not None, "Need CL context to compile."
        self._cl_upsample_buffer_program = cl.Program(self.cl_context, self._cl_upsample_buffer_source).build()

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
        self._cl_upsample_buffer_program.upsample_buffer(self.cl_queue, (hei_2x * wid_2x,), None, *cl_args)
        cl.enqueue_release_gl_objects(self.cl_queue, cl_gl_data) # @UndefinedVariable
        # (3) Finish.
        self.cl_queue.flush()
        self.cl_queue.finish()

    def upsample_to_new_cpu(self, new_shape, level):
        assert level == self.level - 1, "Level should be 1 less than current level (%d), but is: %d" % (self.level, level)
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
        self.shape = new_shape
        self.level = level

    def upsample_to_new(self, new_shape, level):
        """Upsamples the current buffer to given new shape."""
        assert level == self.level - 1, "Level should be 1 less than current level (%d), but is: %d" % (self.level, level)
        assert 2 == len(new_shape), "Shape should be hei x wid, but is: %s" % (str(new_shape))
        assert 2 == new_shape[1] / self.shape[1], "New width (%d) should be 2x old width (%d)" % (new_shape[1], self.shape[1])
        assert 2 == new_shape[0] / self.shape[0], "New height (%d) should be 2x old height (%d)" % (new_shape[0], self.shape[0])
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
        self.shape = new_shape
        self.level = level

    def set_data(self, data, level=0):
        """Sets a new image as buffer data. All CL buffers will be deleted
        and recreated. The GL buffer stays the same.
        
        Data shape is assumed to be a 2D image with 4 channels."""
        new_shape = data.shape[:2]
        assert 2 == len(new_shape), "Assumed shape is hei x wid, but was %s" % (str(new_shape))
        data1D = np.ascontiguousarray(data.reshape(-1, 4))
        pixel_count = np.multiply(*new_shape)
        assert (pixel_count, 4) == data1D.shape, "Buffer array should be %s, but is: %s" % (str((pixel_count, 4)), str(data1D.shape))
        self.cl_buffer.release()
        self.gl_texture.set_data(data1D)
        self.cl_buffer = cl.GLBuffer(self.cl_context, mf.READ_WRITE, self.gl_buffer._id) # @UndefinedVariable
        self.shape = new_shape
        self.level = level

    def get_data(self):
        """Returns the data in image format, i.e. hei x wid x 4."""
        return self.gl_buffer.get_data().reshape(self.shape + (4,))

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

    def get_level(self):
        """Indicates the current level that the CL textures are on."""
        return self.level

    def get_gl_buffer(self):
        """Returns the GL buffer."""
        return self.gl_buffer

    def get_cl_buffer(self):
        """Returns the CL buffer."""
        return self.cl_buffer

    def release(self):
        """Releases all GPU memory."""
        self.cl_buffer.release();
        self.cl_buffer = None
        self.gl_buffer = None

