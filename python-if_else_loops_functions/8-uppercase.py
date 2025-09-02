#!/usr/bin/python3

def uppercase(str):
    result = ""
    for i in range (len(str)):
        j = str[i]
        code_ascii = ord(j)
        if code_ascii >= 97 and code_ascii < 123:
            code_ascii -= 32
        result += chr(code_ascii)
    
    print("{}".format(result))
