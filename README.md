# GMIT Progamming and Scripting project submission by Simon McLain. April 29, 2018. 
## This project entails researching the Fisher's Iris dataset, then writing documentation and code in the Python programming language based on the research. 



Table of Contents
####
1. Introduction to Fisher, his Iris dataset, Data Analytics & Python
2. Summary of investigations
3. Project management & project plan
4. How to run the script
5. References

The file ProjectSubmission.py contains the Python code I developed during this project. 

####
1. Introduction to Fisher, his Iris dataset, Data Analytics and Python 

Sir Ronald Fisher (1890-1962) is often referred to as the father of modern statistics and experimental design due to the major contributions he made to these fields. Fisher introduced the concept of variance (ANOVA), a measure of how data distributes around a mean or expected value, as well as inventing tools for modern experimental design. Fisher literally wrote the book on it: "Statistical Methods for Research Workers", rather he wrote several books on it. His work at Rothame Experimental Station in agricultural research gave him access to agricultural data that he used to develop new theories on experiments. It's quite fortunate he applied his brilliant mind to statistics in agriculture given his other interest: eugenics, considered a respectable scientific topic in his time. 

Among Fisher's work is the Iris dataset, it consists of 150 samples, 50 each of three species of Iris, Iris setosa, Iris virginica and Iris versicolour. Four measurements where taken from each sample. The length and breadth of both petals and sepals. Statistically speaking this dataset is interesting, as it is mathmatically possible to differentiate 3 visually similar 
(almost identical) flowers when an appropriate statistical approach is applied.

This feature has resulted in the Iris data becoming extremely popular with students of Data Analytics when learning. Data Analytics is the science of using computers and computer programming to transform information into knowledge, and potentially to automate a response. For instance, if significant numbers of people in California start viewing a particular widget on Amazon, Amazon's data analytics programs will identify the trend then automatically ship said widgets to a local warehouse, in readiness for orders being placed, not when orders are placed, before, without human intervention at any stage. See d) below. 

Broadly speaking there are four stages of development within Data Analytics, below in order of increasing degree of automation and business value:
 
 a) Descriptive Analytics: 'this' just happened
 
 b) Predictive Analytics: 'this' might happend
 
 c) Prescriptive Analytics: based on the data you should do 'this'
 
 d) Cognitive Analytics: computer automatically did 'this' without human intervention

Python is a 'high-level' 4th generation computer language. Simply put it is easier to learn than other programming languages since the code used is broadly similar to writing, making it easier to read and understand. 

The name Python was inspired by the British surreal comedy group 'Monty Python' and it's nice to imagine the "Knights that say Ni!" planting Iris's in their scubbery. 

2. Summary of investigations

Although simple mathematical operations can be written directly in Python I learned through this project the Seaborn, Numpy, SciPy and Pandas libraries contain modules, mini-scripts, that allow users to quickly perform mathematical operations including more advanced features such as creating summary tables and charts. Some of these libraries are interdependent, typically they are accessed by installing a Python package such as Anaconda, then called using the 'import' command. A Google search for the Iris dataset returns numerous examples of the application of these libraries. Content on StackOverFlow and GitHub is particularly useful. 

I discovered three useful commands for describing data in a csv file which is useful for obtaining a general overview of the content of a such file. Especially useful for large files when the extent of the content is not known. 

The .shape command describes the array, 150 datapoints distributed across five features; Sepal + Petal lengths and widths as wells as type of Iris. 

The .describe command performs a basic statistical analysis of mean, standard deviation, min/ max and distribution. 

Finally the .groupby('class').size() command returns the measurements by each type of Iris. 

The most interesting graphical representation of the data I discovered was contained in a script in a GitHub repository created ritvikraj14. See Figure 1.3 in the charts folder of my repository. This coloured scatterplot clearly differentiates between the three varieties of Iris as demonstrated in the group of blue, orange and green dots. This graphical representation demonstrates what is mean by a multivariant analysis: taking a number of measurements and using them to descriminate unique features. In this case dimensions of sepal and petals descriminating between types of Iris. 

Using this descriptive analytics data and writing a further script, and without any knowledge of flower taxonomy one could go to the Knights' scrubbery, collect several of their Iris flowers and use the model from this data to predict which of the three Iris types they are most likely to be. 

Three further charts can be created using my Python script. Although these do describe each measurement they provided little insight for descriminating between the three types of Iris. 

Fig 1. displays a histogram showing the distribution of each of the four Iris flower measurements

Fig 1.1. displays a boxplot, a graphical representation of the mean and distribution from the mean for each measurement 

Fig 1.2. Displays a scatterplot, where two measurements can be plotted against each other

3. Project management

My approach to the management of this project is based on the Project Management Insititute methodologies and as such I have broken the project in to 5 phases:


a) Initiating
b) Planning
c) Executing
d) Steering
e) Closing

It should be noted that these phases are not intended to be sequential, rather they overlap at times. Initiating occurs for a relatively short period of time, planning occurs throughout the life of the project, executing occurs as soon as the project deliverables are understood, steering begins shortly after planning and executing have begun and closing should be considered as verifying the project deliverables have been met and ends at mid-night on April 29th. 


Intiating Phase
During this phase I reviewed the project orientation video and supporting documentation to identify the deliverables required to obtain a passing grade. I identified times when I would be able to work on the project, given work, family and other committments. 

I also used this as an opportunity to perform some investigative research, identifying potential sources of information. 

Planning Phase
Using Google and Microsoft Edge I identified materials which could be used during the project, downloading Python scripts and recording website addresses. Then uploading them to this repository. I also researched and creates some simple Python scripts that would calculate the average, median and standard deviation  for each of the columns in the Iris dataset. 

I also decided to use this as a learning opportunity to develop and understanding of Matplotlib for graphical representation of the Iris dataset, as well develop a basic understanding of numpy, scipy, pandas and seaborn. These decisions helped me to narrow the focus of the online resources and other materials I would be using during the project. 

Towards the end of the planning phase I decided I wanted to find code that would create a statistical summary of the Iris dataset and create some charts. I decided that a key component of the project would be a decription of what I learned about the Iris dataset from the output of the code. 

Executing Phase
During this phase I actively worked on the key deliverables which I summarise as follows:
a) A comprehensive README file
b) Evidence of thorough research into the Iris dataset and examples of interesting analyses that other have pursued
c) Writing Python scripts to investigate the Iris dataset, including annotation that demonstrates an understanding of the material and demonstrates my own work
d) Comprehesive references of sources the that have contributed to this project

Closing
During this phase I consoldated the files that I had created, checked that the key deliverables meet the requirements laid out in points a - d above. Rechecked the Python scripts run as intended, check references used, finalise the README fiole and tidy-up the project repository, file names etc. 


4. How to run the script

a) Download and install Anaconda https://www.anaconda.com/download/

b) I recommend using visual studio to run the files https://www.visualstudio.com/downloads/

c) To run the file open it in visual studio terminal, type Python then the full file name, and don't forget to include the .py file extension. You may also copy the tasks.json file to create the shortcut Ctrl Shift b to automatically run the active file in the Visual Studio Terminal.

d) When the script in run a summary of the data will be displayed in the integrated terminal. Picture files will also be created for the four charts, these can be saved to your hard drive. 


5. References:

Below is a list of references used during my project. Where the code created relied heavily upon work created by others I have added it to the Python Scripts. 

https://en.wikipedia.org/wiki/Iris_flower_data_set

https://study.com/academy/lesson/sir-ronald-fisher-biography-contributions-to-statistics.html

https://www.britannica.com/biography/Ronald-Aylmer-Fisher

Mark Lutz, Learning Python, 2013 O'Reilly

http://pythonhosted.org/bob.db.iris/py_api.html

https://www.youtube.com/watch?v=PlrEJfvZRNo

Python Scripts
https://medium.com/codebagng/basic-analysis-of-the-iris-data-set-using-python-2995618a6342

Numpy cheat sheet
https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Numpy_Python_Cheat_Sheet.pdf

Pandas cheat sheets
https://www.dataquest.io/blog/pandas-cheat-sheet/

file:///C:/Users/simon/Downloads/Pandas_Cheat_Sheet.pdf

Scipy cheat sheets
https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Python_SciPy_Cheat_Sheet_Linear_Algebra.pdf

Matlpltlib usermanual/ cheatsheet
https://matplotlib.org/Matplotlib.pdf
https://api.ning.com/files/ix5EiwUaTp0E5*jp7eiswyccuIvY2ZsTZtw4N00CRgaI9Y5fMQEYTahMiecJ8nwooZZHezoGsTkJ-duNPnb39c9Qmgg9hX4L/dc1.png
https://storage.googleapis.com/supplemental_media/udacityu/5428018709/numpy_pandas_cheatsheet.pdf

Other references
https://uk.mathworks.com/help/stats/sample-data-sets.html;jsessionid=1ed9d85bab3a1121160e7427a0a8?requestedDomain=true
https://uk.mathworks.com/matlabcentral/fileexchange/32664-iris-data-set-clustering
http://www.pymvpa.org/tutorial_datasets.html

