def multiplication(*args):
    result = 1

    for num in args:
        result *= num

    return result

def add(*args):
    result = 0

    for num in args:
        result += num

    return result

power_to = lambda x, y : x ** y