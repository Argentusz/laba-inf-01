def two_to_eight(s)->str:
    if len(s) == 0:
        return ''
    return two_to_eight(s[:-3]) + str(int(s[-3:], 2))