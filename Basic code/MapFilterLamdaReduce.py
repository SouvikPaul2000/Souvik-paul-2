from ast import Lambda

from functools import reduce

l2=[1,2,3,4,5,6,7,8,9]
l=[1,2,3,4,5,6,7,8,9,10]
a=list(filter(lambda x : x>5,l))
print (a)
b=list(map(pow,a,l2))
print(b)
sum=(reduce(lambda x, y: x + y,b))
print(sum)
