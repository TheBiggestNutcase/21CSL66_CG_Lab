import pygame
import math
import numpy as np

# Function to draw a circle
def draw_circle(surface, color, center, radius):
    pygame.draw.circle(surface, color, center, int(radius))


pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Variables for animations
angle = 0
scale = 1.0
x_translation = width // 2
y_translation = height // 2
color_change = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    # Clear the screen
    screen.fill((0, 0, 0))

    # Calculate transformations
    scaled_radius = 100 * scale
    x = x_translation + 200 * math.sin(pygame.time.get_ticks() * 0.001)
    y = y_translation + 150 * math.cos(pygame.time.get_ticks() * 0.001)

    # Calculate color
    red = int(255 * 0.5 * (1 + math.sin(color_change)))
    green = int(255 * 0.5 * (1 + math.cos(color_change)))
    blue = int(255 * 0.5 * (1 - math.sin(color_change)))
    color = (red, green, blue)

    # Create a surface for the circle
    circle_surface = pygame.Surface((int(scaled_radius*2), int(scaled_radius*2)), pygame.SRCALPHA)
    draw_circle(circle_surface, color, (int(scaled_radius), int(scaled_radius)), scaled_radius)

    # Rotate the circle
    rotated_circle = pygame.transform.rotate(circle_surface, angle)

    # Draw the rotated circle on the screen
    circle_rect = rotated_circle.get_rect(center=(int(x), int(y)))
    screen.blit(rotated_circle, circle_rect)

    # Update animations
    angle += 1  # Rotate
    scale = 1.5 + 0.5 * math.sin(pygame.time.get_ticks() * 0.001)  # Scale with time
    color_change += 0.01  # Change color over time

    pygame.display.flip()
    clock.tick(60)
