FROM ubuntu:22.04

# Set feature names as env variables
ENV LABEL_0=setosa
ENV LABEL_1=versicolor
ENV LABEL_2=virginica
# Set model path
ENV MODEL_PATH=./models/rdf.pkl

# Install pip
RUN apt-get update
RUN apt-get install -y python3-pip

# Install requirements
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt


COPY src/app.py ./src/app.py
COPY src/inference.py ./src/inference.py
COPY models/rdf.pkl ./models/rdf.pkl

EXPOSE 5000
