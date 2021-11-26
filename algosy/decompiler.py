from algosy.reversemorse import morse as rm
from algosy.ten_to_eight import ten_to_eight as tte
from algosy.fib_to_ten import fib_to_ten as ftt
from algosy.eight_to_three import eight_to_three as etth

def main():
    n = input()
    n, err = ftt(n)
    if err:
        print(f'Found error: {err}')
    else:
        n, err = tte(n)
        if err:
            print(f'Found error: {err}')
        else:
            n, err = etth(n)
            if err:
                print(f'Found error: {err}')
            else:
                n, err = rm(n)
                if err:
                    print(f'Found error: {err}')
                else:
                    print(*n, sep='')


if __name__ == '__main__':
    main()