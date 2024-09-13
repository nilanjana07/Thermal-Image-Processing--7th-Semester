import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

class ThermalImageProcessor:
    def __init__(self, image_path):
        self.image_path = image_path
        self.thermal_image = None
        self.preprocessed_image = None

    def load_image(self):
        """
        Load the thermal image from the specified path.
        """
        try:
            self.thermal_image = cv2.imread(self.image_path, cv2.IMREAD_GRAYSCALE)
            if self.thermal_image is None:
                raise ValueError("Image not found or invalid format.")
            print(f"Loaded image: {self.image_path}")
        except Exception as e:
            print(f"Error loading image: {e}")
    
    def preprocess_image(self):
        """
        Preprocess the image (e.g., resize, normalize).
        """
        if self.thermal_image is None:
            raise ValueError("Thermal image is not loaded.")
        
        # Resize the image (optional step)
        self.preprocessed_image = cv2.resize(self.thermal_image, (256, 256))

        # Normalize pixel values to the range [0, 1]
        scaler = MinMaxScaler()
        self.preprocessed_image = scaler.fit_transform(self.preprocessed_image)
        
        print("Preprocessed image.")

    def predict_stress_level(self):
        """
        Dummy function to predict stress level based on thermal image analysis.
        """
        if self.preprocessed_image is None:
            raise ValueError("Preprocessed image is not available.")

        # For demonstration purposes, let's assume a random stress level between 1 and 10.
        stress_level = np.random.uniform(1, 10)
        
        # A real model would use image features to predict stress (e.g., a CNN).
        print(f"Predicted Stress Level: {stress_level:.2f}")
        return stress_level

    def generate_heatmap(self):
        """
        Generate a heatmap based on the temperature variations in the thermal image.
        """
        if self.preprocessed_image is None:
            raise ValueError("Preprocessed image is not available.")
        
        plt.imshow(self.preprocessed_image, cmap='jet')
        plt.colorbar(label='Temperature Variation')
        plt.title('Thermal Image Heatmap')
        plt.show()

    def process_image(self):
        """
        Full pipeline to process the thermal image: load, preprocess, predict stress, generate heatmap.
        """
        self.load_image()
        self.preprocess_image()
        stress_level = self.predict_stress_level()
        self.generate_heatmap()
        return stress_level


# Example Usage
if __name__ == "__main__":
    # Replace 'path_to_image.jpg' with the actual path to the thermal image.
    image_path = 'path_to_image.jpg'
    
    # Create an instance of the ThermalImageProcessor
    processor = ThermalImageProcessor(image_path)
    
    # Process the thermal image
    stress_level = processor.process_image()
    
    # You can now use the stress level in your application logic
    print(f"Final Stress Level: {stress_level:.2f}")
