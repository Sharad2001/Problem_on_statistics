import math
import os
import random
import re
import sys

def stdDev(arr,n):
    sum_of_arr = 0
    sum = 0
    for i in range(n):
        sum_of_arr = sum_of_arr + arr[i]
    mean = sum_of_arr / n
    for i in range(n):
        sqr = (arr[i] - mean)**2
        sum = sum + sqr
    print(math.sqrt(sum/n))

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    stdDev(vals, n)