class Employee:
	
	name = ""
	salary = 0
	
	def __init__(self, n, s):
		self.name = n
		self.salary = s 
	
	def show(self):
		print "		Employee name: {0}, salary: {1}".format(self.name, self.salary)
	
