import csv
import panda as pd
with open('hw.csv',newline = '') as f:
    reader = csv.reader(f)
    file_data = list(reader)
from collections import Counter
file_data.pop(0)
new_list= [] 
for i in range(len(file_data)) :
    n_num = file_data[i][1]
    new_list.append(float(n_num))
n=len(new_list)
total = 0
for x in new_list :
    total = total + x
mean = total/n
n = len(new_list)
if n % 2 == 0:
    median = float(new_list[n//2])
    median2 = float(new_list[n//2-1])
    t_median = (median + median2)/2
else :
    t_median = new_list[n//2] 
t_median
data = Counter(new_list)
data1 = data.values()
def mode(lst) :
    y={}
   
    for i in lst :
       
        if not i in y:
            y[i]=1
        else :
            y[i]+=1
    return [g for g , l in y.items() if l ==max(y.values())]
