FROM python:3.8

ADD ./ /code
#设置code文件夹是工作目录
WORKDIR /code
#安装支持
RUN pip install -r requirements.txt

CMD ["python", "/code/server.py"]