class employee:
    def __init__(self,salary):
        self.__salary=salary
        self.log=0
    def get_salary(self):
        self.log+=1
        print(self.log)
        return self.__salary
    def set_salary(self,new_salary):
        if self.__salary<new_salary:
            print("salary increased")
            if self.__salary==new_salary:
                return new_salary
            return False
e=employee(40000)
print(e.get_salary())
print(e.set_salary(55000))
print(e.get_salary())
