# Version 0.0.4
FROM ubuntu:12.04
MAINTAINER Mike Bartoli "michael.bartoli@pomona.edu"
RUN apt-get update
RUN apt-get -y install \
	python \
	build-essential \
	python-dev \
	python-pip \
	wget \
	unzip \
	git \
	python-setuptools
RUN sudo apt-get install -y python-Levenshtein make libmysqlclient-dev python-mysqldb python-pip python-zmq python-numpy gfortran libopenblas-dev liblapack-dev g++ sqlite3 libsqlite3-dev python-sqlite redis-server

WORKDIR /home
RUN git clone https://github.com/mbartoli/patentprocessing
WORKDIR /home/patentprocessing 

RUN pip install -r requirements.txt


RUN unzip patentprocessor.zip

