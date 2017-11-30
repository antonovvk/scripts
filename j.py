#!/usr/bin/python

import sys, simplejson, argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-1', '--one_line', action='store_true', help='Dump object per line')
    parser.add_argument('-w', '--whole', action='store_true', help='Whole file is JSON object')
    parser.add_argument('-v', '--values', action='store_true', help='Print only values from global object')
    parser.add_argument('-a', '--array', action='store_true', help='Print the array of objects decoded from stream')

    args = parser.parse_args()

    def dump(data):
        print simplejson.dumps(data, indent=None if args.one_line else 4, sort_keys=True)

    arr = []
    with sys.stdin as file:
        if args.whole:
            try:
                data = simplejson.load(file)
            except simplejson.decoder.JSONDecodeError as e:
                sys.stderr.write('Invalid json: {}\n'.format(e))
                exit(1)
            if args.values:
                for v in data if isinstance(data, list) else data.values():
                    dump(v)
            else:
                dump(data)
        else:
            for n, line in enumerate(file):
                try:
                    data = simplejson.loads(line)
                except simplejson.decoder.JSONDecodeError as e:
                    sys.stderr.write('Invalid json at line {}: {}\n'.format(n, e))
                    exit(1)
                if args.array:
                    arr.append(data)
                else:
                    dump(data)

    if arr:
        dump(arr)
