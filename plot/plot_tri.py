#!/usr/bin/python3



def main(fname):
	data={}
		
	with open(fname, "r") as f:
		for line in f.readlines():
			if '//' in line:
				continue
			else:
				sl = line.split(" ")
				data[sl[0]] = sl[1:]
	print(data)


if __name__ == '__main__':
	if len(sys.argv) < 2:
        print("Please add filename=")
    exit()
		main(sys.argv[1]) 
