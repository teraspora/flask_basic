# syntax=docker/dockerfile:1

FROM python:latest
COPY ./requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt
WORKDIR /app
COPY . .
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
