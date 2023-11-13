FROM python:3.9-alpine

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

#WORKDIR /code/app
#RUN python3 -c 'import services; services._add_tables()'

#WORKDIR /code
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]