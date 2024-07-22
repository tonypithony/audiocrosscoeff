# https://www.geeksforgeeks.org/python-pearson-correlation-test-between-two-variables/

# Import those libraries
import pandas as pd
from scipy.stats import pearsonr

# Import your data into Python
df = pd.read_csv("anscombe.csv")
# df = pd.read_csv("Auto.csv")

# Convert dataframe into series
list1 = df['x2']; list2 = df['y2']
# list1 = df['weight']; list2 = df['mpg']

# Apply the pearsonr()
corr, _ = pearsonr(list1, list2)
print('Pearsons correlation: %.4f' % corr)



# https://www.geeksforgeeks.org/visualize-data-from-csv-file-in-python/
import matplotlib.pyplot as plt 
import csv 
  
Names = [] 
Values = [] 
  
with open('anscombe.csv','r') as csvfile:
# with open('Auto.csv','r') as csvfile: 
    lines = csv.reader(csvfile, delimiter=',') 
    for row in lines: 
        # Names.append(row[0]) ; Values.append(row[1]) 
        Names.append(row[1]) ; Values.append(row[5])

x = [float(i) for i in Names[1:]]
y = [float(i) for i in Values[1:]]

# print(x, y)
 
plt.scatter(x, y, color = 'orange',s = 100) 
plt.xticks(rotation = 25) 
plt.xlabel('Names') 
plt.ylabel('Values') 
plt.title(f'Pearsons correlation: {corr:.4f}', fontsize = 20) 
plt.grid()  
plt.show() 