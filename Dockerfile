FROM python:3.7-slim

WORKDIR /app

COPY . /app

RUN apt-get -y update
RUN apt-get -y install wkhtmltopdf

RUN pip install --trusted-host pypi.python.org -r requirements.txt

RUN useradd -m user
USER user

EXPOSE $PORT

ENV NAME World

CMD ["python", "app.py"]
