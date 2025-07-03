from flask import Flask, request, jsonify
from flask_cors import CORS  # Add this line
import joblib

app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests

model = joblib.load("lymphography_model.joblib")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    print(" Received data:", data)
    
    try:
        input_data = [[
            int(data['lymphatics']),
            int(data['block_of_afferent_lymphatic']),
            int(data['bl_of_lymph_c'])
        ]]
        prediction = model.predict(input_data)
        return jsonify({'prediction': int(prediction[0])})
    except Exception as e:
        print(" ERROR:", str(e))
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)