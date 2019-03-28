import collections
import numpy
import matplotlib.pyplot as plt

fp=open('a.txt','r',encoding='UTF-8')
line=fp.readline()
my_dict={}

while line:
    s = line.split()
    for x in s:
        if x==",":
            break
        elif x not in my_dict:
            my_dict[x] = 1

        else :
            my_dict[x] += 1
    line = fp.readline()
fp.close()

num = []

for key in my_dict:
    num.append(my_dict[key])
print(len(num))
a=len(num)
b=range(a)
num.sort()
num.reverse()
plt.loglog(b,num)
plt.xlabel('Rank of word')
plt.ylabel('Number of the occurance')
plt.show()


