#Map, Filter, Reduce and Lambda Functions – Questions & Answers
#1. Add 5 to every element in a nested list using map() and lambda
W#rite a Python program to add 5 to every element in a nested list using map() and lambda.
#Answer:
lst = [[1, 2], [3, 4], [5, 6]]
result = list(map(lambda sub: list(map(lambda x: x + 5, sub)), lst))
print(result)
#2. Filter dictionary keys whose values are greater than 50
#Write a Python program to filter dictionary items whose values are greater than 50 using filter().
d = {"apple": 100, "banana": 40, "cherry": 150}
result = dict(filter(lambda item: item[1] > 50, d.items()))
print(result)

#Write a Python program to find the largest number in a list using reduce().
from functools import reduce
lst = [12, 45, 7, 89, 23]
largest = reduce(lambda a, b: a if a > b else b, lst)
print(largest)
#4.Explain what happens if the lambda function in reduce() accepts only one parameter or three parameters.
#Write a Python program to convert characters of a string into ASCII values using map().
s = "Python"

result = list(map(ord, s))

print(result)

#Write a Python program to remove vowels from a string using filter().
s = "Programming"
result = "".join(filter(lambda ch: ch.lower() not in "aeiou", s))

print(result)

#7. Concatenate characters into a single string using reduce()

#Write a Python program to concatenate characters into a single string using reduce().


from functools import reduce

chars = ['P', 'y', 't', 'h', 'o', 'n']

result = reduce(lambda a, b: a + b, chars)

print(result)


#Write a Python program to print memory addresses of list elements using map() and id().

lst = [10, 350, 10, 350, 20]

addresses = list(map(id, lst))

print(addresses)
Explanation:
Python stores small integers in cache memory.
Same values may share the same memory address.
9. Difference between map(str, [1,2,3]) and map(lambda x: str(x), [1,2,3])
Question:

Explain the difference and tell which one is faster.

Answer:
Method 1
map(str, [1, 2, 3])
Method 2
map(lambda x: str(x), [1, 2, 3])
Explanation:
map(str, ...) directly uses built-in str()
map(lambda x: str(x), ...) adds extra lambda processing
Faster:
map(str, [1, 2, 3])
10. Use map(), filter(), and reduce() in a single pipeline
Question:

Write a Python program using map(), filter(), and reduce() together in one pipeline.

Answer:
from functools import reduce

nums = [5, 10, 15, 20, 25, 30]

result = reduce(
    lambda a, b: a + b,
    filter(
        lambda x: x % 5 == 0,
        map(lambda x: x ** 2, nums)
    )
)

print(result)
Output:
2275
file

I can’t directly generate and attach a downloadable .docx or .pdf file in this chat without using the canvas/file tool.

But I can format it cleanly for you to copy into Word/PDF.

If you want, I can also create:

a Word-style document format
a PDF-style format
or a short handwritten-notes style version.
okk
Map, Filter, Reduce and Lambda Functions – Questions & Answers
1. Add 5 to every element in a nested list using map() and lambda
Question:

Write a Python program to add 5 to every element in a nested list using map() and lambda.

Answer:
lst = [[1, 2], [3, 4], [5, 6]]

result = list(map(lambda sub: list(map(lambda x: x + 5, sub)), lst))

print(result)
Output:
[[6, 7], [8, 9], [10, 11]]
2. Filter dictionary keys whose values are greater than 50
Question:

Write a Python program to filter dictionary items whose values are greater than 50 using filter().

Answer:
d = {"apple": 100, "banana": 40, "cherry": 150}

result = dict(filter(lambda item: item[1] > 50, d.items()))

print(result)
Output:
{'apple': 100, 'cherry': 150}
3. Find the largest number dynamically using reduce()
Question:

Write a Python program to find the largest number in a list using reduce().

Answer:
from functools import reduce

lst = [12, 45, 7, 89, 23]

largest = reduce(lambda a, b: a if a > b else b, lst)

print(largest)
Output:
89
4. What happens if lambda in reduce() accepts wrong parameters?
Question:

Explain what happens if the lambda function in reduce() accepts only one parameter or three parameters.

Answer:
Case 1: One parameter
from functools import reduce

lst = [1, 2, 3]

reduce(lambda x: x + 1, lst)
Error:
TypeError: <lambda>() takes 1 positional argument but 2 were given
Case 2: Three parameters
reduce(lambda x, y, z: x + y + z, lst)
Error:
TypeError: <lambda>() missing 1 required positional argument
Explanation:

reduce() always passes two arguments:

accumulated value
current value

So lambda must accept exactly two parameters.

5. Convert characters into ASCII values using map()
Question:

Write a Python program to convert characters of a string into ASCII values using map().

Answer:
s = "Python"

result = list(map(ord, s))

print(result)
Output:
[80, 121, 116, 104, 111, 110]
6. Remove vowels from a string using filter()
Question:

Write a Python program to remove vowels from a string using filter().

Answer:
s = "Programming"

result = "".join(filter(lambda ch: ch.lower() not in "aeiou", s))

print(result)
Output:
Prgrmmng
7. Concatenate characters into a single string using reduce()
Question:

Write a Python program to concatenate characters into a single string using reduce().

Answer:
from functools import reduce

chars = ['P', 'y', 't', 'h', 'o', 'n']

result = reduce(lambda a, b: a + b, chars)

print(result)
Output:
Python
8. Print memory addresses using map() and id()
Question:

Write a Python program to print memory addresses of list elements using map() and id().

Answer:
lst = [10, 350, 10, 350, 20]

addresses = list(map(id, lst))

print(addresses)
Explanation:
Python caches small integers.
Same values may share the same memory address.
9. Difference between map(str, [1,2,3]) and map(lambda x: str(x), [1,2,3])
Question:

Explain the difference and tell which one is faster.

Answer:
Method 1
map(str, [1, 2, 3])
Method 2
map(lambda x: str(x), [1, 2, 3])
Explanation:
map(str, ...) directly uses built-in str()
map(lambda x: str(x), ...) uses extra lambda processing
Faster:
map(str, [1, 2, 3])
10. Use map(), filter(), and reduce() in a single pipeline
Question:

Write a Python program using map(), filter(), and reduce() together in one pipeline.

Answer:
from functools import reduce

nums = [5, 10, 15, 20, 25, 30]

result = reduce(
    lambda a, b: a + b,
    filter(
        lambda x: x % 5 == 0,
        map(lambda x: x ** 2, nums)
    )
)

print(result)
Output:
2275