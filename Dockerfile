FROM alpine/git as clone

WORKDIR /app

RUN git clone https://github.com/hcsekhar/nursery-project.git

FROM python:3.8

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

CMD ["python", "manage.py", "runserver"]
