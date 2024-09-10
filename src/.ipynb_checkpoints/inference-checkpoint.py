import click
import numpy as np 
import pickle as pkl

from pathlib import Path
# {
#   "sepal_length": 0.0, // float representing the sepal length in cm
#   "sepal_width": 0.0, // float representing the sepal width in cm
#   "petal_length": 0.0, // float representing the petal length in cm
#   "petal_width": 0.0 // float representing the petal width in cm
# }

@click.command()
@click.option("--sepal_length", "-sl", type="float")
@click.option("--sepal_width", "-sw", type="float")
@click.option("--petal_length","pl", type="float")
@click.option("--petal_width", "pw", type="float")
def main(sepal_length, sepal_width, petal_length, petal_width) : 
    """
    load train model
    make prediction 
    stdout prediction in json format
    """

    # load trained model
    with open("../models/rdf.pkl", "rb") as f: 
        rdf = pkl.load(f)

    # predict label
    label = rdf.predict([[sepal_length, sepal_width, petal_length, petal_width]]))


    print({"prediction" : label[0]})
    
    
    
    

