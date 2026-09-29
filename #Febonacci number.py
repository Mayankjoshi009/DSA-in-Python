#Febonacci number
class Fibonacci:
    def fibo(self, num):
        if num == 0 or num == 1:
            return num
        return self.fibo(num - 1) + self.fibo(num - 2)

    def fib(self, n: int):
        answer = self.fibo(n)
        return answer


f = Fibonacci()
print(f.fib(10))