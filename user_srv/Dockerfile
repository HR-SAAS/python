FROM python:3.8

ADD ./ /code/user_srv
#设置code文件夹是工作目录
WORKDIR /code/user_srv
#安装支持
RUN pip install -r requirements.txt -i https://pypi.doubanio.com/simple

CMD ["python", "/code/server.py"]