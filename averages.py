#Simon McLain 2018-04-25
#Experimenting with numpy
# https://docs.scipy.org/doc/numpy/reference/generated/numpy.around.html used to discover how to create print to decimal places
#calculate the mean of each column

import numpy
#imports numpy library providing math functions to operate on them 
data = numpy.genfromtxt('iris.csv', delimiter=',')
# Reads the data into an array
col1 = data[:,0] 
meancol1 = numpy.mean(data[:,0])
col2 =data[:, 1]
meancol2 = numpy.mean(data[:, 1])
col3 =data[:, 2]
meancol3 = numpy.mean(data[:, 2])
col4 =data[:, 3]
meancol4 = numpy.mean(data[:, 3])
# Individually looks at each column and returns the average for that column

print("The average petal length is: ", numpy.around(meancol1, decimals = 2),"milimeters")
print("The average petal width is: ", numpy.around(meancol2, decimals = 2),"milimeters")
print("The average sepal lenght is: ", numpy.around(meancol3, decimals = 2),"milimeters")
print("The average sepal width is: ", numpy.around(meancol4, decimals = 2),"milimeters")

