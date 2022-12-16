FROM python:3.8-slim
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY . /code/
RUN pip install -r requirements.txt
RUN python manage.py collectstatic 
RUN python manage.py makemigrations
RUN python manage.py migrate

#CMD ["gunicorn", "--bind", "0.0.0.0:8000", "CheckMechBackend.wsgi"]
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]