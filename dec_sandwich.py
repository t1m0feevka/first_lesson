def bread_top(func):
    def wrapper():
        print("\033[30m\033[1m {}".format("/¯¯¯¯¯¯¯¯¯\ "))
        func()
    return wrapper


def ingr(func):
    def wrapper():
        func()
        print("\033[0m\033[31m {}".format('--Tomatoes--'))
        print("\033[32m {}".format(' --Salad--'))
    return wrapper


def bread_bottom(func):
    def wrapper():
        func()
        print("\033[30m\033[1m {}".format('\_________/'))
    return wrapper


@bread_bottom
@ingr
@bread_top
def sandwich(food='--Sausage--'):
    print("\033[0m\033[33m {}".format(food))


sandwich()

