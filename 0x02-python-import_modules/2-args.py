#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args = len(argv) - 1

    if args == 0:
        print('0 arguments.')
    elif args == 1:
        print('1 argument:')
        print('{}: {}'.format(args, argv[1]))
    else:
        print('{} arguments:'.format(args))
        for i in range args:
            print('{} : {}'.format(i+1, argv[i+1]))
