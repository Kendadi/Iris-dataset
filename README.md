
## Requirement

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
