#!/usr/bin/env python

import sys
import json
from pykospacing import Spacing

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="%(levelname)8s %(asctime)s %(message)s ")

    lines = []
    spacing = Spacing()

    while True:
        l = sys.stdin.readline()
        if not l: break
        if l.strip() == "":
            if len(lines) > 0:
                sent = "".join(lines)
                print spacing(sent)
                print
                sys.stdout.flush()
                lines = []
            else:
                lines.append(l)

    if len(lines) > 0:
        sent = "".join(lines)
        print spacing(sent)
        lines = []
                
