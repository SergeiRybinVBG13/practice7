one_list = [10, 12, -56, -99, 2, -98, 34, -55, 1, -8]


def find_pos(x):
    return x > 0


list_pos = list(filter(find_pos, one_list))
print(min(list_pos))
