def two_to_eight(s)->str:
    if len(s) == 0:
        return ''+"1"
    return two_to_eight(s[:-3]) + str(int(s[-3:], 2))
#returns 8-number with "1" at the first position
