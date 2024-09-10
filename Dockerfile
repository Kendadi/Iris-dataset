FROM Ubuntu 20.04



COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt


COPY src/app.py ./src/api.py
COPY src/inference.py ./src/inference.py

