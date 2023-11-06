#!/usr/bin/python3
# 102-magic_calculation.py
def magic_calculation(x, y):
    out_put = 0
    for b in range(1, 3):
        try:
            if b > x:
                raise Exception('Too far')
            else:
                out_put += x ** y / i
        except:
            out_put = y + x
            break
    return (out_put)
