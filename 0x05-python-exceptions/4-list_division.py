#!/usr/bin/python3
# 4-list_division.py

def list_division(list_one, list_two, lth):
    temp_lst = []
    for i in range(0, lth):
        try:
            sm = list_one[i] / list_two[i]
        except TypeError:
            print("wrong type")
            sm = 0
        except ZeroDivisionError:
            print("division by 0")
            sm = 0
        except IndexError:
            print("out of range")
            sm = 0
        finally:
            temp_lst.append(sm)
    return (temp_lst)
