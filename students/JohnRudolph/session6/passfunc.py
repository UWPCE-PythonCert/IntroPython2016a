def size_func(fib, lfib):
    if fib % 2 == 0:
        size = 'medium'
    else:
        if lfib % 2 == 0:
            size = 'large'
        else:
            size = 'small'
    return size


def list_pop(fib_list, size_list):
    list_len = len(fib_list)
    for i in range(3):
        indx = i + list_len
        fib_list.append(fib_list[indx - 2]+fib_list[indx - 1])
        size_list.append(size_func(fib_list[indx], fib_list[indx - 1]))
    return fib_list[list_len:], size_list[list_len:]


def hand_weapon():
    fib_list = list(range(2))
    size_list = []
    for i in range(3):
            fib_list.append(fib_list[i]+fib_list[i+1])
            size_list.append(size_func(fib_list[i + 2], fib_list[i + 1]))
    return fib_list[2:], size_list


def gun():
    fib_list, size_list = hand_weapon()
    return list_pop(fib_list, size_list)


def flower_power():
    fib_list, size_list = gun()
    return list_pop(fib_list, size_list)


def score(weapon_type, weapon_size):
    fib_list, size_list = weapon_type()
    return fib_list[size_list.index(weapon_size)]
