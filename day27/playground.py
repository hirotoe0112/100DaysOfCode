def add(*args):
    print(args)
    return sum(args)


print(add(1, 2, 34, 4, 5, 6, 75, 3, 5, 3))


def calculate(**kwargs):
    print(kwargs)


calculate(add=3, multiply=5)
