"""Move the camera using the mouse.

Usage:
    class Window(GlutWindow):
        def __init__(self):
            self.camera = FreeFlyCam(10, 10)
            self.reshape_callback = self.reshape
            self.mouse_callback = self.mouse
            self.motion_callback = self.motion
            self.display_callback = self.display
            self.shader = ...

        def reshape(self, w, h):
            self.camera.set_window_size(w, h)
            self.window.viewport = (0, 0, w, h)

        def mouse_motion(self, x, y):
            if self.camera.mouse_motion(x, y):
                self.post_redisplay()

        def mouse(self, button, state, x, y):
            self.camera.mouse(button, state, x, y)

        def display(self):
            self.shader.modelview_matrix = self.camera.use()
            ...
"""

import numpy as np
from quaternion import Quaternion
from glitter.contexts.glut import get_shift_state
from math import atan2

class MotionState:
    NOCHANGE = 0
    ROTATE_SELF = 1
    STRAFE = 2
    FORWARD = 3

class FreeFlyCam:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.rotation = Quaternion.make_from_wxyz(1, 0, 0, 0)
        self.position = np.array([0, 0, 0], dtype=float)
        self.up = np.array([0, 1, 0], dtype=float)
        self.center = np.array([0, 0, 0], dtype=float)
        self.motion_state = MotionState.NOCHANGE
        self.strafe_speed = 0.001

    def use(self):
        upVector = self.rotation.rotate(self.up)
        lookAt = self.position + self.rotation.rotate(np.array([0, 0, -1]))

        F = lookAt - self.position
        f = F / np.linalg.norm(F)
        UP = upVector / np.linalg.norm(upVector)
        s1 = np.cross(f, UP)
        s = s1 / np.linalg.norm(s1)
        u = np.cross(s, f)

        fovy = 45.0 * np.pi / 180.0
        aspect = self.width / float(self.height)
        znear = 0.001
        zfar = 1000.0
        focal = 1.0 / np.tan(fovy / 2.0)
        persp_mat = np.zeros((4, 4))
        persp_mat[0, 0] = focal / aspect
        persp_mat[1, 1] = focal 
        persp_mat[2, 2] = (zfar + znear) / (znear - zfar)
        persp_mat[2, 3] = 2 * zfar * znear / (znear - zfar)
        persp_mat[3, 2] = -1

        rot_mat = np.identity(4)
        rot_mat[0, :3] = s
        rot_mat[1, :3] = u
        rot_mat[2, :3] = -f
        t_mat = np.identity(4)
        t_mat[:3, 3] = -self.position

        return np.dot(np.dot(persp_mat, rot_mat), t_mat)

    def set_window_size(self, w, h):
        self.width = w
        self.height = h

    def mouse(self, button, state, x, y):
        self.old_x = x;
        self.old_y = y;
        
        if button == 0 and state == 0:
            if get_shift_state():
                self.motion_state = MotionState.STRAFE
            else:
                self.motion_state = MotionState.ROTATE_SELF

        if button == 2 and state == 0:
            self.motion_state = MotionState.FORWARD

        if state == 1:
            self.motion_state = MotionState.NOCHANGE

    def perform_rotate(self, x, y):
        v1 = np.array([self.old_x - self.width / 2, self.height / 2 - self.old_y])
        v2 = np.array([x - self.width / 2, self.height / 2 - y])
        scale = np.sqrt(v1[0] ** 2. / (self.width / 2.) ** 2 + (v1[1] ** 2. / (self.height / 2.) ** 2.))
        scale = scale ** 2.

        angle = atan2(v2[0], v2[1]) - atan2(v1[0], v1[1])
        
        while angle > np.pi:
            angle -= 2*np.pi

        while angle < -np.pi:
            angle += 2*np.pi

        r1 = Quaternion.make_from_axis_angle([0, 1, 0], (1-scale) * 0.001 * (x - self.old_x))
        r2 = Quaternion.make_from_axis_angle([1, 0, 0], (1-scale) * 0.001 * (y - self.old_y))
        r3 = Quaternion.make_from_axis_angle([0, 0, 1], scale * angle)
        
        self.rotation = self.rotation * (r3 * r2 * r1)
        self.rotation.normalize();

    def mouse_motion(self, x, y): 
        result = False
        if self.motion_state == MotionState.ROTATE_SELF:
            self.perform_rotate(x, y)
            result = True

        if self.motion_state == MotionState.FORWARD:
             pres = self.rotation.rotate([0, 0, 1]);
             self.position += pres * self.strafe_speed * (y - self.old_y);
             result = True

        if self.motion_state == MotionState.STRAFE:
             dX = self.rotation.rotate([1, 0, 0]) * self.strafe_speed * (self.old_x - x)
             dY = self.rotation.rotate([0, 1, 0]) * self.strafe_speed * (y - self.old_y)
             self.position += dX + dY;
             result = True

        self.old_x = x;
        self.old_y = y;
        return result

