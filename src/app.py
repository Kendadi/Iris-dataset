from flask import Flask
from flask import request
from inference import main
import os

# {
#   "prediction": "" // The predicted iris type between "setosa", "versicolour" or "virginica"
# }
FEATURE_NAMES = set(['petal_length', 'petal_width', 'sepal_length', 'sepal_width'])
map_ = {i: os.environ[f"LABEL_{i}"] for i in range(3)}

app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
    """
    Gets the inputs from post request
    Calls main function from inference module to get model prediction over input
    :return: array response which contains prediction over each data entry
    """

    # get request data
    feature_dict = request.get_json()

    # return input error if empty json
    if not feature_dict:
        return {
                   'input error': 'Body is empty.'
               }, 500

    # return input error if missing feature
    assert FEATURE_NAMES.issubset(set(feature_dict.keys())), {'input error': 'your input is incomplete'}

    # make prediction
    response = main(**feature_dict)

    # return model error if model output is empty or not in the correct format
    assert type(response) == list, {'model error': 'wrong prediction format'}
    assert len(response) > 0, {'model error': 'empty prediction'}

    return {"prediction": map_[response[0]]}


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
