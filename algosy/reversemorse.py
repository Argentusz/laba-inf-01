def morse(n):
    # Morze dictionary
    # — = 1
    # • = 0
    n = n[len(n) - 2:0:-1]
    morse_dict = {'01': 'a', '1000': 'b', '1010': 'c', '100': 'd', '0': 'e', '0010': 'f', '110': 'g', '0000': 'h',
                  '00': 'i', '0111': 'j', '101': 'k', '0100': 'l', '11': 'm', '10': 'n', '111': 'o', '0110': 'p',
                  '1101': 'q', '010': 'r', '000': 's', '1': 't', '001': 'u', '0001': 'v', '011': 'w', '1001': 'x',
                  '1011': 'y', '1100': 'z', '01111': '1', '00111': '2', '00011': '3', '00001': '4', '00000': '5',
                  '10000': '6', '11000': '7', '11100': '8', '11110': '9', '11111': '0'}

    res = (n.split('2'))

    for i in range((len(res)-1) or 1):
        res[i] = morse_dict[res[i]]

    return res, 0


if __name__ == '__main__':
    code, error = morse(input())
    if not error:
        print(*code, sep='')
    else:
        print(f'Error code: {error}')
