class Employee:
	
	name = ""
	salary = 0
	
	def __init__(self, n, s):
		self.name = n
		self.salary = s 
	
	def show(self):
		print "		Employee name: {0}, salary: {1}".format(self.name, self.salary)
	
class Company:

	name = ""
	employees = []

	def __init__(self, n, listOfE) :
		self.name = n
		self.employees = listOfE

	def append_employee(self, e) :
		self.employees.append(e)

	def show(self) :
		print "Company name is: {0}".format(self.name)
		for e in self.employees :
			e.show()


e1 = Employee("Jonh", 1250)
e2 = Employee("Mary", 1700)
star = Company("star", [e1, e2])

e3 = Employee("Bob", 2000)
e4 = Employee("Alice", 2500)
dust = Company("dust", [e3, e4])

companies = [star, dust]
for c in companies:
	c.show()
		
