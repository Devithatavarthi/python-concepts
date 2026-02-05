 #Use map() with a lambda to add 5 to every element of the following nested list=[[1,2],[3,4],[5,6]]

lst=[[1,2],[3,4],[5,6]]
result=list(map(lambda sub:list(map(lambda x:x+5,sub)),lst))
print(result)
