FROM python3.8-slim-buster
RUN apt update -y && apt install awscli -y
# Create app folder and copy all files and source codes into app folder
WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt
RUN pip install --upgrade accelerate
RUN pip install transformers accelerate

CMD ["python3", "app.py"]
