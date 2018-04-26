#Simon McLain 2018-04-25
# Experimenting with numpy
# https://docs.scipy.org/doc/numpy/reference/generated/numpy.std.html reference to standard deviation 
# calculate the standard deviation of each column

import numpy
#imports numpy library providing math functions to operate on them 
data = numpy.genfromtxt('iris.csv', delimiter=',')
# Reads the data into an array
col1 = data[:,0] 
stdcol1 = numpy.std(data[:,0])
col2 =data[:, 1]
stdcol2 = numpy.std(data[:, 1])
col3 =data[:, 2]
stdcol3 = numpy.std(data[:, 2])
col4 =data[:, 3]
stdcol4 = numpy.std(data[:, 3])
# Individually looks at each column and returns the standard deviation for that column

print("The standard deviation in petal length is: ", numpy.around(stdcol1, decimals = 2))
print("The standard deviation in petal width is: ", numpy.around(stdcol2, decimals = 2))
print("The standard deviation in sepal length is: ", numpy.around(stdcol3, decimals = 2))
print("The standard deviation in sepal width is: ", numpy.around(stdcol4, decimals = 2))
