import socket


def get_free_tcp_port():
    # 获取
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp.bind(("", 0))
    _, port = tcp.getsockname()
    tcp.close()
    return port


def get_ip_addr():
    host_name = socket.gethostname()
    host = socket.gethostbyname(host_name)
    return host
