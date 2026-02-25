#Use functools.reduce() with a lambda to find the largest number from a given
#list Dynamically
from functools import reduce
lt=[10,20,30,40]
large=reduce(lambda a,b:a if a>b else b,lt)
print(large)
