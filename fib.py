def fibonacci(n):
    fib = []
    fib.append(1)
    fib.append(1)
    [fib.append(fib[k - 1] + fib[k - 2]) for k in range(2, n)]
    return fib

def ten_to_fib(n):
    i=0
    sum = 0
    dec=[]
    ans =""
    fib = fibonacci(i + 1)
    while(fib[-1]<n):
        fib=[]
        fib = fibonacci(i+1)
        i+=1
    for i in fib[::-1]:
        sum+=i
        if(sum>n):
            sum-=i
            dec.append(0)
        elif(sum<=n):
            dec.append(1)
            continue
    dec.append("(fib)")
    for i in dec:
        s = str(i)
        ans+=s
    return ans
