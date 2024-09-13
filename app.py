from flask import Flask, request, jsonify, send_file
import os
from thermal_image_processing import ThermalImageProcessor

app = Flask(__name__)

# Create a folder for uploading images
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/process-image', methods=['POST'])
def process_image():
    """
    Endpoint to upload a thermal image and return the stress level and heatmap.
    """
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400

    file = request.files['image']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Save the uploaded image to the upload folder
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(image_path)
    
    try:
        # Create an instance of the thermal image processor
        processor = ThermalImageProcessor(image_path)
        
        # Process the image: get the stress level and generate the heatmap
        stress_level = processor.process_image()
        
        # Return the stress level as a response
        response = {
            'stress_level': round(stress_level, 2),
            'message': 'Thermal image processed successfully. Heatmap generated.'
        }
        
        return jsonify(response), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/heatmap/<filename>', methods=['GET'])
def get_heatmap(filename):
    """
    Endpoint to retrieve the heatmap generated for the thermal image.
    """
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(image_path):
        return send_file(image_path, mimetype='image/jpeg')
    else:
        return jsonify({'error': 'Heatmap not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
