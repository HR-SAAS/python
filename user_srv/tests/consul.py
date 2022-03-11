import requests

host = "http://localhost:9001"


def register(id, name, address, port):
    rsp = requests.put(host + '/v1/agent/service/register', json={
        "Name": name,
        "ID": id,
        "Tags": ["123", "456"],
        "Address": address,
        "Port": port,
        "Check": {
            "Name": name,
            "GRPC": f"{address}:{port}",
            "Interval": "5s",
            "Timeout": "5s",
            "Method": "get",
            "DeregisterCriticalServiceAfter": "5s"
        }
    })
    if rsp.status_code == 200:
        print("注册成功")
    else:
        print("注册失败", rsp.text)


def deregister(id):
    rsp = requests.put(host + f'/v1/agent/service/deregister/{id}')
    if rsp.status_code == 200:
        print("注销成功")
    else:
        print("注销失败", rsp.text)


def filter_service(f):
    rsp = requests.get(host + f'/v1/agent/services', params={
        "filter": f
    })
    if rsp.status_code == 200:
        print("成功",rsp.json())
    else:
        print("失败", rsp.text)


if __name__ == "__main__":
    # register("user-srv", "user-srv", "192.168.159.119", 5001)
    # deregister("wm")
    filter_service('Service == "用户服务" ')
