FROM python:3.7.3-slim-stretch

RUN apt update
RUN apt install -y python3-numpy python3-scipy python3-matplotlib python3-pandas python3-gdal python3-lxml gdal-bin libgdal-dev libsqlite3-mod-spatialite libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev build-essential checkinstall

WORKDIR /usr/src/app

COPY ./requirements-deps.txt /usr/src/app
RUN pip3 install -r requirements-deps.txt
