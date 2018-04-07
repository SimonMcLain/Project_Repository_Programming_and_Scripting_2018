# Simon McLain 2018-04-07

"""Roughwork"""

import csv
"""imports a module to enable reading of a comma separated values file"""

with open("iris.csv") as f:
  """opens the file and asigns content as the variable f""" 
  for line in f:
    """this for statement instructs Python to interate over each line in the file, which is asigned as f"""
    a = line.split(',')
    """this statement splits the line by the commas and assigns each value to the variable a""" 
    
    
    print (a[0], a[1], a[2], a[3])
    """this instructs Python to print the first four values of each line"""

    

    

    







    
    




    
  


    


 
 
  #for line in f:
    # print(line.split(',')[0].format(*line)
  
