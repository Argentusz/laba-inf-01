from algosy.fib import fibonacci

def fib_to_ten(s)->(int, str):
    try:
        summ =0
        num = list(map(int, list(s)))
        fib = fibonacci(len(num))
        fib = fib[::-1]
        for i in range(len(num)):
            summ += num[i]*fib[i]
    except TypeError:
        return '', 'uf-10_err'
    return summ, 0

def main():
    print(fib_to_ten(input()))

if __name__ == '__main__':
    main()
