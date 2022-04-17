FROM python:3.8

WORKDIR /code/tag_srv
COPY requirements.txt /code/tag_srv/requirements.txt
RUN pip install -r requirements.txt -i https://pypi.doubanio.com/simple

ADD ./ /code/tag_srv

CMD ["python", "/code/tag_srv/server.py"]