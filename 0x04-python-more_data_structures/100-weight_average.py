#!/usr/bin/python3
def weight_average(my_list=[]):
    res = 0
    if my_list:
        weight_sum = 0
        summ = 0
        for tu in my_list:
            summ += (tu[0] * tu[1])
            weight_sum = weight_sum + tu[1]
        res = summ / weight_sum
    return res
