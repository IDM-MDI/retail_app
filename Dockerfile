FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirements.txt /code/

RUN pip install -r requirements.txt

COPY . /code/

CMD bash -c "python manage.py makemigrations && python manage.py migrate && python manage.py createsuperuser --noinput && python manage.py populate_fake_data && python manage.py runserver 0.0.0.0:8000"
