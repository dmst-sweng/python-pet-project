from Company import Company
from Employee import Employee

e1 = Employee("Jonh", 1250)
e2 = Employee("Mary", 1700)
star = Company("star", [e1, e2])

e3 = Employee("Bob", 2000)
e4 = Employee("Alice", 2500)
dust = Company("dust", [e3, e4])

companies = [star, dust]
for c in companies:
	c.show()
		
