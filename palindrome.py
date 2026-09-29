def palindrome(n):
    original=n
    reversed_num=0
    while n>0:
        digit=n%10
        reversed_num=reversed_num*10+digit
        n=n//10    
    if original==reversed_num:
        print(f"{original} is a palindrome.")
    else:
        print(f"{original} is not a palindrome.")
from math import *     
def count_digits(n):
    print(int(log10(n))+1 if n>0 else 1,"digits.")
def reverse_number(n):
    reversed_num=0
    while n>0:
        digit=n%10
        reversed_num=reversed_num*10+digit
        n=n//10
    print(f"Reversed number: {reversed_num}")           
palindrome(121)
palindrome(123456)                
count_digits(121)
count_digits(123456)                