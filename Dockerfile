FROM python:3.6-alpine
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD gunicorn --workers 4 --bind 0.0.0.0:5000 website.__main__:app
