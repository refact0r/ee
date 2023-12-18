import filecmp
import sys


def main(args):
    if len(args) != 2:
        sys.exit("Usage: python filesizes.py dir1 dir2")
    dir1, dir2 = args

    dcmp = filecmp.dircmp(dir1, dir2)

    dcmp.report()


if __name__ == "__main__":
    main(sys.argv[1:])
