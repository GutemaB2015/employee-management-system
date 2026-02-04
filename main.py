from database import create_table
from employee import add_employee, list_employees, delete_employee
from employee import Employee

def main():
    create_table()

    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. List Employees")
        print("3. Delete Employee")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Name: ")
            department = input("Department: ")
            email = input("Email: ")

            employee = Employee(name, department, email)
            add_employee(employee)
            print("Employee added successfully.")

        elif choice == "2":
            list_employees()

        elif choice == "3":
            emp_id = input("Enter employee ID to delete: ")
            delete_employee(emp_id)
            print("Employee deleted successfully.")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
