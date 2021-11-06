# mortgage.py
#
# Exercise 1.7
import re
data=[]
with open('Data/portfolio.csv','rt') as f:
    for t in re.split(',|\n',f.read()):
        try:
            data.append(float(t))
        except ValueError:
            pass
data=[data[n:n+2] for n in range(0, len(data), 2)]
suka=0
for i in data:
    suka=suka + i[0]*i[1]
print(suka)
