import argparse
import sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type = float, default = 1.0, help = 'What is the 1st number?')
    parser.add_argument('--y', type = float, default = 1.0, help = 'What is the 2nd number?')
    parser.add_argument('--operation', type = str, default = 'add', help = 'What is the operation? (add, sub, mul, div)')
    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))

def calc(args):
    if args.operation == 'add':
        return args.x + args.y
    if args.operation == 'sub':
        return args.x - args.y
    if args.operation == 'mul':
        return args.x * args.y
    if args.operation == 'div':
        return args.x / args.y

if __name__ == '__main__':
    main()
