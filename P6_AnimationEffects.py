import OpenGL.GL as gl
import OpenGL.GLU as glu
import glfw
import math

# Initialize GLFW and create a window
if not glfw.init():
    raise Exception('GLFW initialization failed')

window = glfw.create_window(800, 600, 'Animation Effects', None, None)
if not window:
    glfw.terminate()
    raise Exception('Window creation failed')

glfw.make_context_current(window)

# Set up OpenGL
gl.glMatrixMode(gl.GL_PROJECTION)
gl.glLoadIdentity()
gl.glOrtho(-4, 4, -3, 3, -1, 1)
gl.glMatrixMode(gl.GL_MODELVIEW)

# Define the vertices for the objects
square_vertices = [
    (-1, -1),
    (1, -1),
    (1, 1),
    (-1, 1)
]

triangle_vertices = [
    (-1, 0),
    (1, 0),
    (0, 1)
]

# Set up the animation variables
square_rotation = 0
triangle_scale = 1
animation_offset = 0

# Main loop
while not glfw.window_should_close(window):
    glfw.poll_events()

    # Clear the screen
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)

    # Animate the square
    gl.glLoadIdentity()
    gl.glTranslatef(math.sin(animation_offset) * 2, 0, 0)
    gl.glRotatef(square_rotation, 0, 0, 1)

    # Draw the square
    gl.glBegin(gl.GL_QUADS)
    for vertex in square_vertices:
        gl.glVertex2f(vertex[0], vertex[1])
    gl.glEnd()

    # Animate the triangle
    gl.glLoadIdentity()
    gl.glTranslatef(-math.sin(animation_offset) * 2, 0, 0)
    gl.glScalef(triangle_scale, triangle_scale, 1)

    # Draw the triangle
    gl.glBegin(gl.GL_TRIANGLES)
    for vertex in triangle_vertices:
        gl.glVertex2f(vertex[0], vertex[1])
    gl.glEnd()

    # Update animation variables
    square_rotation += 1
    triangle_scale += 0.01
    animation_offset += 0.01

    glfw.swap_buffers(window)

# Clean up
glfw.terminate()