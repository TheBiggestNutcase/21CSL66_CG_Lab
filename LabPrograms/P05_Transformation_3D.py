import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

# Define vertices, edges, and colors of a proper cube
vertices = ((1,-1,-1),
            (1,1,-1),
            (-1,1,-1),
            (-1,-1,-1),
            (1,-1,1),
            (1,1,1),
            (-1,-1,1),
            (-1,1,1))

edges = ((0, 1),
         (1, 2),
         (2, 3),
         (3, 0),
         (4, 5),
         (5, 6),
         (6, 7),
         (7, 4),
         (0, 4),
         (1, 5),
         (2, 6),
         (3, 7))

surfaces = ((0, 1, 2, 3),
            (3, 2, 7, 6),
            (6, 7, 5, 4),
            (4, 5, 1, 0),
            (1, 5, 7, 2),
            (4, 0, 3, 6))

colors = ((1, 0, 0),
          (0, 1, 0),
          (0, 0, 1),
          (1, 1, 0),
          (1, 0, 1),
          (0, 1, 1),
          (1, 1, 1),
          (0.5, 0.5, 0.5))

def draw_cube():
    glBegin(GL_QUADS)
    for surface in surfaces:
        for vertex in surface:
            glColor3fv(colors[vertex])
            glVertex3fv(vertices[vertex])
    glEnd()

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glColor3fv((0, 0, 0))
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)
    
    # Variables for transformations
    angle_x = 0
    angle_y = 0
    scale = 1.0
    x_translation = 0
    y_translation = 0

    clock = pygame.time.Clock()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    angle_y -= 5
                elif event.key == K_RIGHT:
                    angle_y += 5
                elif event.key == K_UP:
                    angle_x -= 5
                elif event.key == K_DOWN:
                    angle_x += 5
                elif event.key == K_PLUS or event.key == K_EQUALS:
                    scale += 0.1
                elif event.key == K_MINUS or event.key == K_UNDERSCORE:
                    scale -= 0.1

        # Clear the screen and set the color
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glClearColor(0.0, 0.0, 0.0, 1.0)
        
        # Apply transformations
        glPushMatrix()
        glTranslatef(x_translation, y_translation, 0)
        glRotatef(angle_x, 1, 0, 0)
        glRotatef(angle_y, 0, 1, 0)
        glScalef(scale, scale, scale)
        
        # Draw the cube
        draw_cube()
        
        glPopMatrix()

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
