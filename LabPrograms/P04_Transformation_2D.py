import matplotlib.pyplot as plt
import numpy as np

def plot_shape(vertices, color='b', label=None):
    vertices = np.append(vertices, [vertices[0]], axis=0)  # Close the shape
    plt.plot(vertices[:, 0], vertices[:, 1], color=color, label=label)

def translate(vertices, tx, ty):
    translation_matrix = np.array([[1, 0, tx],
                                   [0, 1, ty],
                                   [0, 0, 1]])
    vertices_homogeneous = np.hstack([vertices, np.ones((vertices.shape[0], 1))])
    translated_vertices = vertices_homogeneous.dot(translation_matrix.T)
    return translated_vertices[:, :2]

def rotate(vertices, angle):
    theta = np.radians(angle)
    rotation_matrix = np.array([[np.cos(theta), -np.sin(theta), 0],
                                [np.sin(theta),  np.cos(theta), 0],
                                [0, 0, 1]])
    vertices_homogeneous = np.hstack([vertices, np.ones((vertices.shape[0], 1))])
    rotated_vertices = vertices_homogeneous.dot(rotation_matrix.T)
    return rotated_vertices[:, :2]

def scale(vertices, sx, sy):
    scaling_matrix = np.array([[sx, 0, 0],
                               [0, sy, 0],
                               [0, 0, 1]])
    vertices_homogeneous = np.hstack([vertices, np.ones((vertices.shape[0], 1))])
    scaled_vertices = vertices_homogeneous.dot(scaling_matrix.T)
    return scaled_vertices[:, :2]

def main():
    # Define the original square vertices
    square_vertices = np.array([
        [1, 1],
        [3, 1],
        [3, 3],
        [1, 3]
    ])

    # Define the original triangle vertices
    triangle_vertices = np.array([
        [4, 1],
        [5, 3],
        [6, 1]
    ])

    plt.figure()
    plt.axis('equal')
    plt.grid(True)

    # Plot the original square and triangle
    plot_shape(square_vertices, color='b', label='Original Square')
    plot_shape(triangle_vertices, color='c', label='Original Triangle')

    # Apply and plot the translated square and triangle
    translated_square = translate(square_vertices, 2, 2)
    plot_shape(translated_square, color='r', label='Translated Square (tx=2, ty=2)')

    translated_triangle = translate(triangle_vertices, 2, 2)
    plot_shape(translated_triangle, color='m', label='Translated Triangle (tx=2, ty=2)')

    # Apply and plot the rotated square and triangle
    rotated_square = rotate(square_vertices, 45)
    plot_shape(rotated_square, color='g', label='Rotated Square (45 degrees)')

    rotated_triangle = rotate(triangle_vertices, 45)
    plot_shape(rotated_triangle, color='y', label='Rotated Triangle (45 degrees)')

    # Apply and plot the scaled square and triangle
    scaled_square = scale(square_vertices, 1.5, 0.5)
    plot_shape(scaled_square, color='purple', label='Scaled Square (sx=1.5, sy=0.5)')

    scaled_triangle = scale(triangle_vertices, 1.5, 0.5)
    plot_shape(scaled_triangle, color='orange', label='Scaled Triangle (sx=1.5, sy=0.5)')

    plt.legend()
    plt.title('2D Transformations on a Square and a Triangle')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.show()

if __name__ == "__main__":
    main()
