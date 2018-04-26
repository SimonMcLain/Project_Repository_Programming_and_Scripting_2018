#Simon McLain 2018-04-25
# Experimenting with numpy
# https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Numpy_Python_Cheat_Sheet.pdf reference to standard deviation 
# find the median for each column

import numpy
#imports numpy library providing math functions to operate on them 
data = numpy.genfromtxt('iris.csv', delimiter=',')
# Reads the data into an array
col1 = data[:,0] 
medcol1 = numpy.median(data[:,0])
col2 =data[:, 1]
medcol2 = numpy.median(data[:, 1])
col3 =data[:, 2]
medcol3 = numpy.median(data[:, 2])
col4 =data[:, 3]
medcol4 = numpy.median(data[:, 3])
# Individually looks at each column and returns the median for that column

print("The median petal length is: ", numpy.around(medcol1, decimals = 2), "millimeters")
print("The median petal width is: ", numpy.around(medcol2, decimals = 2), "millimeters")
print("The median sepal length is: ", numpy.around(medcol3, decimals = 2), "millimeters")
print("The median sepal width is: ", numpy.around(medcol4, decimals = 2), "millimeters")
