import OpenGL.GL as gl
import OpenGL.GLU as glu
import glfw

# Initialize GLFW and create a window
if not glfw.init():
    raise Exception('GLFW initialization failed')

window = glfw.create_window(800, 600, 'Cube', None, None)
if not window:
    glfw.terminate()
    raise Exception('Window creation failed')

glfw.make_context_current(window)

# Set up OpenGL
gl.glMatrixMode(gl.GL_PROJECTION)
glu.gluPerspective(45, 800 / 600, 0.1, 50.0)
gl.glMatrixMode(gl.GL_MODELVIEW)

# Set up the cube vertices
vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

# Set up the cube edges
edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7)
)

# Set up the rotation angles
rotation_x = 0
rotation_y = 0
rotation_z = 0

# Main loop
while not glfw.window_should_close(window):
    glfw.poll_events()

    # Clear the screen
    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)

    # Apply the rotation
    gl.glLoadIdentity()
    gl.glTranslatef(0.0, 0.0, -5)
    gl.glRotatef(rotation_x, 1, 0, 0)
    gl.glRotatef(rotation_y, 0, 1, 0)
    gl.glRotatef(rotation_z, 0, 0, 1)

    # Draw the cube
    gl.glBegin(gl.GL_LINES)
    for edge in edges:
        for vertex in edge:
            gl.glVertex3fv(vertices[vertex])
    gl.glEnd()

    # Update the rotation angles
    rotation_x += 1
    rotation_y += 2
    rotation_z += 3

    glfw.swap_buffers(window)

# Clean up
glfw.terminate()