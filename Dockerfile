FROM madhuravius/baltimore-backend-python-base

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV CPLUS_INCLUDE_PATH /usr/include/gdal
ENV C_INCLUDE_PATH /usr/include/gdal

WORKDIR /usr/src/app

COPY ./requirements.txt /usr/src/app
RUN pip3 install -r requirements.txt

COPY . /usr/src/app
EXPOSE 8000