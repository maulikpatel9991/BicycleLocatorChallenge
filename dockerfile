FROM python:3

# Copy requirements.txt file
COPY requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install -r /app/requirements.txt
COPY . .
RUN python manage.py migrate
EXPOSE 8001
CMD ["python", "manage.py","runserver","0.0.0.0:8001"]