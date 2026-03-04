#Create a class Student with instance attributes name and marks.
#Add an instance method is_passed() that returns True if marks > 40.
#Then create 2 student objects and print whether each has passed or failed.
class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def is_passed(self):
        return self.marks>40
s1=student("h",89)
s2=student("j",67)
print(s1.name,"passed" if s1.is_passed() else "failed")
print(s2.name,"passed" if s2.is_passed() else "failed")