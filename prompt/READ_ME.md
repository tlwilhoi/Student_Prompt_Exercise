# Employee Management Application

## How to Run

1. Ensure Python is installed and available in your PATH.
2. Open a terminal in the project directory.
3. Run the application:
	```
	python Controller_Emp.py
	```

## Menu Options

1. Add Employee
2. Add Manager
3. Display All Employees
4. Edit Employee (not ID)
5. Delete Employee
6. Save Employees to CSV
7. Load Employees from CSV
8. Exit

## Input Rules

- EmployeeID: Must be unique and exactly 4 digits (e.g., 1234)
- First/Last Name: Cannot be empty or contain digits
- Department: Must be 3 uppercase letters (e.g., HRD)
- Phone Number: Must be a valid 10-digit number (formatted or unformatted)
- Manager Team Size: Must be a non-negative integer

## Sample Inputs

### Add Employee
```
Enter Employee ID: 1234
Enter First Name: John
Enter Last Name: Doe
Enter Department (3 uppercase letters): HRD
Enter Phone Number (10 digits or formatted): 123-456-7890
```

### Add Manager
```
Enter Employee ID: 5678
Enter First Name: Mary
Enter Last Name: Jones
Enter Department (3 uppercase letters): ITD
Enter Phone Number (10 digits or formatted): 0987654321
Enter Team Size: 5
```

## Sample Output

```
--- Employee List ---
EmployeeID: 1234, First Name: John, Last Name: Doe, Department: HRD, Phone Number: 1234567890
ManagerID: 5678, First Name: Mary, Last Name: Jones, Department: ITD, Phone Number: 0987654321, Team Size: 5
```

## Error Handling

- If an input is invalid, a simple error message will be shown and you will be prompted to try again.
- All general errors are handled gracefully with a user-friendly message.
