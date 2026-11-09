#!/usr/bin/env python3
# test5
import sys


def main(argv):
    if len(argv) < 2:
        print(f"Usage: {sys.argv[0]} <name> <mobile>", file=sys.stderr)
        return 2

    mobile = argv[-1]
    name = " ".join(argv[:-1])

    if len(name) <= 20 and len(mobile) <= 10:
        print("PASS")
    else:
        print("FAIL")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
