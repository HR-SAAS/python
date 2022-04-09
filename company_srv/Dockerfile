FROM python:3.8

ADD ./ /code/company_srv
#设置code文件夹是工作目录
WORKDIR /code/company_srv
#安装支持
RUN pip install -r requirements.txt -i https://pypi.doubanio.com/simple

CMD ["python", "/code/company_srv/server.py"]