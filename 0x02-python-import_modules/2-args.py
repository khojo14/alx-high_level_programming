#!/usr/bin/python3
import sys

args = len(argv) - 1

if args == 0:
    print('0 arguments.')
elif args == 1:
    print('1 argument:')
    print('{args}: {argv[0]}'.format(args,argv[1])
else:
    print('{args} arguments:'.format(args)
    for i in range args:
        print('{i+1}: {argv[i]}'.format(i+1,argv[i+1]))
