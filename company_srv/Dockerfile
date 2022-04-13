FROM python:3.8

WORKDIR /code/company_srv
COPY requirements.txt /code/company_srv/requirements.txt
RUN pip install -r requirements.txt -i https://pypi.doubanio.com/simple

ADD ./ /code/company_srv

CMD ["python", "/code/company_srv/server.py"]