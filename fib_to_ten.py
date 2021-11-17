from fib import fibonacci

def fib_to_ten(s)->int:
    summ =0
    num = list(map(int, list(s)))
    fib = fibonacci(len(num))
    fib = fib[::-1]
    for i in range(len(num)):
        summ += num[i]*fib[i]
    return summ
