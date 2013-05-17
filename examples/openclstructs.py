#!/usr/bin/env python
"""Tests the advanced OpenGL/CL interoperability constructs.

@author: Kai Ruhl
@since 2013-02"""

import numpy as np
import time
import glitter.convenience.clinterop as clio


class PerformanceTimer(object):
    """Records a series of ticks and gives statistics about them."""

    def __init__(self):
        self.tick_list = [time.time()]
        self.tick_dict = {}

    def tick(self, tick_id=None):
        """Adds a stop time to list of recorded tick timestamps.
        If a tick id is given, there is a tick list specifically for that id."""
        if tick_id is None:
            tick_list = self.tick_list
        else:
            if self.tick_dict.has_key(tick_id):
                tick_list = self.tick_dict[tick_id]
            else:
                tick_list = []
                self.tick_dict[tick_id] = tick_list
        tick_list.append(time.time())

    def diff(self, tick_id=None, events_back=1):
        """Returns the difference to the tick recorded one (or events_back
        many) before.
        
        If a tick id is given, there is a tick list specifically for that id."""
        tick_list = self.tick_list if tick_id is None else self.tick_dict[tick_id]
        event_idx = max(0, len(tick_list) - 1 - events_back)
        return tick_list[-1] - tick_list[event_idx]


def test_glcl_constructs():
    """Tests the mipmap textures and array buffers."""
    gl_context = clio.get_gl_context("q")
    cl_context = clio.get_cl_context(gl_context)
    val1o = 500. # do not take -99.99 or assert will fail due to float inaccuracies.
    val2o = 250.
    ticker = PerformanceTimer()

    # (1) Test mipmap texture.
    if True:
        img_shape = (2161, 4097, 4)
        img_half_shape = (img_shape[0] / 2, img_shape[1] / 2, 4)
        img = np.float32(np.random.random(img_shape))
        mtex = clio.GLCLMipmapTexture(gl_context, cl_context, img, level=1, cl_access="rw")
        clio.write_cl_texture(cl_context, mtex.get_cl_object("w"), 20, 20, val1o)
        clio.write_cl_texture(cl_context, mtex.get_cl_object("w"), img_half_shape[1] - 1, img_half_shape[0] - 1, val2o)
        val1r = mtex.get_data(1)[20, 20, 0]
        assert val1o == val1r, "Texture value (RAM) should still be %.2f, but is %.2f" % (val1o, val1r)
        val2r = mtex.get_data(1)[img_half_shape[0] - 1, img_half_shape[1] - 1, 0]
        assert val2o == val2r, "Texture border value (RAM) should still be %.2f, but is %.2f" % (val2o, val2r)
        # (a) Upsample.
        ticker.tick("4K texture")
        mtex.set_level(0, upsample_if_oneup=True)
        ticker.tick("4K texture")
        print "Texture upsampling took %f seconds (without mem allocation)." % (ticker.diff("4K texture"))
        val1t = clio.read_cl_texture(cl_context, mtex.get_cl_object("r"), 40, 40)
        assert val1o == val1t, "Texture value should still be %.2f, but is %.2f" % (val1o, val1t)
        val1r = mtex.get_data(0)[40, 40, 0]
        assert val1o == val1r, "Texture value (RAM) should still be %.2f, but is %.2f" % (val1o, val1r)
        val2t = clio.read_cl_texture(cl_context, mtex.get_cl_object("r"), img_shape[1] - 1, img_shape[0] - 1)
        assert val2o == val2t, "Texture border value should still be %.2f, but is %.2f" % (val2o, val2t)
        val2r = mtex.get_data(0)[img_shape[0] - 1, img_shape[1] - 1, 0]
        assert val2o == val2r, "Texture border value (RAM) should still be %.2f, but is %.2f" % (val2o, val2r)
        # (b) Replace data.
        mtex.set_data(np.float32(np.ones((80, 160, 4))))
        val1T = clio.read_cl_texture(cl_context, mtex.get_cl_object("r"), 40, 40)
        assert 1. == val1T, "Texture value should still be %.2f, but is %.2f" % (1., val1T)
        mtex.reset()
        mtex.release()

    # (2) Test mipmap buffer.
    if True:
        img_shape = (2161, 4097, 4)
        img_half_shape = (img_shape[0] / 2, img_shape[1] / 2, 4)
        img_half = np.float32(np.random.random(img_half_shape))
        mbuf = clio.GLCLMipmapBuffer(gl_context, cl_context, max_shape=img_shape[:2], data=img_half, level=1)
        clio.write_cl_buffer(cl_context, mbuf.cl, mbuf.get_pos(8, 4), val1o)
        clio.write_cl_buffer(cl_context, mbuf.cl, mbuf.get_pos(img_half_shape[1] - 1, img_half_shape[0] - 1), val2o)
        val1r = mbuf.get_data()[4, 8, 0]
        assert val1o == val1r, "Buffer value (RAM) should still be %.2f, but is %.2f" % (val1o, val1r)
        val2r = mbuf.get_data(1)[img_half_shape[0] - 1, img_half_shape[1] - 1, 0]
        assert val2o == val2r, "Buffer border value (RAM) should still be %.2f, but is %.2f" % (val2o, val2r)
        # (a) Upsample.
        ticker.tick("4K buf")
        mbuf.set_level(0, upsample_if_oneup=True)
        ticker.tick("4K buf")
        print "Buffer  upsampling took %f seconds (with mem allocation)." % (ticker.diff("4K buf"))
        val1b = clio.read_cl_buffer(cl_context, mbuf.cl, mbuf.get_pos(16, 8))
        assert val1o == val1b, "Buffer value should still be %.2f, but is %.2f" % (val1o, val1b)
        val1r = mbuf.get_data()[8, 16, 0]
        assert val1o == val1r, "Buffer value (RAM) should still be %.2f, but is %.2f" % (val1o, val1r)
        val2t = clio.read_cl_buffer(cl_context, mbuf.cl, mbuf.get_pos(img_shape[1] - 1, img_shape[0] - 1))
        assert val2o == val2t, "Buffer border value should still be %.2f, but is %.2f" % (val2o, val2t)
        val2r = mbuf.get_data(0)[img_shape[0] - 1, img_shape[1] - 1, 0]
        assert val2o == val2r, "Buffer border value (RAM) should still be %.2f, but is %.2f" % (val2o, val2r)
        # (b) Replace data.
        mbuf.set_data(np.float32(np.ones(img_half_shape)), level=1) # must be one of image pyramid.
        val1T = clio.read_cl_buffer(cl_context, mbuf.cl, 0)
        assert 1. == val1T, "Onebuf value should still be %.2f, but is %.2f" % (1., val1T)
        mbuf.set_data(np.float32(2. * np.ones(img_shape)), level=0) # must be one of image pyramid.
        mbuf.reset()
        mbuf.release()

    # (3) Test onemap buffer (array buffer with only one field).
    if True:
        img_shape = (2161, 4097, 4)
        img_half_shape = (img_shape[0] / 2, img_shape[1] / 2, 4)
        img_half = np.float32(np.random.random(img_half_shape))
        mbuf = clio.GLCLOnemapBuffer(gl_context, cl_context, img_shape[:2], img_half, 1)
        clio.write_cl_buffer(cl_context, mbuf.cl, mbuf.get_pos(8, 4), val1o)
        clio.write_cl_buffer(cl_context, mbuf.cl, mbuf.get_pos(img_half_shape[1] - 1, img_half_shape[0] - 1), val2o)
        val1r = mbuf.get_data(1)[4, 8, 0]
        assert val1o == val1r, "Onebuf value (RAM) should still be %.2f, but is %.2f" % (val1o, val1r)
        val1r = mbuf.get_data(0)[mbuf.get_data_pos(8, 4) + (0,)]
        assert val1o == val1r, "Onebuf value (RAM) should still be %.2f, but is %.2f" % (val1o, val1r)
        val2r = mbuf.get_data(1)[img_half_shape[0] - 1, img_half_shape[1] - 1, 0]
        assert val2o == val2r, "Onebuf border value (RAM) should still be %.2f, but is %.2f" % (val2o, val2r)
        # (a) Upsample.
        ticker.tick("4K onebuf")
        mbuf.set_level(0, upsample_if_oneup=True)
        ticker.tick("4K onebuf")
        print "Onebuf  upsampling took %f seconds (without mem allocation)." % (ticker.diff("4K onebuf"))
        val1b = clio.read_cl_buffer(cl_context, mbuf.cl, mbuf.get_pos(16, 8))
        assert val1o == val1b, "Onebuf value should still be %.2f, but is %.2f" % (val1o, val1b)
        val1r = mbuf.get_data()[8, 16, 0]
        assert val1o == val1r, "Onebuf value (RAM) should still be %.2f, but is %.2f" % (val1o, val1r)
        val2t = clio.read_cl_buffer(cl_context, mbuf.cl, mbuf.get_pos(img_shape[1] - 1, img_shape[0] - 1))
        assert val2o == val2t, "Onebuf border value should still be %.2f, but is %.2f" % (val2o, val2t)
        val2r = mbuf.get_data(0)[img_shape[0] - 1, img_shape[1] - 1, 0]
        assert val2o == val2r, "Onebuf border value (RAM) should still be %.2f, but is %.2f" % (val2o, val2r)
        # (b) Replace data.
        mbuf.set_data(np.float32(np.ones(img_half_shape)), level=1) # must be one of image pyramid.
        val1T = clio.read_cl_buffer(cl_context, mbuf.cl, 0)
        assert 1. == val1T, "Onebuf value should still be %.2f, but is %.2f" % (1., val1T)
        val1T = clio.read_cl_buffer(cl_context, mbuf.cl, 1)
        assert 1. != val1T, "Onebuf value should be random, but is %.2f" % (val1T)
        mbuf.set_data(np.float32(2. * np.ones(img_shape)), level=0) # must be one of image pyramid.
        mbuf.reset_to_zero()
        assert (0. == mbuf.get_data(level=0)).all(), "Buffer data was supposed to be reset to zero, but was not."
        mbuf.reset()
        mbuf.release()


if __name__ == "__main__":
    test_glcl_constructs()
