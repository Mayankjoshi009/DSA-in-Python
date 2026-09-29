from math import *     
def count_digits(n):
    print(int(log10(n))+1 if n>0 else 1,"digits.")
count_digits(12345)    