# Simon McLain 2018-04-28
# Working out produce a coloured scatterplat
# Reference to https://stackoverflow.com/questions/45862223/use-different-colors-in-scatterplot-for-iris-dataset

# Performing a linear and quadratic classification of the Fisher Iris dataset

# Import matplotlib and assign a short name
import matplotlib.pyplot as plt 

# Import seaborn 
import seaborn as sns 

iris = sns.load_dataset("iris")

ratio = iris["sepal_length"]/iris["sepal_width"]

for name, group in iris.groupby("species"):
    plt.scatter(group.index, ratio[group.index], label=name)

plt.legend()
plt.show()





