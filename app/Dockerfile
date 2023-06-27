FROM python:3.10

ADD . /www/
WORKDIR /www
RUN pip install -r ./reqirments/reqirments.txt
CMD [ "gunicorn", "--config", "gunicorn.config", "app:app" ]
