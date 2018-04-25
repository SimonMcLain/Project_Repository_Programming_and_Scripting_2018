#Simon McLain 2018-04-25
#Experimenting with numpy

#calculate the mean of each column

import numpy

# Read data into an array

data = numpy.genfromtxt('Data/iris.csv', delimiter=',')

firstcol = data[:,3]
meancolumn = numpy.mean(data[:,3])

print("The average of each column is: ", meancolumn)
