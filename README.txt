Name of Group Members: Joshua Vayle and Ben Remer
Email addresses: jvayle3@gatech.edu and bremer@gatech.edu 
Date of Submission: 04/19/2019


Files submitted:
        tsp-3510.py → the main file that contains not only the main method (find_tsp) but also all of the methods for the genetic algorithm. This is the most important file in the project submission
        objects.py → this is the object file that holds the object definitions for City (our name for the vertex object) and Fitness (which stores the route, its distance, and the fitness of the route (fitness = 1/distance of the route)
        README.txt → this file is the one you have open right now and contains a small overview of the project and the instructions on how to run it
        Algorithm.pdf → a small writeup on how the algorithm works and our rationale for choosing a genetic algorithm
        mat-output.txt → the output file from the 30 node test case

Execution Instructions
to run our project simply:
0) install numpy if not installed by running "pip install numpy"
1) open the command line
2) using cd command navigate to the location of the project
3) run the initialization command as specified in the instructions:
    <project file path>: genetic <input-coordinates.txt>  <output-tour.txt> <time>

Known Bugs/Limitations:
The only possible limitation is that since the algorithm does do random breeding and mutation the solution route that it
finds will be inconsistent. In other words it might not find the same solution every time. This means it is
theoretically possible that our algorithm fails to get under the threshold (min total cycle cost) one time you run it,
but very well might get it the next time. Therefore, it might be necessary to run the algorithm multiple times to get an
 idea of the average solution it is coming up with.
