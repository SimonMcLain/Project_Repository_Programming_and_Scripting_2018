# Simon McLain 2018-04-26
# Simple analysis of the different varieties within the Iris dataset
# https://github.com/ritvikraj14/IrisData/blob/master/iris.py provided advanced code that I have studied and amended


# Import seaborn 
import seaborn as sns 

# Import scipy and assign a short name
import scipy as sci

# Import numpy and assign a short name
import numpy as np 

# Import pandas and assign a short name
import pandas as pd

# Imprt matplotlib and assign a short name
import matplotlib.pyplot as plt 

# create header labels for each column of data
names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

# load the file into an array as iris with the header labels
iris = pd.read_csv("iris.csv", names=names)


""" .shape returns basic information about the find, according to the names assigned above. 150 intergers (the measurements)
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

# returns a scatter plot
iris.plot.scatter(x = 'sepal_length', y = 'sepal_width')
plt.show()

iris = sns.load_dataset("iris")

ratio = iris["sepal_length"]/iris["sepal_width"]

for name, group in iris.groupby("species"):
    plt.scatter(group.index, ratio[group.index], label=name)

plt.legend()
plt.show()






