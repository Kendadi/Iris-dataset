# MaintainX - Take Home Assessment Applied Machine Learning Engineer

The goal of this take home assessment is to evaluate your machine learning knowledge and your software development skills.

## Task

Your task for this assessment is to train a model and expose it's inference function through an HTTP API. The choice of the model is yours.

The dataset to use is the [iris dataset](https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html) from scikit-learn.

The main thing we are looking at is how you structured your code and your thought process. We will not be looking at how performant the model is. This will be used as a conversation starter during the in person interview.

**You must commit and push your changes to the repo at least 1h before the live interview.**

## Requirement

Your API will be need to follow theses requirements:

`HTTP POST /predict`

Request:

```json
{
  "sepal_length": 0.0, // float representing the sepal length in cm
  "sepal_width": 0.0, // float representing the sepal width in cm
  "petal_length": 0.0, // float representing the petal length in cm
  "petal_width": 0.0 // float representing the petal width in cm
}
```

Response

```json
{
  "prediction": "" // The predicted iris type between "setosa", "versicolour" or "virginica"
}
```

## Testing

We have joined a postman collection and a bash script depending on your preference to test your API. Feel free to edit them to match your API's config (ex.: port, host, etc.).

## --------------------------------------------------------------------------------------

## Run project 
To run this application please follow these steps : 

build docker image : 
```bash
docker build -t iris_api .
```
run the docker container : 
```bash
docker run -it -p 5000:5000 iris_api python3 /src/app.py
```

Example of output : 
![alt text](inference%20result.png)
