import base64
import argparse
import sys

parser = argparse.ArgumentParser()

parser.add_argument("-e", "--encode", help="if you want to encode")
parser.add_argument("-d", "--decode", help="if you want to decode")

args = parser.parse_args()
if args.encode is not None:
    a = args.encode
    b = a.encode("ascii")
    c = base64.b64encode(b)
    d = c.decode("ascii")
    print("encoded string: ", d)
if args.decode is not None:
    a = args.decode
    b = base64.b64decode(a)
    c = str(b, "utf-8")
    print("decode string: ", c)
