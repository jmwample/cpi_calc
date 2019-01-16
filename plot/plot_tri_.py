#!/usr/bin/python3

import sys

class Data(type):
    
class InstrData:
    incomplete = 1

    name = ""
    drop = 0
    total = 0
    num = 0
    med = 0
    avg = 0
    std = 0

    def __init__(self, line):
        if len(line) != 7:
            return
        else:
            try:
                name = line[0]
                drop = int(line[1])
                total = int(line[2])
                num = int(line[3])
                med = int(line[4])
                avg = int(line[5])
                std = int(line[6])
            except:
                return
            incomplete=0
            
    # def __str__(self):
    #     return "{0} {1} {2} {3} {4}".format(name, num, med, avg, std)

    def get_x_y(self):
        return
            

def main(fname):
    data={}
       	
    with open(fname, "r") as f:
       	for line in f.readlines():
       		if '//' in line:
       			continue
       		else:
       			sl = line.split()
       			data[sl[0]] = InstrData(line)
    print(data)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please add filename=")
        exit()
    main(sys.argv[1]) 
