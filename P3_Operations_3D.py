import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Define the cube vertices
def create_cube():
    vertices = np.array([
        [0, 0, 0],
        [1, 0, 0],
        [1, 1, 0],
        [0, 1, 0],
        [0, 0, 1],
        [1, 0, 1],
        [1, 1, 1],
        [0, 1, 1]
    ])
    return vertices

# Define the faces of the cube
def create_faces(vertices):
    faces = [
        [vertices[j] for j in [0, 1, 2, 3]],
        [vertices[j] for j in [4, 5, 6, 7]],
        [vertices[j] for j in [0, 1, 5, 4]],
        [vertices[j] for j in [2, 3, 7, 6]],
        [vertices[j] for j in [1, 2, 6, 5]],
        [vertices[j] for j in [4, 7, 3, 0]]
    ]
    return faces

# Translation function
def translate(vertices, tx, ty, tz):
    translation_matrix = np.array([tx, ty, tz])
    return vertices + translation_matrix

# Rotation function (around the Z axis)
def rotate(vertices, angle):
    theta = np.radians(angle)
    rotation_matrix = np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta), np.cos(theta), 0],
        [0, 0, 1]
    ])
    return np.dot(vertices, rotation_matrix)

# Scaling function
def scale(vertices, sx, sy, sz):
    scaling_matrix = np.array([
        [sx, 0, 0],
        [0, sy, 0],
        [0, 0, sz]
    ])
    return np.dot(vertices, scaling_matrix)

# Plotting function
def plot_cube(vertices, title):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    faces = create_faces(vertices)
    face_collection = Poly3DCollection(faces, alpha=0.25, linewidths=1, edgecolors='r')
    face_collection.set_facecolor('cyan')
    ax.add_collection3d(face_collection)
    
    # Plot the vertices
    ax.scatter3D(vertices[:, 0], vertices[:, 1], vertices[:, 2])
    
    # Setting the plot title
    ax.set_title(title)
    
    # Set labels
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    
    # Set the aspect ratio to be equal
    ax.set_box_aspect([1,1,1])
    
    plt.show()

# Create the original cube
original_cube = create_cube()

# Plot the original cube
plot_cube(original_cube, "Original Cube")

# Translate the cube
translated_cube = translate(original_cube, 2, 3, 1)
plot_cube(translated_cube, "Translated Cube (tx=2, ty=3, tz=1)")

# Rotate the cube
rotated_cube = rotate(original_cube, 45)
plot_cube(rotated_cube, "Rotated Cube (45 degrees around Z-axis)")

# Scale the cube
scaled_cube = scale(original_cube, 1.5, 0.5, 2)
plot_cube(scaled_cube, "Scaled Cube (sx=1.5, sy=0.5, sz=2)")
