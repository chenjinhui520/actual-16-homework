


import argparse


def func1(x):
    if x.lower() == 'true':
        return True
    else:
        return False

parser = argparse.ArgumentParser()
parser.add_argument("--type", help="type", type=str, choices=['encode', 'decode'], required=True)
parser.add_argument("--text", help="text", type=str, required=True)
parser.add_argument("--lst", help="lst", type=func1, required=True)

args = parser.parse_args()
print args

print args.type
print args.text
print args.lst
