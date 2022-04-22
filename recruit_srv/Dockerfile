FROM python:3.8

WORKDIR /code/recruit_srv
COPY requirements.txt /code/recruit_srv/requirements.txt
RUN pip install -r requirements.txt -i https://pypi.doubanio.com/simple

ADD ./ /code/recruit_srv

CMD ["python", "/code/recruit_srv/server.py"]