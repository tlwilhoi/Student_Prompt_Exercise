def display_menu():
    print("\nEmployee Management System")
    print("1. Add Employee")
    print("2. Add Manager")
    print("3. Display All Employees")
    print("4. Edit Employee (not ID)")
    print("5. Delete Employee")
    print("6. Save Employees to CSV")
    print("7. Load Employees from CSV")
    print("8. Exit")

def show_message(message):
    print(f"\n{message}")

def prompt_employee_input():
    while True:
        try:
            employee_id = input("Enter Employee ID: ")
            first_name = input("Enter First Name: ")
            last_name = input("Enter Last Name: ")
            department = input("Enter Department (3 uppercase letters): ")
            phone_number = input("Enter Phone Number (10 digits or formatted): ")
            return employee_id, first_name, last_name, department, phone_number
        except Exception as e:
            show_message(f"Error: {e}. Please try again.")

def prompt_manager_input():
    while True:
        try:
            employee_id, first_name, last_name, department, phone_number = prompt_employee_input()
            team_size = input("Enter Team Size: ")
            if not team_size.isdigit() or int(team_size) < 0:
                raise ValueError("Team Size must be a non-negative integer.")
            return employee_id, first_name, last_name, department, phone_number, int(team_size)
        except Exception as e:
            show_message(f"Error: {e}. Please try again.")

def display_employees(employees):
    print("\n--- Employee List ---")
    if not employees:
        show_message("No employees to display.")
        return
    for emp in employees:
        try:
            print(emp)
        except Exception as e:
            show_message(f"Error displaying employee: {e}")


