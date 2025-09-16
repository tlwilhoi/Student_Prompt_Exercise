from Model_Emp import Employee, Manager
from data_emp import save_employees, load_employees
from View_Emp import display_menu, show_message, prompt_employee_input, prompt_manager_input, display_employees

def main():
    employees = []
    while True:
        display_menu()
        choice = input("Select an option: ")
        if choice == '1':
            try:
                emp_data = prompt_employee_input()
                emp = Employee(*emp_data)
                employees.append(emp)
                show_message("Employee added successfully.")
            except Exception as e:
                show_message(f"Error adding employee: {e}")
        elif choice == '2':
            try:
                mgr_data = prompt_manager_input()
                mgr = Manager(*mgr_data)
                employees.append(mgr)
                show_message("Manager added successfully.")
            except Exception as e:
                show_message(f"Error adding manager: {e}")
        elif choice == '3':
            display_employees(employees)
        elif choice == '4':
            display_employees(employees)
            emp_id = input("Enter the EmployeeID of the employee to edit: ")
            try:
                emp = None
                for e in employees:
                    if e.employee_id == emp_id:
                        emp = e
                        break
                if emp is None:
                    show_message("EmployeeID not found.")
                else:
                    show_message("Editing employee (ID cannot be changed):")
                    if isinstance(emp, Manager):
                        _, first_name, last_name, department, phone_number, team_size = prompt_manager_input()
                        emp.first_name = first_name
                        emp.last_name = last_name
                        emp.department = department
                        emp.phone_number = phone_number
                        emp.team_size = team_size
                    else:
                        _, first_name, last_name, department, phone_number = prompt_employee_input()
                        emp.first_name = first_name
                        emp.last_name = last_name
                        emp.department = department
                        emp.phone_number = phone_number
                    show_message("Employee updated successfully.")
            except Exception as e:
                show_message(f"Error editing employee: {e}")
        elif choice == '5':
            display_employees(employees)
            emp_id = input("Enter the EmployeeID of the employee to delete: ")
            try:
                found = False
                for i, emp in enumerate(employees):
                    if emp.employee_id == emp_id:
                        del employees[i]
                        show_message("Employee deleted successfully.")
                        found = True
                        break
                if not found:
                    show_message("EmployeeID not found.")
            except Exception as e:
                show_message(f"Error deleting employee: {e}")
        elif choice == '6':
            filename = input("Enter filename to save employees: ")
            try:
                save_employees(filename, employees)
                show_message("Employees saved successfully.")
            except Exception as e:
                show_message(f"Error saving employees: {e}")
        elif choice == '7':
            filename = input("Enter filename to load employees: ")
            try:
                employees = load_employees(filename)
                show_message("Employees loaded successfully.")
            except Exception as e:
                show_message(f"Error loading employees: {e}")
        elif choice == '8':
            show_message("Exiting program.")
            break
        else:
            show_message("Invalid option. Please try again.")

import datetime

def log_test(message):
    with open("test_log.txt", "a") as log:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.write(f"[{timestamp}] {message}\n")

def run_tests():
    log_test("--- Begin Employee/Manager Tests ---")
    # Valid Employee
    try:
        emp1 = Employee("1234", "John", "Doe", "HRD", "1234567890")
        log_test("PASS: Valid Employee created.")
    except Exception as e:
        log_test(f"FAIL: Valid Employee creation failed: {e}")
    # Invalid Employee (ID not 4 digits)
    try:
        emp2 = Employee("12", "Jane", "Smith", "ENG", "1234567890")
        log_test("FAIL: Invalid EmployeeID accepted.")
    except Exception as e:
        log_test(f"PASS: Invalid EmployeeID rejected: {e}")
    # Invalid Employee (ID duplicate)
    try:
        emp3 = Employee("1234", "Jake", "Long", "FIN", "1234567890")
        log_test("FAIL: Duplicate EmployeeID accepted.")
    except Exception as e:
        log_test(f"PASS: Duplicate EmployeeID rejected: {e}")
    # Invalid Employee (First name contains digit)
    try:
        emp4 = Employee("2345", "J0hn", "Doe", "HRD", "1234567890")
        log_test("FAIL: Invalid first name accepted.")
    except Exception as e:
        log_test(f"PASS: Invalid first name rejected: {e}")
    # Invalid Employee (Department not 3 uppercase letters)
    try:
        emp5 = Employee("3456", "Alice", "Brown", "hrd", "1234567890")
        log_test("FAIL: Invalid department accepted.")
    except Exception as e:
        log_test(f"PASS: Invalid department rejected: {e}")
    # Invalid Employee (Phone number not 10 digits)
    try:
        emp6 = Employee("4567", "Bob", "White", "MKT", "12345")
        log_test("FAIL: Invalid phone number accepted.")
    except Exception as e:
        log_test(f"PASS: Invalid phone number rejected: {e}")
    # Valid Manager
    try:
        mgr1 = Manager("5678", "Mary", "Jones", "ITD", "0987654321", 5)
        log_test("PASS: Valid Manager created.")
    except Exception as e:
        log_test(f"FAIL: Valid Manager creation failed: {e}")
    # Invalid Manager (Negative team size)
    try:
        mgr2 = Manager("6789", "Sam", "Hill", "ITD", "0987654321", -2)
        log_test("FAIL: Invalid team size accepted.")
    except Exception as e:
        log_test(f"PASS: Invalid team size rejected: {e}")
    log_test("--- End Employee/Manager Tests ---")

if __name__ == "__main__":
    run_tests()
    try:
        main()
    except Exception:
        print("An error occurred. Please try again.")