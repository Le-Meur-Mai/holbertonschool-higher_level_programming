#!/usr/bin/python3

def safe_print_division(a, b):

    try:
        result = -1
        result = a / b
    except ZeroDivisionError:
        result = -1
    finally:
        print("Inside result: ", end="")
        if result == -1:
            print("{}".format(None))
        else:
            print("{}".format(result))
            return (result)
