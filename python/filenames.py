import os
import sys


def main(args):
    if len(args) != 1:
        sys.exit("Usage: python filesizes.py dir")
    dir = args[0]

    for filename in os.listdir(dir):
        f = os.path.join(dir, filename)
        if not os.path.isfile(f):
            continue
        print(filename)


if __name__ == "__main__":
    main(sys.argv[1:])
