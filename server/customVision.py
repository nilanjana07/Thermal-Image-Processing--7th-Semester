from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials

# Set your Custom Vision API credentials
prediction_key = ""
endpoint = ""

# Initialize the Custom Vision client
credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
predictor = CustomVisionPredictionClient(endpoint, credentials)

# Set the project ID and model iteration ID from the Custom Vision project
project_id = ""
model_iteration = ""

# Upload the thermal image for anomaly detection
image_path = "thermal_image.jpg"
with open(image_path, "rb") as image_data:
    results = predictor.classify_image(project_id, model_iteration, image_data.read())

# Analyze the results
for prediction in results.predictions:
    print(f"{prediction.tag_name}: {prediction.probability * 100:.2f}% confidence")
