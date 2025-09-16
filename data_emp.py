import csv
from Model_Emp import Employee, Manager

def save_employees(filename, employees):
	with open(filename, 'w', newline='') as csvfile:
		writer = csv.writer(csvfile)
		# Write header
		writer.writerow(['Type', 'EmployeeID', 'FirstName', 'LastName', 'Department', 'PhoneNumber', 'TeamSize'])
		for emp in employees:
			if isinstance(emp, Manager):
				writer.writerow(['Manager', emp.employee_id, emp.first_name, emp.last_name, emp.department, emp.phone_number, emp.team_size])
			else:
				writer.writerow(['Employee', emp.employee_id, emp.first_name, emp.last_name, emp.department, emp.phone_number, ''])

def load_employees(filename):
	employees = []
	with open(filename, 'r', newline='') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			if row['Type'] == 'Manager':
				emp = Manager(row['EmployeeID'], row['FirstName'], row['LastName'], row['Department'], row['PhoneNumber'], int(row['TeamSize']))
			else:
				emp = Employee(row['EmployeeID'], row['FirstName'], row['LastName'], row['Department'], row['PhoneNumber'])
			employees.append(emp)
	return employees
