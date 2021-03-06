import os
from datetime import datetime
import time

def format_datetime(dt):
    return dt.strftime('%Y-%m-%d %H:%M:%S')

def format_date(dt):
    return dt.strftime('%Y-%m-%d')

def format_time_ms(float_time):
    local_time = time.localtime(float_time)
    data_head = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
    data_secs = (float_time - int(float_time)) * 1000
    return "%s.%03d" % (data_head, data_secs)


def get_parameter(kwargs, key, default=None):
    """ Get a specified named value for this (calling) function

    The parameter is searched for in kwargs

    :param kwargs: Parameter dictionary
    :param key: Key e.g. 'max_workers'
    :param default: Default value
    :return: result
    """

    if kwargs is None:
        return default

    value = default
    if key in kwargs.keys():
        value = kwargs[key]
    return value
    
def to_int(s, default_value = 0):
    try:
        return int(s)
    except:
        return default_value


def singleton(cls):
    _instance = {}

    def inner():
        if cls not in _instance:
            _instance[cls] = cls()
        return _instance[cls]
    return inner

def create_dir(root_dir, sub_system, time_str: list):
    the_dir = os.path.join(root_dir, sub_system, time_str)
    if not os.path.exists(the_dir):
        os.makedirs(os.path.join(root_dir, sub_system, time_str))
    return the_dir

def yield_file_bytes(full_file_path, chunk_size):
    if not os.path.exists(full_file_path):
        raise Exception("%s file not found" %(full_file_path))
    
    with open(full_file_path, 'rb') as f:
        while True:
            data = f.read(chunk_size)
            if not data:
                break
            yield data