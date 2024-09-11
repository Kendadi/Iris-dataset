FROM ubuntu:22.04
COPY requirements.txt ./requirements.txt
RUN apt-get update
RUN apt-get install -y python3-pip
RUN pip install -r requirements.txt
COPY src/app.py ./src/app.py
COPY src/inference.py ./src/inference.py
COPY models/rdf.pkl ./models/rdf.pkl

EXPOSE 5000
