#!/usr/bin/python3

import numpy as np
import sys



def main(fname):
    res = []

    with open(fname, "r") as f:
        for line in f.readlines():
            res.append(int(line))
    
    print(np.median(res)/10000)
    print(min(res)/10000)
    print(np.average(res)/10000)
    print(np.std(res)/10000)

if __name__ =="__main__":
    if len(sys.argv) < 2: 
        print("Please add filename")
        exit()
    main(sys.argv[1])
