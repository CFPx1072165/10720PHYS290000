fp = open('Alice.txt','r',encoding='utf-8')

line = fp.readline()
import string
dict = {}
while line:
    s=line.split()
    for i in s:
        j=i.replace(',','').replace('_','').replace('.','').replace('-','').replace('!','').replace(':','').replace('?','').replace(']','').replace('[','').replace('(','').replace(')','').replace('\\','')
        if j in dict:
            dict[j]+=1
        else:
            dict[j]=1
    line=fp.readline()
print(dict)
keycoll=[]
for value in dict.values():
    keycoll.append(value)
keycoll.sort()
keycoll.reverse()
import matplotlib.pyplot as plt
plt.loglog(keycoll)

from scipy import optimize

def func(x,amp,alpha):
    return amp*x**alpha

para,params=optimize.curve_fit(func,range(1,len(keycoll)+1),keycoll)
print(para,params)
plt.loglog(range(1,len(keycoll)+1),func(range(1,len(keycoll)+1),para[0],para[1]),'r*',label='fit')
plt.xlabel('the Rank of the word')
plt.ylabel('the number of occurrences')
plt.show()
fp.close()
