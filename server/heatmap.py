import cv2
import numpy as np
import matplotlib.pyplot as plt

def generate_heatmap(image_path):
    # Read the thermal image (assumed to be grayscale)
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if img is None:
        raise ValueError(f"Image not found at {image_path}")

    # Apply a colormap to the grayscale image to create a heatmap
    heatmap = cv2.applyColorMap(img, cv2.COLORMAP_JET)

    # Save the heatmap image
    heatmap_file = image_path.replace(".jpg", "_heatmap.jpg")
    cv2.imwrite(heatmap_file, heatmap)

    # Display the heatmap
    plt.imshow(heatmap)
    plt.title("Thermal Image Heatmap")
    plt.axis('off')
    plt.show()

    return heatmap_file

# Example usage
if __name__ == "__main__":
    generate_heatmap(r"sD:\Thermal Image Processing- 7th Semester\images.jpg")
