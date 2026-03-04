#Create a class Employee with attributes name and company_name = "TechCorp".
#Add a class method change_company(cls, new_name) to update the company name for all employees.
#Demonstrate how this change affects all instances
class employee:
    company_name="TechCrop"
    def __init__(self,name):
        self.name=name
    @classmethod
    def change_company(cls,new_name):
        cls.company_name==new_name
e1=employee("j")
e2=employee("k")
employee.change_company("cvtech")
print(e1.company_name)
print(e2.company_name)
