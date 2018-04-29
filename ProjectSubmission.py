# Simon McLain 2018-04-26
# Simple analysis of the different varieties within the Iris dataset
# https://github.com/ritvikraj14/IrisData/blob/master/iris.py provided advanced code that I have investigated during my project. 


# Import seaborn library and assign a short name
import seaborn as sns 

# Import scipy and assign a short name
import scipy as sci

# Import numpy and assign a short name
import numpy as np 

# Import pandas and assign a short name
import pandas as pd

# Import matplotlib and assign a short name
import matplotlib.pyplot as plt 

# create names for header labels for each column of data, enabling them to be called in subsequent code
names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

# load the file into an array as iris with the header names
iris = pd.read_csv("iris.csv", names=names)


""" .shape returns basic information about the file, according to the names assigned above. 150 intergers (the measurements)
 and 5 classes"""
print(iris.shape)

# .describe returns Stats about each column of data 

print(iris.describe())

# returns the number of measurements for each class

print(iris.groupby('class').size())

# returns a histogram
iris.plot.hist()

plt.show()

# returns a box plot
iris.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
plt.show()

# returns a scatter plot, x and why can be assigned to one of the names created, provided it is an integer
iris.plot.scatter(x = 'sepal_length', y = 'sepal_width')
plt.show()

iris = sns.load_dataset("iris")
# loads the dataset into seaborn
ratio = iris["sepal_length"]/iris["sepal_width"]
"""names can be used here, and a scatter plot created for comparison of any combination. For instance petal length and 
width measurements could be plotted here"""


for name, group in iris.groupby("species"):
    plt.scatter(group.index, ratio[group.index], label=name)
# groups and labels chart, in this instance so they can be identified by colour
plt.legend()
plt.show()






