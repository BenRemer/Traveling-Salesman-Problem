from timeit import default_timer as timer
import timeit
import time
import numpy as np

def timerStupid():
    start = time.time()
    print("hello")
    end = time.time()
    print("Run-time for algo one" + end - start)

def timerSmarter():
    #
    print(timeit.timeit(stmt=func1, number=10000))
    print(timeit.timeit(stmt=func2, number=10000))

def func1():
    print("hello")
    _norm= np.linalg.norm()

    #args will need to be hardcoded here

def func2():
    print("hello")
    #args will need to be hardocded here

def main():
	# input_file = sys.argv[1]
	# output_file = sys.argv[2]
	# time = sys.argv[3]
	# points = read_file(input_file)
	# for point in range(1,len(points)):
	# 	print(point, ':' , points[point])
	#event = threading.Event
	#for(i)

    start = time.time()

    f = open("tsp.txt", "r")
    lines = f.readlines()
    d = open("output.txt", "w")
    for line in lines:
        d.write(line)

    while(time.time() - start < 10):
        x = 1
    end = time.time()
    print("Run-time for algo one" + str(end - start))


if __name__ == "__main__":
    main()