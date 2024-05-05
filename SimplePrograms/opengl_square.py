import glfw
from OpenGL.GL import *
import sys

def draw_square():
    glBegin(GL_QUADS)
    glVertex2f(-0.5, -0.5)
    glVertex2f(0.5, -0.5)
    glVertex2f(0.5, 0.5)
    glVertex2f(-0.5, 0.5)
    glEnd()

def main():
    if not glfw.init():
        return

    window = glfw.create_window(800, 600, "OpenGL Square", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    while not glfw.window_should_close(window):
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT)
        glColor3f(1.0, 1.0, 1.0)
        draw_square()
        glfw.swap_buffers(window)

    glfw.terminate()

if __name__ == "__main__":
    main()
