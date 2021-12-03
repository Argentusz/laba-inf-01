def eight_to_ten(s)->(int, str):
    ans=0
    dec=[]
    j=0
    arr = list(map(int, list(s)))
    try:
        for i in arr[::-1]:
            ans = i*8**j
            dec.append(ans)
            j+=1
        st = str(sum(dec))
        ans = int(st[::-1])
    except TypeError:
        return '', 'u8-10_err'
    return ans, 0

#returns inverted 10-number 
if __name__ == '__main__':
    print(eight_to_ten(input()))