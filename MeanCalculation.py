# Simon McLain 2018-04-18
# https://stackoverflow.com/questions/7716331/calculating-arithmetic-mean-average-in-python
# Calculate Means

def mean(n):
    return float(sum(n)) / max(len(n), 1)

with open("iris.csv","rb") as f:
  for line in f:
    a = line.split(',')
    
n = (a[0], a[1], a[2], a[3])*1.0

x = mean(n)

print(x)








