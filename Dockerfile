FROM python:3.7-slim

WORKDIR /app

COPY . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt
RUN apt-get -y update
RUN apt-get -y install wget wkhtmltopdf xz-utils libfontconfig1 libxrender1
RUN cd ~
RUN wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.3/wkhtmltox-0.12.3_linux-generic-amd64.tar.xz
RUN tar vxf 'wkhtmltox-0.12.3_linux-generic-amd64.tar.xz'
RUN cp wkhtmltox/bin/wk* /usr/local/bin/

RUN useradd -m user
USER user

EXPOSE $PORT

ENV NAME World

CMD ["python", "app.py"]
