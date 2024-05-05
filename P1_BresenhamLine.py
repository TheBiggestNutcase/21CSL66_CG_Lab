from OpenGL.GL import *
from OpenGL.GLUT import *

X1, Y1, X2, Y2 = 0, 0, 0, 0

def LineBres():
    global X1, Y1, X2, Y2  # Define X1, Y1, X2, Y2 as global
    glClear(GL_COLOR_BUFFER_BIT)
    dx = abs(X2 - X1)
    dy = abs(Y2 - Y1)
    p = 2 * dy - dx
    twoDy = 2 * dy
    twoDyDx = 2 * (dy - dx)
    x, y = 0, 0
    if X1 > X2:
        x = X2
        y = Y2
        X2 = X1
    else:
        x = X1
        y = Y1
        X2 = X2
    glBegin(GL_POINTS)
    glVertex2i(x, y)
    while x < X2:
        x += 1
        if p < 0:
            p += twoDy
        else:
            y += 1
            p += twoDyDx
        glVertex2i(x, y)
    glEnd()
    glFlush()

def Init():
    glClearColor(1.0, 1.0, 1.0, 0)
    glColor3f(0.0, 0.0, 0.0)
    glPointSize(8.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, 500, 0, 500, -1, 1)

def display():
    LineBres()

def main():
    global X1, Y1, X2, Y2
    print("Enter two points for drawing line Bresenham:")
    X1, Y1 = map(int, input("\nEnter points (X1,Y1): ").split())
    X2, Y2 = map(int, input("Enter points (X2,Y2): ").split())

    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutCreateWindow("LINE BRESENHAM")
    Init()
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()
