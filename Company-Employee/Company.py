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

