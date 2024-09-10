from inference import main
from flask import Flask
from flask import request
from inference import main

app = Flask(__name__)






@app.route('/predict', methods=['POST'])
def predict():
    feature_dict = request.get_json()
    if not feature_dict:
        return {
            'error': 'Body is empty.'
        }, 500

    
    response = main(**feature_dict)

    return response, 200



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')