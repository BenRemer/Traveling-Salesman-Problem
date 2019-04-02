import sys



def read_file(file):
	""" Makes a dictionary, goes line by line and add them to the dictionary as tuple of (x,y)"""
	points = {} # Make dictionary
	f = open(file, "r") # Open file
	for line in f:
		line = line.strip('\n') # Strip off new line character
		split = line.split(" ", 3) # Split into three parts
		points[int(split[0])] = ((float(split[1]), float(split[2]))) # Save to dictionary
		# print(points[split[0]])
	f.close()
	return points

def main():
	input_file = sys.argv[1]
	output_file = sys.argv[2]
	time = sys.argv[3]
	points = read_file(input_file)
	for point in range(1,len(points)):
		print(point, ':' , points[point])

if __name__ == "__main__":
    main()