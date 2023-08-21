FROM python:3.10


RUN mkdir /test_app

WORKDIR /test_app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN python manage.py migrate

RUN python manage.py loaddata fixtures/dump.json

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


