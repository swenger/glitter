import numpy
import pyopencl as cl
from pyopencl.tools import get_gl_sharing_context_properties

from glitter import ArrayBuffer, VertexArray, get_default_program
from glitter.contexts.glut import GlutWindow, main_loop

kernel_code = """
__kernel void animate(__global float4* positions,
                      __global float4* colors,
                      __global float4* velocities,
                      __global float4* initial_positions,
                      __global float4* initial_velocities,
                      float dt) {
    unsigned int i = get_global_id(0);
    float4 p = positions[i];
    float4 v = velocities[i];
    float life = velocities[i].w;

    life -= dt;
    if (life <= 0.0) {
        p = initial_positions[i];
        v = initial_velocities[i];
        life = 1.0;    
    }

    v.z -= 9.8 * dt;
    p.xyz += v.xyz * dt;
    v.w = life;

    positions[i] = p;
    velocities[i] = v;
    colors[i].w = life;
}
"""

class CLCode(object):
    def __init__(self, num, gl_positions, gl_colors, velocities, dt=0.001):
        platform = cl.get_platforms()[0]
        self.ctx = cl.Context(properties=[(cl.context_properties.PLATFORM, platform)] + get_gl_sharing_context_properties(), devices=None)
        self.queue = cl.CommandQueue(self.ctx)
        self.program = cl.Program(self.ctx, kernel_code).build()

        self.num = num
        self.gl_positions = gl_positions
        self.gl_colors = gl_colors
        self.velocities = velocities
        self.dt = numpy.float32(dt)

        self.cl_positions = cl.GLBuffer(self.ctx, cl.mem_flags.READ_WRITE, self.gl_positions._id) # TODO wrap this?
        self.cl_colors = cl.GLBuffer(self.ctx, cl.mem_flags.READ_WRITE, self.gl_colors._id) # TODO wrap this?
        self.cl_velocities = cl.Buffer(self.ctx, cl.mem_flags.READ_ONLY | cl.mem_flags.COPY_HOST_PTR, hostbuf=velocities)
        self.cl_initial_positions = cl.Buffer(self.ctx, cl.mem_flags.READ_ONLY | cl.mem_flags.COPY_HOST_PTR, hostbuf=self.gl_positions.data)
        self.cl_initial_velocities = cl.Buffer(self.ctx, cl.mem_flags.READ_ONLY | cl.mem_flags.COPY_HOST_PTR, hostbuf=self.velocities)

        #self.queue.finish() # TODO is this necessary?
        
    def execute(self, sub_intervals):
        cl.enqueue_acquire_gl_objects(self.queue, [self.cl_positions, self.cl_colors])
        args = (self.cl_positions, self.cl_colors, self.cl_velocities, self.cl_initial_positions, self.cl_initial_velocities, self.dt)
        for i in xrange(0, sub_intervals):
            self.program.animate(self.queue, [self.num], None, *args)
        cl.enqueue_release_gl_objects(self.queue, [self.cl_positions, self.cl_colors])
        #self.queue.finish() # TODO is this necessary?

def timer(last_time=[0]):
    cle.execute(10)
    #window.flush() # TODO is this necessary?
    window.add_timer(1, timer)
    window.post_redisplay()

def keyboard(*args):
    raise SystemExit

def display():
    window.clear()
    vao.draw()
    window.swap_buffers()

if __name__ == "__main__":
    num = 200000

    window = GlutWindow(double=True, alpha=True, depth=True)
    window.display_callback = display
    window.keyboard_callback = keyboard

    positions = numpy.ndarray((num, 4), dtype=numpy.float32)
    colors = numpy.ndarray((num, 4), dtype=numpy.float32)
    velocities = numpy.ndarray((num, 4), dtype=numpy.float32)

    positions[:, 0] = numpy.sin(numpy.arange(0, num) * 2 * numpy.pi / num) * (numpy.random.random_sample((num,)) / 3 + 0.2)
    positions[:, 1] = numpy.cos(numpy.arange(0, num) * 2 * numpy.pi / num) * (numpy.random.random_sample((num,)) / 3 + 0.2)
    positions[:, 2:] = 0, 1
    colors[:] = 0, 1, 0, 1
    velocities[:, :2] = 2 * positions[:, :2]
    velocities[:, 2] = 3
    velocities[:, 3] = numpy.random.random_sample((num,))

    gl_positions = ArrayBuffer(data=positions, usage="DYNAMIC_DRAW")
    gl_colors = ArrayBuffer(data=colors, usage="DYNAMIC_DRAW")
    vao = VertexArray([gl_positions, gl_colors])
    shader = get_default_program()
    
    cle = CLCode(num, gl_positions, gl_colors, velocities)

    with shader(modelview_matrix=((1, 0, 0, 0), (0, 0, 1, 0), (0, 1, 0, 0), (0, 0, 0, 2))):
        timer()
        main_loop()

