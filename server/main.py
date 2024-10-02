from heatmap import generate_heatmap
from feature_extraction import extract_image_features

def analyze_thermal_image(image_path):
    print(f"Analyzing thermal image: {image_path}")

    # Step 1: Generate heatmap using OpenCV
    print("Generating heatmap...")
    heatmap_file = generate_heatmap(image_path)
    print(f"Heatmap saved at: {heatmap_file}")

    # Step 2: Extract features using Scikit-Image
    print("Extracting image features...")
    features = extract_image_features(image_path)

    # Display the extracted features
    print("\nImage Analysis Results:")
    print(f"Number of Regions Detected: {features['num_regions']}")
    print(f"Mean Intensity: {features['mean_intensity']:.2f}")

if __name__ == "__main__":
    # Example thermal image path
    image_path = "sample_data/images.jpg"
    analyze_thermal_image(image_path)
