FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /project
WORKDIR /project
ADD requirements.txt /project/
RUN pip install --upgrade pip && pip install -r requirements.txt
RUN apt-get update && apt install nodejs -y && apt install npm -y
RUN npm install -g @vue/cli
ADD . /project/
EXPOSE 8080
EXPOSE 8000
