# WRITE A RECURSIVE FUNCTION TO CALCULATE SUM OF FIRST N number :
def calc_sum(n):
    if n==0:
        return 0
    return n+calc_sum(n-1)
print(calc_sum(10))

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)
print(fib(6))