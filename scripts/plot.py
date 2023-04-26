import numpy as np
import matplotlib.pyplot as plt

N = 4

width = 0.2
names= []
marks= []
names1 = []
marks1 =[]
k=0
f = open('results_30M_ipcp.txt','r')
g =open('probability-graphs.txt','r')
for row in f:
    row = row.split(' ')
    k=k+1
    names.append(row[0])
    marks.append(round(float(row[1]),3))

for row in g:
    row = row.split(' ')
    
    names1.append(row[0])
    marks1.append(round(float(row[1]),3))

X_axis = np.arange(len(names))
plt.bar(X_axis - 0.2, marks, 0.4, label = 'IPCP')
plt.ylabel('IPCP', fontsize = 20)
plt.bar(X_axis + 0.2, marks1, 0.4, label = 'DPT THRESHOLD')
  
plt.xticks(X_axis, names)


plt.xticks(rotation=60)
plt.rcParams['xtick.labelsize'] = 50

plt.subplots_adjust(bottom=0.25)
plt.xlabel("TRACE")
plt.ylabel('IPCP') # or IPC or MISS RATE
plt.title("PERFORMANCE COMPARISON - GRAPHS",fontsize = 25)
#plt.xticks(ind+width, ['400', '403', '436', '482'])
plt.legend()
#plt.ylim(ymin=100000)
#plt.ylim(0, 1.15)
plt.show()

#benchmark 403: random [0.77553,1.0276,0,1.1908]
