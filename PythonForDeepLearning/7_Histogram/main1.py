import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('images/tobago.jpg')

# Viewing Separate Color Channels
color = ('b', 'g', 'r')

# Create a figure to hold the subplots
fig = plt.figure()

for i, col in enumerate(color):
    # Calculate the histogram for the current channel
    histogram2 = cv2.calcHist([image], [i], None, [256], [0, 256])
    
    # Create a subplot for each channel
    plt.subplot(3, 1, i + 1)
    
    # Plot the histogram
    plt.plot(histogram2, color=col)
    plt.xlim([0, 256])
    
    # Add titles and labels for each subplot
    plt.title(f'Histogram of {col.upper()} Channel')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')

# Adjust the layout of the subplots
plt.tight_layout()

# Save the figure with subplots as a single image
plt.savefig('color_histograms.png')

# Show the entire figure with all three subplots
plt.show()
