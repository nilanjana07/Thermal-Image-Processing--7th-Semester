import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import os

# Load grayscale image and apply color map
def apply_colormap(image_path, colormap_type):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise ValueError(f"Image at {image_path} not found.")
    
    # Apply chosen colormap
    colormap_dict = {
        "JET": cv2.COLORMAP_JET,
        "HOT": cv2.COLORMAP_HOT,
        "COOL": cv2.COLORMAP_COOL,
        
    }

    if colormap_type in colormap_dict:
        if isinstance(colormap_dict[colormap_type], int):  # OpenCV colormaps
            color_image = cv2.applyColorMap(image, colormap_dict[colormap_type])
        else:  # Matplotlib colormaps
            color_image = cm.ScalarMappable(cmap=colormap_dict[colormap_type]).to_rgba(image)[:, :, :3] * 255
            color_image = color_image.astype(np.uint8)
    else:
        raise ValueError("Unsupported colormap type. Choose from 'JET', 'HOT', 'COOL', 'RAINBOW', 'MAGMA', 'VIRIDIS'.")
    
    return color_image

# Save the heatmap images with the specified colormap
def save_colored_images(input_folder, output_folder, colormap_list):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image_path = os.path.join(input_folder, filename)
            for cmap in colormap_list:
                heatmap_image = apply_colormap(image_path, cmap)
                output_path = os.path.join(output_folder, f"{filename.split('.')[0]}_{cmap}.jpg")
                cv2.imwrite(output_path, heatmap_image)
                print(f"Saved: {output_path}")

# Example usage
input_folder = "greyscalenew"  # Folder containing grayscale thermal images
output_folder = "heatmap_images_new"   # Folder to save generated heatmaps
colormap_list = ["JET", "HOT", "COOL"]  # Choose desired color maps

# Generate and save heatmaps
save_colored_images(input_folder, output_folder, colormap_list)
