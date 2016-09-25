# todo: Use python's built in serializer

def retrieve(filename):
    with open(filename) as fh:
        return data_from_string(fh.read())

def string_from_data(data):
    return '\n'.join(data)

def data_from_string(s):
    return s.split('\n')