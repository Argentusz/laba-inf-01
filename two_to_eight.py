def two_to_eight(s) -> str:
    if len(s) == 0:
        return ''+"1"
    st = two_to_eight(s[:-3]) + str(int(s[-3:], 2))
    # k = int(st)+1
    # st=str(k)
    return st

print(two_to_eight("1010110010110"))