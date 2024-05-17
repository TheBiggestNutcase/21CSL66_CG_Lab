import tkinter as tk
import random

# Initialize the main window
root = tk.Tk()
root.title("Animation Effects")

# Set up the canvas
screen_width = 800
screen_height = 600
canvas = tk.Canvas(root, width=screen_width, height=screen_height, bg="white")
canvas.pack()

# Define colors
colors = ["red", "green", "blue"]

# Define object properties
num_objects = 10
objects = []
for _ in range(num_objects):
    x = random.randint(50, screen_width - 50)
    y = random.randint(50, screen_height - 50)
    radius = random.randint(10, 30)
    color = random.choice(colors)
    speed_x = random.randint(-5, 5)
    speed_y = random.randint(-5, 5)
    obj = {"x": x, "y": y, "radius": radius, "color": color, "speed_x": speed_x, "speed_y": speed_y, "id": None}
    obj["id"] = canvas.create_oval(x-radius, y-radius, x+radius, y+radius, fill=color, outline=color)
    objects.append(obj)

# Animation update function
def update():
    for obj in objects:
        # Move the object
        obj["x"] += obj["speed_x"]
        obj["y"] += obj["speed_y"]

        # Bounce off the edges
        if obj["x"] - obj["radius"] < 0 or obj["x"] + obj["radius"] > screen_width:
            obj["speed_x"] = -obj["speed_x"]
        if obj["y"] - obj["radius"] < 0 or obj["y"] + obj["radius"] > screen_height:
            obj["speed_y"] = -obj["speed_y"]

        # Update the object's position on the canvas
        canvas.coords(obj["id"], obj["x"]-obj["radius"], obj["y"]-obj["radius"], obj["x"]+obj["radius"], obj["y"]+obj["radius"])

    # Schedule the next update
    root.after(16, update)  # Approx 60 FPS

# Start the animation
update()

# Run the Tkinter main loop
root.mainloop()
