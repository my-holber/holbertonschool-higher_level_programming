def divisible_by_2(my_list=[]):
    _result = []
    for i in my_list[:]:
        if (i % 2 == 0):
            _result.append(True)
        else:
            _result.append(None)
    return (_result)
