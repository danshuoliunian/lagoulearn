# coding:utf-8

# 封装常量获取方法

class global_vae:
    # case_id
    Id = '0'
    request_name = '1'
    url = '2'
    run = '3'
    request_way = '4'
    header = '5'
    case_depend = '6'
    data_depend = '7'
    field_depend = '8'
    data = '9'
    expect = '10'
    result = '11'


# 获取caseid
def get_id():
    return global_vae.Id


# 获取url
def get_url():
    return global_vae.url


def get_run():
    return global_vae.run


def get_run_way():
    return global_vae.request_way


def get_header():
    return global_vae.header


def get_case_depend():
    return global_vae.case_depend


def get_data_depend():
    return global_vae.data_depend


def get_field_depend():
    return global_vae.field_depend


def get_data():
    return global_vae.data


def get_expect():
    return global_vae.expect


def get_result():
    return global_vae.result


def get_header_value():
    header = {
        "header": "1234",
        "cookie": "Mushihsi"
    }
