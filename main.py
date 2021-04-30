#
# Learning Python OOP
#

class Employee:
	num_of_employees = 0
	raise_amount = 1.04

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'

		Employee.num_of_employees += 1

	def __repr__(self):
		return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

	# def __str__(self):
	# 	pass

	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)

	@classmethod
	def set_raise_amt(cls, amount):
		cls.raise_amount = amount

	@classmethod
	def from_string(cls, emp_str):
		first, last, pay = emp_str.split('-')
		return cls(first, last, pay)

	@staticmethod
	def is_workday(day):
		if day.weekday() == 5 or day.weekday() == 6:
			return False
		return True


class Developer(Employee):
	raise_amount = 1.10

	def __init__(self, first, last, pay, programming_lang):
		super().__init__(first, last, pay)
		self.programming_lang = programming_lang


class Manager(Employee):

	def __init__(self, first, last, pay, employees=None):
		super().__init__(first, last, pay)
		if employees is None:
			self.employees = []
		else:
			self.employees = employees

	def add_employee(self, employee):
		if employee not in self.employees:
			self.employees.append(employee)

	def rmv_employee(self, employee):
		if employee in self.employees:
			self.employees.remove(employee)

	def print_employees(self):
		for employee in self.employees:
			print('⇾', employee.fullname())


emp_1 = Employee('John', 'Lennon', 50000)
emp_2 = Employee('Salil', 'Chowdhury', 60000)

print(emp_1)
