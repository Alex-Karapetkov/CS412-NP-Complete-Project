Both the approximation solution and exact solution accept this kind of user input:\
Example Input\
3 3\
a b 3\
b c 4\
a c 5

The input is a weighted graph specified by a line containing the number of vertices n and the number of edges m followed by m lines containing the edges given in u v w format, representing an edge between u and v of weight w.\
The output contains two lines: the length of the path on one line followed by a list of vertices for the path/cycle on the second line. For example, the correct output to the example input is:

12\
a b c a
