from functools import reduce
l=[5,10,15,20,25,30]
result=list(reduce(lambda a,b=a+b),
             filter(lambda x:x%5==0),
                   map(lambda x:x*x),l)
print(result)
