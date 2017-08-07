#!/usr/bin/python
#-*-coding:utf8-*-

import argparse, sys, csv, json
from sets import Set

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--delim', action='store', help='CSV delimiter', default=',')
    parser.add_argument('-q', '--quote', action='store', help='CSV quote char', default='"')
    parser.add_argument('-f', '--fields', action='append', help='Fields to print', type=int)
    parser.add_argument('-m', '--map', action='append', help='Map fields to dict keys', type=lambda kv: kv.split(":"), dest='kv')

    args = parser.parse_args()

    rd = csv.reader(sys.stdin, delimiter=args.delim, quotechar=args.quote)
    for row in rd:
        if args.fields:
            for i, field in enumerate(row):
                if i in args.fields:
                    print json.dumps(field)
        elif args.kv:
            res = {}
            for k, v in args.kv:
                try:
                    idx = int(k)
                    if idx < len(row):
                        res[v] = row[idx]
                except:
                    pass

            print json.dumps(res)
        else:
            print json.dumps(row)
