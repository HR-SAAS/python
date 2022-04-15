FROM python:3.8

WORKDIR /code/resume_srv
COPY requirements.txt /code/resume_srv/requirements.txt
RUN pip install -r requirements.txt -i https://pypi.doubanio.com/simple

ADD ./ /code/resume_srv

CMD ["python", "/code/resume_srv/server.py"]