from abc import ABC, abstractmethod

class Person(ABC):
    @abstractmethod
    def showName(self):
        pass

    def showAge(self):
        print("The Age is 30")


class Employee(Person):

    def showName(self):
        print("Mayank")
        
    def showDesignation(self):
        print("This is a Developer...")

employeeOne = Employee()
employeeOne.showDesignation()
employeeOne.showName()
employeeOne.showAge()