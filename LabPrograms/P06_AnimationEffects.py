import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math
import numpy as np

# Function to draw a circle
def draw_circle(radius, num_segments):
    glBegin(GL_TRIANGLE_FAN)
    for i in range(num_segments + 1):
        angle = 2.0 * math.pi * i / num_segments
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        glVertex2f(x, y)
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluOrtho2D(-400, 400, -300, 300)

    # Variables for animations
    angle = 0
    scale = 1.0
    x_translation = 0
    y_translation = 0
    color_change = 0

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # Clear the screen and set the color
        glClear(GL_COLOR_BUFFER_BIT)
        glClearColor(0.0, 0.0, 0.0, 1.0)

        # Apply transformations
        glPushMatrix()
        glTranslatef(x_translation, y_translation, 0)
        glRotatef(angle, 0, 0, 1)
        glScalef(scale, scale, 1.0)
        
        # Apply color change
        red = 0.5 * (1 + np.sin(color_change))
        green = 0.5 * (1 + np.cos(color_change))
        blue = 0.5 * (1 - np.sin(color_change))
        glColor3f(red, green, blue)

        # Draw the circle
        draw_circle(100, 50)
        
        glPopMatrix()

        # Update animations
        angle += 1  # Rotate
        scale = 1.5 + 0.5 * np.sin(pygame.time.get_ticks() * 0.001)  # Scale with time
        x_translation = 200 * np.sin(pygame.time.get_ticks() * 0.001)  # Translate with time
        y_translation = 150 * np.cos(pygame.time.get_ticks() * 0.001)  # Translate with time
        color_change += 0.01  # Change color over time

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
