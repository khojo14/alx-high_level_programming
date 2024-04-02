#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    args = len(argv) - 1

    if args == 0:
        print('0')
    else:
        result = 0
        for i in range(1, args + 1):
            result += int(argv[i])

        print(result)
