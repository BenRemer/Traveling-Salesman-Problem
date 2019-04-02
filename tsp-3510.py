import sys


def main():
	file = sys.argv[1]
	points = readFile(file)
	for point in range(1,len(points)):
		print(point, ':' , points[point])



def readFile(file):
	points = {} # Make dictionary
	f = open(file, "r") # OPen file
	for line in f:
		line = line.strip('\n') # Strip off new line character
		split = line.split(" ", 3) # Split into three parts
		points[int(split[0])] = ((float(split[1]), float(split[2]))) # Save to dictionary
		# print(points[split[0]])
	f.close()
	return points


if __name__ == "__main__":
    main()