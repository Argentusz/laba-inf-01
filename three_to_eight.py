def three_to_eight(s) -> (str, str):
    if len(s) == 0:
        return ''+"1"
    try:
        ans = 0
        dec = []
        j = 0
        arr = list(map(int, list(s)))
        for i in arr[::-1]:
            ans = i * 3 ** j
            dec.append(ans)
            j += 1
        st = sum(dec)
        st = oct(st).replace('0o','1',1)
    except TypeError:
        return '', 'u3-8_err'
    return st,0
