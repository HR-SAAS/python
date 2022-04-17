FROM python:3.8

WORKDIR /code/message_srv
COPY requirements.txt /code/message_srv/requirements.txt
RUN pip install -r requirements.txt -i https://pypi.doubanio.com/simple

ADD ./ /code/message_srv

CMD ["python", "/code/message_srv/server.py"]