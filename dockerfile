FROM python:3

Run pip install -r requirements.txt
COPY . .
RUN python manage.py migrate
EXPOSE 8001
CMD ["python", "manage.py","runserver","0.0.0.0:8001"]