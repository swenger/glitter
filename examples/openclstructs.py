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
    ticker = PerformanceTimer()

    # (1) Test mipmap texture.
    if True:
        img_shape = (2160, 4096, 4)
        img = np.float32(np.random.random(img_shape))
        mtex = clio.GLCLMipmapTexture(gl_context, cl_context, img, cl_level=1, cl_access="rw")
        clio.write_cl_texture(cl_context, mtex.get_cl_texture("w"), 20, 20, val1o)
        val1r = mtex.get_data(1)[20, 20, 0]
        assert val1o == val1r, "Texture value (RAM) should still be %.2f, but is %.2f" % (val1o, val1r)
        ticker.tick("4K texture")
        mtex.set_cl_level(0, upsample_if_oneup=True)
        ticker.tick("4K texture")
        print "Texture upsampling took %f seconds (without mem allocation)." % (ticker.diff("4K texture"))
        val1t = clio.read_cl_texture(cl_context, mtex.get_cl_texture("r"), 40, 40)
        assert val1o == val1t, "Texture value should still be %.2f, but is %.2f" % (val1o, val1t)
        val1r = mtex.get_data(0)[40, 40, 0]
        assert val1o == val1r, "Texture value (RAM) should still be %.2f, but is %.2f" % (val1o, val1r)
        mtex.set_data(np.float32(np.ones((4096, 2160, 4))))
        val1T = clio.read_cl_texture(cl_context, mtex.get_cl_texture("r"), 40, 40)
        assert 1. == val1T, "Texture value should still be %.2f, but is %.2f" % (1., val1T)
        mtex.release()

    # (2) Test mipmap buffer.
    if True:
        img_shape = (2161, 4097, 4)
        # img_shape = (40, 60, 4)
        img_half = np.float32(np.random.random((img_shape[0] / 2 - 1, img_shape[1] / 2 - 1, 4)))
        mbuf = clio.GLCLMipmapBuffer(gl_context, cl_context, img_half, 1)
        clio.write_cl_buffer(cl_context, mbuf.get_cl_buffer(), mbuf.get_pos(8, 4), val1o)
        val1r = mbuf.get_data()[4, 8, 0]
        assert val1o == val1r, "Buffer value (RAM) should still be %.2f, but is %.2f" % (val1o, val1r)
        ticker.tick("4K buf")
        mbuf.upsample_to_new(img_shape[:2], 0)
        ticker.tick("4K buf")
        print "Buffer  upsampling took %f seconds (with mem allocation)." % (ticker.diff("4K buf"))
        val1b = clio.read_cl_buffer(cl_context, mbuf.get_cl_buffer(), mbuf.get_pos(16, 8))
        assert val1o == val1b, "Buffer value should still be %.2f, but is %.2f" % (val1o, val1b)
        val1r = mbuf.get_data()[8, 16, 0]
        assert val1o == val1r, "Buffer value (RAM) should still be %.2f, but is %.2f" % (val1o, val1r)
        mbuf.release()


if __name__ == "__main__":
    test_glcl_constructs()
