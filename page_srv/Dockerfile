FROM python:3.8

WORKDIR /code/page_srv
COPY requirements.txt /code/page_srv/requirements.txt
RUN pip install -r requirements.txt -i https://pypi.doubanio.com/simple

ADD ./ /code/page_srv

CMD ["python", "/code/page_srv/server.py"]