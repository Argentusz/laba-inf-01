def eight_to_ten(s)->int:
    ans=0
    dec=[]
    j=0
    arr = list(map(int, list(s)))
    for i in arr[::-1]:
        ans = i*8**j
        dec.append(ans)
        j+=1
    return sum(dec)