import OpenGL.GL as gl
import OpenGL.GLU as glu
import glfw

# Initialize GLFW and create a window
if not glfw.init():
    raise Exception('GLFW initialization failed')

window = glfw.create_window(800, 600, 'Rectangle', None, None)
if not window:
    glfw.terminate()
    raise Exception('Window creation failed')

glfw.make_context_current(window)

# Set up OpenGL
gl.glMatrixMode(gl.GL_PROJECTION)
gl.glLoadIdentity()
gl.glOrtho(-4, 4, -3, 3, -1, 1)
gl.glMatrixMode(gl.GL_MODELVIEW)

# Set up the rectangle vertices
vertices = [
    (-2, -1),
    (2, -1),
    (2, 1),
    (-2, 1)
]

# Set up the translation and rotation variables
translation_x = 0
translation_y = 0
rotation_angle = 0

# Main loop
while not glfw.window_should_close(window):
    glfw.poll_events()

    # Clear the screen
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)

    # Apply transformations
    gl.glLoadIdentity()
    gl.glTranslatef(translation_x, translation_y, 0)
    gl.glRotatef(rotation_angle, 0, 0, 1)

    # Draw the rectangle
    gl.glBegin(gl.GL_QUADS)
    for vertex in vertices:
        gl.glVertex2f(vertex[0], vertex[1])
    gl.glEnd()

    # Update transformations
    translation_x += 0.01
    translation_y += 0.01
    rotation_angle += 1

    glfw.swap_buffers(window)

# Clean up
glfw.terminate()