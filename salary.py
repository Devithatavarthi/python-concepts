#Create a class Employee with:
#instance attributes: name, base_salary
#class variable: bonus_rate = 0.1
#instance method: final_salary() → base_salary + (base_salary × bonus_rate)
#class method: update_bonus(cls, new_rate) → updates bonus for all employees
#static method: is_valid_salary(sal) → checks if salary > 0
#Create two employees, show final salaries, update bonus rate, and show again.
class employee:
    bonus_rate=0.1
    def __init__(self,name,base_salary):
        self.name=name
        self.base_salary=base_salary
    def final_salary(self):
        self.base_salary+(base_salary*bonus_rate)
    @classmethod
    def update_bonus(cls,new_rate):
        cls.bonus_rate=new_rate
    @staticmethod
    def is_valid_salary(sal):
        return sal>0
e1=employee("l",89)
e2=employee("m",120)
print(e1.)
