FROM alpine/git as clone

WORKDIR /app

RUN git clone https://github.com/hcsekhar/nursery-project.git

FROM python:3.8

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", 0.0.0.0:8000"]
