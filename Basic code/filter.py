l=[1,2,3,4,5,6,7,8,9,10]
def greter(num):
    return num>5
a=list(filter(greter,l))
print (a)