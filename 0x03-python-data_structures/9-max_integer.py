
def max_integer(my_list=[]):
    max_num = 0
    list_len = len(my_list)
    i = 0

    if list_len == 0:
        return None
    while i < (list_len - 1):
        if my_list[i] > max_num:
            max_num = my_list[i]
        i += 1
    return max_num
        