#!/usr/bin/python3

import sys
import matplotlib.pyplot as plt

def main(fname):
    data={}
       	
    with open(fname, "r") as f:
       	for line in f.readlines():
            if '//' in line:
                continue
            else:
                sl = line.split()
                data[sl[0]] = [[0,0], [int(sl[1]),float(sl[3])], [int(sl[1]),float(sl[6])]]
    # print(data)
    plot(data)

colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']

def plot(data):
    plt.figure()
    i = 0
    hz_x = [0,250]
    hz_y_80 = [300,300]
    hz_y_95 = [750,750]

    labels = []

    for k, c in data.items():
        print( k, c)
        t = plt.Polygon(c, color=colors[i], alpha=0.5, label=k)
        plt.gca().add_patch(t)
        labels.append(k)
        i +=1

    plt.plot(hz_x, hz_y_80, 'k--')
    plt.plot(hz_x, hz_y_95, 'k-')
    labels = ["95% Cache resolved"] + labels
    labels = ["80% Cache resolved"] + labels
    plt.legend(labels=labels)

    plt.xlim([0,250])
    plt.ylim([0,800])
    plt.xlabel('Instructions')
    plt.ylabel('Cycles')
    plt.show()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please add filename=")
        exit()
    main(sys.argv[1]) 
