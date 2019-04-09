import matplotlib.pyplot  as plt
import math
import numpy as np
import random
import matplotlib.pyplot as plt
n = int(input('the number of people n'))
m = float(input('the money each one owns'))
d = float(input('the ratio of the money to give(小数)'))
choice = int(input('case (0)if you have no money,stop. case(1) otherwise'))
k = int(input('times'))
money=[m] * n
"""print(money),test point"""
def case_0(instead):
    i=0
    while i<k :
        chosen1=random.randint(0,n-1)
        chosen2=random.randint(0,n-1)
        while chosen2==chosen1:
            chosen2=random,randint(0,n-1)
        result  = random.random()
        if result<=1/3:
            instead[chosen1]+=d*m
            instead[chosen2]-=d*m
        #chosen1 win
        elif result<=2/3:
            instead[chosen2] += d*m
            instead[chosen1] -= d*m
        if instead[chosen2]<=0 or instead[chosen1]<=0:
            break
    return instead
def case_1(instead):
    i=0
    while i<k :
        chosen1=random.randint(0,n-1)
        chosen2=random.randint(0,n-1)
        while chosen2==chosen1:
            chosen2=random,randint(0,n-1)
        result  = random.random()
        if result<=1/3:
            instead[chosen1]+=d*m
            instead[chosen2]-=d*m
        #chosen1 win
        elif result<=2/3:
            instead[chosen2] += d*m
            instead[chosen1] -= d*m
    return instead
if choice==0:
    result_0=case_0(money)
    plt.hist(result_0)
    plt.title('Salary Game')
    plt.xlabel('Money')
    plt.ylabel('The Number of People')
    plt.show()
elif choice==1:
    result_1 = case_1(money)
    plt.hist(result_1)
    plt.title('Salary Game')
    plt.xlabel('Money')
    plt.ylabel('The Number of People')
    plt.show()



