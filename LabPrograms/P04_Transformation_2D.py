import matplotlib.pyplot as plt
import numpy as np

def plot_shape(vertices, color='b', label=None):
    vertices = np.append(vertices, [vertices[0]], axis=0)  # Close the shape
    plt.plot(vertices[:, 0], vertices[:, 1], color=color, label=label)

def translate(vertices, tx, ty):
    return vertices + np.array([tx, ty])

def rotate(vertices, angle):
    theta = np.radians(angle)
    rotation_matrix = np.array([[np.cos(theta), -np.sin(theta)],
                                [np.sin(theta),  np.cos(theta)]])
    return vertices.dot(rotation_matrix)

def scale(vertices, sx, sy):
    return vertices * np.array([sx, sy])

square_vertices = np.array([[1, 1], [3, 1], [3, 3], [1, 3]])
triangle_vertices = np.array([[4, 1], [5, 3], [6, 1]])

plt.figure()
plt.axis('equal')
plt.grid(True)

# Plot the original shapes
plot_shape(square_vertices, color='b', label='Original Square')
plot_shape(triangle_vertices, color='c', label='Original Triangle')

# Apply and plot the translated shapes
plot_shape(translate(square_vertices, 2, 2), color='r', label='Translated Square (tx=2, ty=2)')
plot_shape(translate(triangle_vertices, 2, 2), color='m', label='Translated Triangle (tx=2, ty=2)')

# Apply and plot the rotated shapes
plot_shape(rotate(square_vertices, 45), color='g', label='Rotated Square (45 degrees)')
plot_shape(rotate(triangle_vertices, 45), color='y', label='Rotated Triangle (45 degrees)')

# Apply and plot the scaled shapes
plot_shape(scale(square_vertices, 1.5, 0.5), color='purple', label='Scaled Square (sx=1.5, sy=0.5)')
plot_shape(scale(triangle_vertices, 1.5, 0.5), color='orange', label='Scaled Triangle (sx=1.5, sy=0.5)')

plt.legend()
plt.title('2D Transformations on a Square and a Triangle')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()