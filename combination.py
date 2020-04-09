import itertools
import numpy as np

list1 = np.arange(1,5,1)
list2 = []
for i in range(1,len(list1)+1):
    iter = itertools.combinations(list1,i)
    list2.append(list(iter))
print(list2)