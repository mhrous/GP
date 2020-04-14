def func1(obj):
    return obj


def func2(obj):
    return obj


def post_processing(obj):
    res_1 = func1(obj)
    res_2 = func2(res_1)

    return res_2
