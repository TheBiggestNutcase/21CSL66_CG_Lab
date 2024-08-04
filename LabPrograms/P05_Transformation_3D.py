import pygame
import math

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Define cube vertices
vertices = [
    [-1, -1, -1],
    [1, -1, -1],
    [1, 1, -1],
    [-1, 1, -1],
    [-1, -1, 1],
    [1, -1, 1],
    [1, 1, 1],
    [-1, 1, 1]
]

# Define edges
edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),  # back face
    (4, 5), (5, 6), (6, 7), (7, 4),  # front face
    (0, 4), (1, 5), (2, 6), (3, 7)   # connecting edges
]

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Function to rotate and scale point
def transform_point(x, y, z, angle_x, angle_y, scale):
    # Scale
    x *= scale
    y *= scale
    z *= scale

    # Rotate around Y-axis
    new_x = x * math.cos(angle_y) - z * math.sin(angle_y)
    new_z = x * math.sin(angle_y) + z * math.cos(angle_y)
    x, z = new_x, new_z

    # Rotate around X-axis
    new_y = y * math.cos(angle_x) - z * math.sin(angle_x)
    new_z = y * math.sin(angle_x) + z * math.cos(angle_x)
    y, z = new_y, new_z

    return x, y, z

# Function to project 3D point to 2D
def project(x, y, z, win_width, win_height, fov, viewer_distance):
    factor = fov / (viewer_distance + z)
    x = x * factor + win_width / 2
    y = -y * factor + win_height / 2
    return x, y

# Main game loop
angle_x, angle_y = 0, 0
scale = 1.0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                angle_y -= 0.1
            elif event.key == pygame.K_RIGHT:
                angle_y += 0.1
            elif event.key == pygame.K_UP:
                angle_x -= 0.1
            elif event.key == pygame.K_DOWN:
                angle_x += 0.1
            elif event.key == pygame.K_PLUS or event.key == pygame.K_EQUALS:
                scale += 0.1
            elif event.key == pygame.K_MINUS:
                scale = max(0.1, scale - 0.1)  # Prevent negative or zero scale

    screen.fill(BLACK)

    # Draw edges
    for edge in edges:
        points = []
        for vertex in edge:
            x, y, z = vertices[vertex]
            x, y, z = transform_point(x, y, z, angle_x, angle_y, scale)
            x, y = project(x, y, z, width, height, 256, 4)
            points.append((x, y))
        pygame.draw.line(screen, WHITE, points[0], points[1], 1)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()