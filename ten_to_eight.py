def ten_to_eight(n)->str:
    n = str(n)
    n = int(n[::-1])
    s =str(oct(n))
    ar = list(map(str, list(s)))
    del ar[0]
    del ar[0]
    s=''
    for i in ar:
       s+=i
    return s
