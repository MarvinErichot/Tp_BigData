FROM python:3.8-slim

WORKDIR /Tp_BigData

COPY . /Tp_BigData

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

ENV FLASK_APP=app.py

CMD ["python", "app.py"]
