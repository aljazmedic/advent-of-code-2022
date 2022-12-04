import time
from typing import Iterable, List, Union
from functools import reduce, partial, wraps, lru_cache
from collections import defaultdict, Counter, namedtuple, deque
from itertools import chain, combinations, permutations, product, groupby, count, cycle, islice, repeat, accumulate
from itertools import tee, zip_longest, filterfalse, takewhile, dropwhile, starmap
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
import os
import sys
import re


def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def advent_fname():
    if any(('test' in x for x in sys.argv)):
        return 'test.txt'
    return 'input.txt'


def ngroups(iterable, n):
    # Groups an iterable into n groups
    # https://stackoverflow.com/a/8991553/1051777
    it = iter(iterable)
    while True:
        chunk = tuple(islice(it, n))
        if not chunk:
            return
        yield chunk


def fread_split(fname, sep="\n", strip=True, mode='r', encoding='utf-8', buffer_size=1024):
    # Reads a file and splits it into chunks given a separator
    with open(fname, mode, encoding=encoding) as rf:
        d: str = ""
        while True:
            d0 = rf.read(buffer_size)
            if not d0:
                break
            d += d0
            while sep in d:
                r, d = d.split(sep, 1)
                yield r.strip() if strip else r
        if d:
            yield d.strip() if strip else d


def _do_split(data: str, arg: Union[str, float, int, callable], strip=True) -> Iterable[str]:
    # Performs a split on data given a separator. It can be percent/absolute or a string.
    if isinstance(arg, str):
        d = data.split(arg)
    elif isinstance(arg, (float, int)):
        l = len(data)
        if isinstance(arg, float):
            arg = round(l * arg)
        if arg >= l:
            d = [data]
        else:
            d = data[:arg], data[arg:]
    elif callable(arg):
        return (arg(data))

    if strip:
        d = map(str.strip, d)

    return list(d)


def rsplit(*sep, data: str = None, fname=None, mode='r', strip=True, encoding='utf-8', group_n=None):
    # Splits data recursively given a list of separators
    # Separators are applied in order.
    # If data is None, then fname must be given.
    # If group_n is None, then the data is split into chunks of size 1.
    # If however group_n is given, then the data is split into chunks of size group_n.
    if not sep:
        sep = ("\n",)

    # First split is done manually
    if data is None:
        print("Reading file...")
        assert fname is not None, "fname is None"
        s1 = fread_split(
            fname, sep=sep[0], mode=mode, encoding=encoding, strip=strip)
    else:
        s1 = _do_split(data, sep[0], strip=strip)

    # Then recursively
    def _rec_rsplit(sep, data: str, strip: bool):
        if len(sep) == 1:
            return _do_split(data, sep[0], strip=strip)
        return [_rec_rsplit(sep[1:], data=d, strip=strip) for d in _do_split(data, sep[0], strip=strip)]

    s1 = (_rec_rsplit(sep[1:], data=d, strip=strip) for d in s1)
    if group_n is not None:
        s1 = ngroups(s1, group_n)
    return s1


def read_test_case():
    test_exists = os.path.exists('test.txt')
    ins_exists = os.path.exists('INSTRUCTIONS.md')
    if test_exists:
        # Check if test.txt is empty
        with open('test.txt', 'r') as rf:
            if not rf.read():
                test_exists = False
    if not test_exists and ins_exists:
        print("Generating test.txt")
        with open('test.txt', 'w') as wf:
            with open('INSTRUCTIONS.md', 'r') as rf:
                d = rf.read()
                # find <pre><code>
                n = d.count('<pre><code>')
                if n != 1:
                    if n == 0:
                        print("Cannot find test automatically")
                        time.sleep(1)
                        return 1
                    if n > 1:
                        print("Found more than one test")
                        print("Taking first one.")
                d = d.split('<pre><code>')[1]
                d = d.split('</code></pre>')[0].strip()
                wf.write(d)
        print("Wrote test.txt")
    else:
        if test_exists:
            print("test.txt exists.")
        else:
            print("INSTRUCTIONS.md does not exist.")
    time.sleep(0.5)
    return 0


if __name__ == "__main__":
    read_test_case()
    exit(0)
    l = []
    for t in rsplit('\n\n', '\n', fname="1/1.txt"):
        a = sum(map(int, t))
        l.append(a)
        # Sort L keep highest
        l.sort(reverse=True)
        l = l[:3]
    print(l)
    print(l[0])

    for t in ngroups(rsplit(" ", data="1 2 3 4 5 6 7 8 9 10"), 2):
        print(t)
