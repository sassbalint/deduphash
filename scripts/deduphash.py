# -*- coding: utf-8 -*-
"""Annotate duplicate lines in stdin."""

import sys
import collections
import hashlib

STRHASH = collections.defaultdict(int)

def strhash(string):
    """Return a (16 digit) hash value for 'string'."""
    return str(int(
        hashlib.sha256(
            string.encode('utf-8')).hexdigest(), 16) % 10**16)

def deduphash():
    """
    Print lines prefixed with ' - '
    except duplicate lines which are prefixed with ' + '.
    """

    # read from stdin (until empty string)
    while True:

        # skip possible UTF-8 errors
        try:
            line = sys.stdin.readline()
        except Exception as e:
            print("SKIP <- Error: [{}] [{}]".format(
                sys.exc_info()[0], e), file=sys.stderr)
            print(line, file=sys.stderr)
            continue

        if line == '':
            exit(0)

        line = line.strip()
        hashcode = strhash(line)
        if hashcode in STRHASH:
            code = '+'
        else:
            STRHASH[hashcode] += 1
            code = '-'
        print(" {} {}".format(code, line))

def main():
    """Main."""
    deduphash()

if __name__ == '__main__':
    main()
