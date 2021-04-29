class Employee:
	pass


emp_1 = Employee()
emp_2 = Employee()

print(emp_1)
print(emp_2)

emp_1.first = 'Hasan'
emp_1.last = 'Nahiyan'
emp_1.email = 'hasan.nahiyan.nobel@gmail.com'
emp_1.pay = 50000

emp_2.first = 'Test'
emp_2.last = 'User'
emp_2.email = 'test.user@gmail.com'
emp_2.pay = 60000

print(emp_1.email)
print(emp_2.email)
