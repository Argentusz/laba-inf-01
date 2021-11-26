def ten_to_eight(n)->(str, str):
    try:
        n = str(n)
        n = int(n[::-1])
        s =str(oct(n))
        ar = list(map(str, list(s)))
        del ar[0]
        del ar[0]
        s=''
        for i in ar:
           s+=i
    except TypeError:
        return '', 'u10-8_err'
    if(s[0]!="1"):
        return '', 'u10-8_err_missing_1_point_left'
    return s,0

if __name__ == '__main__':
    print(ten_to_eight(input()))