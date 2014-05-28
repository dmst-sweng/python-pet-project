from Company import Company
from Employee import Employee

#if __name__ == "main":
star = Company()
john = Employee("Jonh", 1250)
star.set_employee(john)
mary = Employee("Mary", 1700)
star.set_employee(mary)
bob = Employee("Bob", 2000)
star.set_employee(bob)
alice = Employee("Alice", 2500)
star.set_employee(alice)
for e in star.employees:
	print "Name {0}, salary: {1}".format(e.name, e.salary)
