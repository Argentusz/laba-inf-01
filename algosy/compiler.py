from algosy.eight_to_ten import eight_to_ten as ette
from algosy.fib import fibonacci
from algosy.fib import ten_to_fib as ttf
from algosy.morze import morse as m
from algosy.three_to_eight import three_to_eight as thte


def comp(n):

    n, err = m(n)
    if err:
        print(f'Found error: {err}')
    else:
        n, err = thte(n)
        if err:
            print(f'Found error: {err}')
        else:
            n, err = ette(n)
            if err:
                print(f'Found error: {err}')
            else:
                n, err = ttf(n)
                if err:
                    print(f'Found error: {err}')
                else:
                    return n


def main():
    comp(input())


if __name__ == '__main__':
    main()
