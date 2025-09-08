#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    new_list = []
    for i in range(0, 2):
        if i < len(tuple_a):
            new_list.append(tuple_a[i])
        else:
            new_list.append(0)
    for i in range(0, 2):
        if i < len(tuple_b):
            new_list.append(tuple_b[i])
        else:
            new_list.append(0)

    new_tuple = ((new_list[0] + new_list[2]), (new_list[1] + new_list[3]))
    return (new_tuple)
