flag = True


def times(x, y):
    global flag
    return x * y if flag else 1


print(times(5, 8))
