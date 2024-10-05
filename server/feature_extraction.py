from skimage import io, filters, measure
import matplotlib.pyplot as plt
import numpy as np

# Define temperature thresholds and conditions
TEMP_CONDITIONS = {
    "low_temp": {
        "threshold": 0.3,  # Temperatures below this might indicate hypothermia or poor circulation
        "condition": "Cold regions detected - May indicate poor blood circulation or hypothermia."
    },
    "normal_temp": {
        "threshold": 0.4,  # Temperatures within this range are considered normal
        "condition": "Normal temperature - No abnormalities detected."
    },
    "high_temp": {
        "threshold": 0.5,  # Temperatures above this may indicate inflammation or infection
        "condition": "Hot regions detected - May indicate inflammation, infection, or inflammation-related conditions."
    }
}

def classify_temperature(region_mean_intensity):
    """
    Classifies the region's mean intensity (temperature) and returns the condition.
    """
    if region_mean_intensity < TEMP_CONDITIONS["low_temp"]["threshold"]:
        return TEMP_CONDITIONS["low_temp"]["condition"]
    elif TEMP_CONDITIONS["low_temp"]["threshold"] <= region_mean_intensity <= TEMP_CONDITIONS["normal_temp"]["threshold"]:
        return TEMP_CONDITIONS["normal_temp"]["condition"]
    else:
        return TEMP_CONDITIONS["high_temp"]["condition"]

def extract_image_features(image_path):
    """
    Analyze thermal image for features and classify regions based on temperature thresholds.
    """
    # Load the thermal image
    img = io.imread(image_path, as_gray=True)

    if img is None:
        raise ValueError(f"Image not found at {image_path}")

    # Apply edge detection (e.g., Sobel filter)
    edges = filters.sobel(img)

    # Label distinct regions in the image
    labeled_image, num_regions = measure.label(edges > 0.1, background=0, return_num=True)

    # Calculate the region properties (e.g., area, centroid)
    regions = measure.regionprops(labeled_image)

    # Calculate mean intensity of the entire thermal image
    mean_intensity = np.mean(img)

    # Lists to store condition results
    conditions = {
        "cold": [],
        "normal": [],
        "hot": []
    }

    # Analyze each region
    for region in regions:
        # Calculate the mean intensity for the region
        region_mean_intensity = np.mean(img[region.coords[:, 0], region.coords[:, 1]])
        
        # Classify the region based on its temperature and store the corresponding condition
        condition = classify_temperature(region_mean_intensity)
        print(f"Region with mean temperature {region_mean_intensity *100 : }°C classified as: {condition}")
        
        # Append to appropriate list for further analysis or summary
        if condition == TEMP_CONDITIONS["low_temp"]["condition"]:
            conditions["cold"].append(region)
        elif condition == TEMP_CONDITIONS["normal_temp"]["condition"]:
            conditions["normal"].append(region)
        else:
            conditions["hot"].append(region)

    # Display the overall analysis results
    print("\nImage Analysis Results:")
    print(f"Number of regions detected: {num_regions}")
    print(f"Mean intensity of the entire image: {mean_intensity *100 + 7:}°C")
    print(f"Cold regions: {len(conditions['cold'])} - May indicate poor circulation or hypothermia.")
    print(f"Normal regions: {len(conditions['normal'])} - No abnormalities detected.")
    print(f"Hot regions: {len(conditions['hot'])} - May indicate inflammation or infection.")

    # Plot the original image and the edge-detected image
    fig, ax = plt.subplots(1, 2, figsize=(10, 5))
    
    ax[0].imshow(img, cmap='gray')
    ax[0].set_title("Original Thermal Image")
    ax[0].axis('off')

    ax[1].imshow(edges, cmap='gray')
    ax[1].set_title("Edge Detection (Sobel)")
    ax[1].axis('off')

    plt.show()

    return conditions

# Example usage
if __name__ == "__main__":
    extract_image_features("sample_data/humanfeet.jpg")

