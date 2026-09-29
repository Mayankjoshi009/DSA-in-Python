def armstong_number(n):
    num = n
    total = 0
    num_digits = len(str(n))
    while n > 0:
        digit = n % 10
        total += digit ** num_digits
        n //= 10
    if total == num:
        print(f"{num} is an Armstrong number.")
    else:
        print(f"{num} is  5not an Armstrong number.")
a = int(input("Enter a number: "))
armstong_number(a)
