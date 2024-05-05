import math
import glfw
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_square():
    glBegin(GL_QUADS)
    glVertex2f(-0.5, -0.5)
    glVertex2f(0.5, -0.5)
    glVertex2f(0.5, 0.5)
    glVertex2f(-0.5, 0.5)
    glEnd()

def draw_circle(radius, num_segments=100):
    glBegin(GL_TRIANGLE_FAN)
    for i in range(num_segments):
        theta = 2.0 * 3.1415926 * i / num_segments
        x = radius * math.cos(theta)
        y = radius * math.sin(theta)
        glVertex2f(x, y)
    glEnd()

def draw_line(x1, y1, x2, y2):
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, 1, 1)
    glPointSize(2)

    # Draw a square
    glColor3f(1, 0, 0)  # Red
    glLoadIdentity()
    glTranslatef(-0.5, 0.5, 0)
    draw_square()

    # Draw a circle
    glColor3f(0, 1, 0)  # Green
    glLoadIdentity()
    glTranslatef(0.5, 0.5, 0)
    draw_circle(0.3)

    # Draw a line
    glColor3f(0, 0, 1)  # Blue
    glLoadIdentity()
    draw_line(-0.8, -0.8, 0.8, -0.8)

    glfw.swap_buffers(window)

def resize(window, width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-1, 1, -1, 1)
    glMatrixMode(GL_MODELVIEW)

def key_callback(window, key, scancode, action, mods):
    if key == glfw.KEY_ESCAPE and action == glfw.PRESS:
        glfw.set_window_should_close(window, True)

def main():
    if not glfw.init():
        return

    global window
    window = glfw.create_window(800, 600, "Basic Geometric Operations", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)
    glfw.set_window_size_callback(window, resize)
    glfw.set_key_callback(window, key_callback)

    glClearColor(0, 0, 0, 0)

    while not glfw.window_should_close(window):
        glfw.poll_events()
        display()

    glfw.terminate()

if __name__ == "__main__":
    main()
