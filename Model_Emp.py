
class Employee:
	_used_ids = set()
	def __str__(self):
		return (f"EmployeeID: {self.employee_id}, First Name: {self.first_name}, Last Name: {self.last_name}, "
				f"Department: {self.department}, Phone Number: {self.phone_number}")
	def __init__(self, employee_id, first_name, last_name, department, phone_number):
		# Ensure EmployeeID is a unique 4-digit number
		if not (str(employee_id).isdigit() and len(str(employee_id)) == 4):
			raise ValueError("EmployeeID must be a 4-digit number.")
		if employee_id in Employee._used_ids:
			raise ValueError(f"EmployeeID {employee_id} is already in use.")
		Employee._used_ids.add(employee_id)
		self.employee_id = employee_id
		self.first_name = first_name
		self.last_name = last_name
		self.department = department
		self.phone_number = phone_number

	@property
	def first_name(self):
		return self._first_name

	@first_name.setter
	def first_name(self, value):
		if not value or any(char.isdigit() for char in value):
			raise ValueError("First Name cannot be empty or contain digits.")
		self._first_name = value

	@property
	def last_name(self):
		return self._last_name

	@last_name.setter
	def last_name(self, value):
		if not value or any(char.isdigit() for char in value):
			raise ValueError("Last Name cannot be empty or contain digits.")
		self._last_name = value

	@property
	def department(self):
		return self._department

	@department.setter
	def department(self, value):
		if not (value.isupper() and len(value) == 3 and value.isalpha()):
			raise ValueError("Department must be 3 uppercase letters.")
		self._department = value

	@property
	def phone_number(self):
		return self._phone_number

	@phone_number.setter
	def phone_number(self, value):
		# Remove all non-digit characters
		digits = ''.join(filter(str.isdigit, value))
		if len(digits) != 10:
			raise ValueError("Phone number must be a valid 10-digit number.")
		self._phone_number = digits
class Manager(Employee):
	def __str__(self):
		return (f"ManagerID: {self.employee_id}, First Name: {self.first_name}, Last Name: {self.last_name}, "
				f"Department: {self.department}, Phone Number: {self.phone_number}, Team Size: {self.team_size}")

	def __init__(self, employee_id, first_name, last_name, department, phone_number, team_size):
		super().__init__(employee_id, first_name, last_name, department, phone_number)
		self.team_size = team_size

	@property
	def team_size(self):
		return self._team_size

	@team_size.setter
	def team_size(self, value):
		if not isinstance(value, int) or value < 0:
			raise ValueError("Team size must be a non-negative integer.")
		self._team_size = value
		

		