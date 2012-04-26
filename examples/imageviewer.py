#!/usr/bin/env python

"""OpenGL image viewer and player.

@author: Stephan Wenger
@date: 2012-02-29
"""

import os
from numpy import array
from PIL import Image

from glitter import Texture2D, get_copy_pipeline_2d
from glitter.contexts.glut import GlutWindow, main_loop

class ImageCache(object):
    def __init__(self, filenames):
        if not filenames:
            filenames = [os.getcwd()]

        def imopen(filename):
            try:
                return Image.open(filename)
            except IOError:
                return None

        def add_files(lst, dirname, fnames):
            lst.extend(filter(None, (imopen(os.path.join(dirname, fname)) for fname in sorted(fnames))))

        self.filenames = []
        for filename in filenames:
            if os.path.isfile(filename):
                self.filenames.append(Image.open(filename))
            elif os.path.isdir(filename):
                os.path.walk(filename, add_files, self.filenames)

    def __len__(self):
        return len(self.filenames)

    def __getitem__(self, idx):
        return array(self.filenames[idx])

class IntroductionExample(object):
    def __init__(self, images):
        self.window = GlutWindow(double=True, multisample=True)
        self.window.display_callback = self.display
        self.window.keyboard_callback = self.keyboard
        self.images = images
        self.window.shape = self.images[0].shape[:2]
        self.render_pipeline = get_copy_pipeline_2d(context=self.window, sampler_type="isampler2D",
                maxval=255, yscale=-1, use_framebuffer=False, image=Texture2D(self.images[0]))
        self.current_index = 0

    def display(self):
        self.window.clear()
        self.render_pipeline.image.data = self.images[self.current_index]
        self.render_pipeline.draw()
        self.window.swap_buffers()

    def keyboard(self, key, x, y):
        # TODO play, pause, speed control, single frame
        raise SystemExit

    def timer(self):
        self.current_index = (self.current_index + 1) % len(self.images)
        self.window.add_timer(1000 / 25, self.timer)
        self.window.post_redisplay()

    def run(self):
        self.timer()
        main_loop()

if __name__ == "__main__":
    import sys
    IntroductionExample(ImageCache(sys.argv[1:])).run()

