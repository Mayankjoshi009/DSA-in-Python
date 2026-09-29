def factor(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    print("Factors of", num, "are:", factors)
num = int(input("Enter a number to find its factors: "))
factor(num) 
#t(c) = O(n)
#s(c) = O(a)
def factors(no):
    factors = []
    for i in range(1, no//2 + 1):
        if no % i == 0:
            factors.append(i)
    factors.append(no)  # Include the number itself as a factor        
    print("Factors of", no, "are:", factors)
no = int(input("Enter a number to find its factors: "))
factors(no)
#t(c) = O(n/2) = O(n)
#s(c) = O(a)
from math import sqrt
def factors_sqrt(number):
    factors = []
    for i in range(1, int(sqrt(number)) + 1):
        if number % i == 0:
            factors.append(i)
            if i != number // i:  # Avoid adding the square root twice for perfect squares
                factors.append(number // i)
    factors.sort()  # Sort the factors for better readability
    print("Factors of", number, "are:", factors)

number = int(input("Enter a number to find its factors: "))
factors_sqrt(number)
#t(c) = O(sqrt(n) )+ O(n log n) for sorting
#s(c) = O(a)