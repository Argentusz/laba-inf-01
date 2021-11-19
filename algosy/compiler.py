from eight_to_ten import eight_to_ten as ette
from fib import fibonacci
from fib import ten_to_fib as ttf
from morze import morse as m
from three_to_eight import three_to_eight as thte


def main():
    n = input()
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
                    print(n)




if __name__ == '__main__':
    main()
