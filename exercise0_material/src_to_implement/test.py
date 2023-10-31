import numpy as np
import matplotlib.pyplot as plt

rows = 10  # Number of rows
columns = 10  # Number of columns

# Create an empty array filled with white (255, 255, 255)
checkerboard = np.full((rows, columns, 3), (255, 255, 255), dtype=np.uint8)

# Set the black squares (0, 0, 0)
checkerboard[1::2, ::2] = [0, 0, 0]
checkerboard[::2, 1::2] = [0, 0, 0]

# Display the checkerboard
plt.imshow(checkerboard)
plt.axis('off')  # Turn off axis labels and ticks
plt.show()

width, height = 100, 100  # Dimensions of the array
radius = 10  # Radius of the circle
# Create an empty array filled with zeros
circle = np.zeros((height, width), dtype=np.uint8)

# Calculate the center of the circle
center_x, center_y = width // 2, height // 6

# Set points inside the circle to 1
for y in range(height):
    for x in range(width):
        if (x - center_x) ** 2 + (y - center_y) ** 2 <= radius ** 2:
            circle[y, x] = 1

import matplotlib.pyplot as plt

plt.imshow(circle, cmap='gray', origin='upper')
plt.axis('off')  # Turn off axis labels and ticks
plt.show()