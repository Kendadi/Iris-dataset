import pickle as pkl
import os

# {
#   "sepal_length": 0.0, // float representing the sepal length in cm
#   "sepal_width": 0.0, // float representing the sepal width in cm
#   "petal_length": 0.0, // float representing the petal length in cm
#   "petal_width": 0.0 // float representing the petal width in cm
# }

MODEL_PATH = os.environ["MODEL_PATH"]

def main(sepal_length: float, sepal_width: float, petal_length: float, petal_width: float) -> list:
    """
    load trained model
    make prediction 
    stdout prediction in json format
    :return: label list
    """

    # load trained model
    with open(MODEL_PATH, "rb") as f:
        rdf = pkl.load(f)

    # predict label
    label = rdf.predict([[sepal_length, sepal_width, petal_length, petal_width]])

    print({"prediction": label[0]})
    return label.tolist()
