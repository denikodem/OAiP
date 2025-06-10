def max_num(lst):
    if len(lst) == 1:
        return lst
    else:
        max_rest = max_num(lst[1:])
        return lst if lst > max_rest else max_rest
