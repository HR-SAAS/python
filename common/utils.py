import socket


def sortByMap(model, m):
    if m is not None:
        sort = []
        for i, v in dict(m).items():
            sort.append(f"{i} {v}")
        model.order_by(",".join(sort))
    return model


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


def build_model_filters(model, search: dict, extra_columns=None):
    if extra_columns is None:
        extra_columns = {}
    filters = []
    if search:
        for field, v in search.items():
            value = v.split(" ")
            op = "="
            query = value[0]
            if len(value) > 1:
                op = value[0]
                query = value[1]
            # The field exists as an exposed column
            if model.__mapper__.has_property(field):
                column = getattr(model, field)
                _filter = column.op(op)(query)
                filters.append(_filter)
            else:
                if field in extra_columns:
                    column = extra_columns[field]
                    _filter = column.op(op)(query)
                    filters.append(_filter)
    return filters
