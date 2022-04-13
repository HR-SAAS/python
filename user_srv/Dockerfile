FROM python:3.8

WORKDIR /code/user_srv
COPY requirements.txt /code/user_srv/requirements.txt
RUN pip install -r requirements.txt -i https://pypi.doubanio.com/simple

ADD ./ /code/user_srv
#设置code文件夹是工作目录
#安装支持

CMD ["python", "/code/user_srv/server.py"]