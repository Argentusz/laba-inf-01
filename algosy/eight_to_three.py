from algosy.eight_to_ten import eight_to_ten as ett

def eight_to_three(s)->(str,str):
    a = list(s)
    del a[0]
    st=''
    try:
        for i in a:
            st+=i
        num = ett(st)
        num = num[0]
        num = int(str(num)[::-1])
        binar =''
        while num > 0:
            binar = str(num % 3) + binar
            num //= 3
        ar = list(map(str, list(binar)))
        for i in ar:
            s += i
    except TypeError:
        return '', 'u8-3_err'
    if s[0] != '2' or s[-1] != '2':
        return '', 'u8-3_err_missing_2_points!'
    return s,0
