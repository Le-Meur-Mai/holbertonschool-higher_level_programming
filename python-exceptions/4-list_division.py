#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):

    new_list = []
    for i in range(0, list_length):
        error = 0
        try:
            result = my_list_1[i] / my_list_2[i]
            new_list.append(result)
        except (ZeroDivisionError, TypeError, IndexError):

            if len(my_list_1) <= i or len(my_list_2) <= i:
                error += 1
                print("out of range")
            else:
                if (not isinstance(my_list_1[i], (float, int)) or
                    not isinstance(my_list_2[i], (float, int))):
                    error += 1
                    print("wrong type")
                if my_list_2[i] == 0:
                    error += 1
                    print("division by 0")
        finally:
            if error != 0:
                new_list.append(0)
    return (new_list)
