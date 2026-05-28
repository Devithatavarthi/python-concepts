#1. Create a class Person whose constructor takes age as an argument.
# Raise a ValueError if the age is less than 0.
class Person:
    def __init__(self, age):
        if age < 0:
            raise ValueError("Age cannot be negative")
        self.age = age

try:
    p = Person(-5)
except ValueError as e:
    print(e)
#2. Write a function named find_length(obj) that uses a loop to calculate the length of the given object without using the built-in len() function.
# The function should return the calculated length if the object is iterable.
# If a non-iterable object such as an integer is passed, the function should raise and handle a TypeError.
def find_length(obj):
    try:
        count = 0
        for i in obj:
            count += 1
        return count
    except TypeError:
        print("TypeError: Integer object is not iterable")

print(find_length([1, 2, 3, 4]))
print(find_length(10))
#3. Create a class Student with an attribute marks.
# Implement a method set_marks(marks) that raises a
# ValueError if marks are not in the range 0 to 100.
class Student:
    def set_marks(self, marks):
        if marks < 0 or marks > 100:
            raise ValueError("Marks should be between 0 and 100")
        self.marks = marks

try:
    s = Student()
    s.set_marks(120)
except ValueError as e:
    print(e)
 #4. Create a custom exception named InvalidAgeError.
# Create a class Voter with a method check_eligibility(age)
# that raises this exception if age is less than 18.
class InvalidAgeError(Exception):
    pass

class Voter:
    def check_eligibility(self, age):
        if age < 18:
            raise InvalidAgeError("Not eligible to vote")
        print("Eligible to vote")

try:
    v = Voter()
    v.check_eligibility(16)
except InvalidAgeError as e:
    print(e)
#5. Create a class BankAccount with an attribute balance.
# Implement a method withdraw(amount) that raises an exception
# if the withdrawal amount is greater than the available balance.
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise Exception("Insufficient balance")
        self.balance -= amount
        print("Remaining Balance:", self.balance)

try:
    b = BankAccount(5000)
    b.withdraw(7000)
except Exception as e:
    print(e)
#6. Create a class PasswordValidator with a method validate(password).
# Raise an exception if the passwo0rd length is less than 8 characters.
class PasswordValidator:
    def validate(self, password):
        if len(password) < 8:
            raise Exception("Password must contain at least 8 characters")
        print("Valid Password")

try:
    p = PasswordValidator()
    p.validate("abc12")
except Exception as e:
    print(e)
#7. Create a class UserInput with a method get_integer(value).
# Handle ValueError and TypeError using separate except blocks.
class UserInput:
    def get_integer(self, value):
        try:
            number = int(value)
            print("Integer:", number)
        except ValueError:
            print("ValueError: Invalid value")
        except TypeError:
            print("TypeError: Invalid type")

u = UserInput()
u.get_integer("123")
u.get_integer("abc")
u.get_integer(None)
#8. Create a base class Shape with a method area() that raises NotImplementedError.
# Create a child class Rectangle that overrides and implements the area method.
class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement area method")

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

r = Rectangle(5, 4)
print("Area:", r.area())
#9. Create a class Service with a method that calls another method which raises an exception.
# Catch and handle the exception in the Service class.
class Service:
    def risky_method(self):
        raise Exception("Something went wrong")

    def execute(self):
        try:
            self.risky_method()
        except Exception as e:
            print("Handled Exception:", e)

s = Service()
s.execute()
#10. Create a class Transaction with a method process()
# that uses try, except, and finally blocks to ensure a cleanup message is always printed.
class Transaction:
    def process(self):
        try:
            amount = int(input("Enter amount: "))
            print("Transaction Successful:", amount)
        except ValueError:
            print("Invalid input")
        finally:
            print("Cleanup completed")

t = Transaction()
t.process()
#11. Create a class LoginSystem with a method login(password) that raises an
# exception for an incorrect password and handles the exception outside the class.
class LoginSystem:
    def login(self, password):
        if password != "admin123":
            raise Exception("Incorrect Password")
        print("Login Successful")

try:
    l = LoginSystem()
    l.login("wrongpass")
except Exception as e:
    print(e)