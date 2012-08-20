#!/usr/bin/env python

"""OpenGL player for videos stored as directories of image files.

@author: Stephan Wenger
@date: 2012-02-29
"""

import os
from numpy import array
from PIL import Image

from glitter import Texture2D, get_copy_pipeline_2d
import glitter.raw as _gl
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
            lst.extend(x for x in (imopen(os.path.join(dirname, fname)) for fname in sorted(fnames)) if x)

        self.filenames = []
        for filename in filenames:
            if os.path.isfile(filename):
                self.filenames.append(Image.open(filename))
            elif os.path.isdir(filename):
                os.path.walk(filename, add_files, self.filenames)

    def __len__(self):
        return len(self.filenames)

    def __getitem__(self, idx):
        return array(self.filenames[idx]) # TODO caching and preloading

class IntroductionExample(object):
    fps_scale = 1.1

    def __init__(self, images):
        self.window = GlutWindow(double=True, multisample=True)
        self.window.display_callback = self.display
        self.window.keyboard_callback = self.keyboard
        self.window.special_callback = self.special
        self.images = images
        self.window.shape = self.images[0].shape[:2]
        self.render_pipeline = get_copy_pipeline_2d(context=self.window, sampler_type="isampler2D",
                maxval=255, yscale=-1, use_framebuffer=False, image=Texture2D(self._prepare_image(0)))
        self.current_index = 0
        self.fps = 25
        self.playing = False

    def _prepare_image(self, idx):
        img = self.images[idx]
        while img.ndim < 3:
            img = img[..., None]
        return img

    def display(self):
        self.window.clear()
        self.render_pipeline.image.data = self._prepare_image(self.current_index)
        self.window.window_title = self.images.filenames[self.current_index].filename
        self.render_pipeline.draw()
        self.window.swap_buffers()

    def keyboard(self, key, x, y):
        key = chr(key)
        if key == "+":
            self.fps *= self.fps_scale
        elif key == "-":
            self.fps /= self.fps_scale
        elif key == " ":
            if self.playing:
                self.playing = False
            else:
                self.playing = True
                self.timer()
        elif key == chr(27):
            raise SystemExit

    def special(self, key, x, y):
        if key == _gl.GLUT_KEY_LEFT:
            self.current_index = (self.current_index - 1) % len(self.images)
            self.window.post_redisplay()
        elif key == _gl.GLUT_KEY_RIGHT:
            self.current_index = (self.current_index + 1) % len(self.images)
            self.window.post_redisplay()
        if key == _gl.GLUT_KEY_PAGE_UP:
            self.current_index = (self.current_index - self.fps) % len(self.images)
            self.window.post_redisplay()
        elif key == _gl.GLUT_KEY_PAGE_DOWN:
            self.current_index = (self.current_index + self.fps) % len(self.images)
            self.window.post_redisplay()
        elif key == _gl.GLUT_KEY_HOME:
            self.current_index = 0
            self.window.post_redisplay()
        elif key == _gl.GLUT_KEY_END:
            self.current_index = len(self.images) - 1
            self.window.post_redisplay()

    def timer(self):
        if self.playing:
            self.current_index = (self.current_index + 1) % len(self.images)
            self.window.add_timer(int(round(1000.0 / self.fps)), self.timer)
            self.window.post_redisplay()

    def run(self):
        self.timer()
        main_loop()

if __name__ == "__main__":
    import sys
    IntroductionExample(ImageCache(sys.argv[1:])).run()

