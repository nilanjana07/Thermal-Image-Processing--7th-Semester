import cv2
import numpy as np
import matplotlib.pyplot as plt

def color_to_grayscale(image_path, output_path):
    # Read the color heatmap image
    color_image = cv2.imread(image_path)
    
    # Convert the color image to grayscale
    grayscale_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)
    
    # Save the grayscale image to the specified output path
    cv2.imwrite(output_path, grayscale_image)
    
    # Display the original and grayscale images for comparison
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.title('Original Color Heatmap')
    plt.imshow(cv2.cvtColor(color_image, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    
    plt.subplot(1, 2, 2)
    plt.title('Converted Grayscale Image')
    plt.imshow(grayscale_image, cmap='gray')
    plt.axis('off')
    
    plt.show()

# Example usage
color_to_grayscale("new high 1.png", "graynewhigh1.jpg")
