#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return
    else:
        score = 0
        for i in a_dictionary:
            if a_dictionary[i] > score:
                score = a_dictionary[i]
        for i in a_dictionary:
            if a_dictionary[i] == score:
                best_student = i
                break
    return (best_student)
