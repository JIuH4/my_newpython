def getSum(n):
    if len(n) == 5:
        return 0
    else:

        return n[0] + getSum(n[1:])


def fibo(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibo(n - 1) + fibo(n - 2)


print(fibo(40))
