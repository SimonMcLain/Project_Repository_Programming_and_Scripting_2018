# Simon McLain 2018-04-26
# Simple analysis of the different varieties within the Iris dataset
# https://github.com/ritvikraj14/IrisData/blob/master/iris.py provided advanced code that I have studied and amended


# scipy

import scipy

# numpy

import numpy

#panda
import pandas

#matplot
import matplotlib.pyplot as plt 


# Load dataset 

names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

dataset = pandas.read_csv("iris.csv", names=names)


# shape

print(dataset.shape)

# head

print(dataset.head(10))

# descriptions

print(dataset.describe())

# class distribution

print(dataset.groupby('class').size())

