class Employee:
	name = ""
	salary = 0
	def __init__(self, n, s):
		self.name = n
		self.salary = s 
	def calc_income():
		return salary * 14
	
class Company:
	employees = []
	def set_employee(self, e) :
		self.employees.append(e)


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
