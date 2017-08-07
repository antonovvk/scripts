#!/usr/bin/python

import sys, json, argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-1', '--one_line', action='store_true', help='Dump object per line')
    parser.add_argument('-w', '--whole', action='store_true', help='Whole file is JSON object')
    parser.add_argument('-v', '--values', action='store_true', help='Print only values from global object')
    parser.add_argument('-a', '--array', action='store_true', help='Print the array of objects decoded from stream')

    args = parser.parse_args()

    def dump(data):
        print json.dumps(data, indent=None if args.one_line else 4, sort_keys=True)

    arr = []
    with sys.stdin as file:
        if args.whole:
            data = json.load(file)
            if args.values:
                for v in data if isinstance(data, list) else data.values():
                    dump(v)
            else:
                dump(data)
        else:
            for line in file:
                data = json.loads(line)
                if args.array:
                    arr.append(data)
                else:
                    dump(data)

    if arr:
        dump(arr)
