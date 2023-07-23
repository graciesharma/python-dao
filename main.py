from employee import Employee
from department import Department
from employee_dao import EmployeeDAO
from department_dao import DepartmentDAO

def print_employees(employees):
    for employee in employees:
        print("Employee ID:", employee.get_emp_id())
        print("Name:", employee.get_name())
        print("Age:", employee.get_age())
        print("Department:", employee.get_department())
        print()

def print_departments(departments):
    for department in departments:
        print("Department ID:", department.get_dept_id())
        print("Name:", department.get_name())
        print("Employees:")
        for emp in department.get_employees():
            print("  - Employee ID:", emp.get_emp_id()) 
            print("    Name:", emp.get_name())
            print("    Age:", emp.get_age())
        print()

def associate_employee_in_department(employee_dao, department_dao):
    print("Available Employees:")
    print_employees(employee_dao.get_all_employees())

    emp_id = input("Enter Employee ID to associate: ")
    employee = employee_dao.get_employee(emp_id)
    if not employee:
        print("Employee not found.")
        return

    print("Available Departments:")
    print_departments(department_dao.get_all_departments())

    dept_id = input("Enter Department ID to associate: ")
    department = department_dao.get_department(dept_id)
    if not department:
        print("Department not found.")
        return

    department.add_employee(employee)
    employee.set_department(dept_id)

    department_dao.update_department(dept_id, department)
    employee_dao.update_employee(emp_id, employee)

    print(f"Employee {employee.get_name()} associated with Department {department.get_name()} successfully!")

def main():
    employee_dao = EmployeeDAO()
    department_dao = DepartmentDAO()

    emp1 = Employee("E001", "Gracie Sharma", 21, None)
    emp2 = Employee("E002", "Raghav GC", 20, None)
    emp3 = Employee("E003", "Yunish Shrestha", 21, None)

    employee_dao.add_employee(emp1)
    employee_dao.add_employee(emp2)
    employee_dao.add_employee(emp3)

    dept1 = Department("D001", "HR")
    dept2 = Department("D002", "IT")
    dept3 = Department("D003", "Finance")

    department_dao.add_department(dept1)
    department_dao.add_department(dept2)
    department_dao.add_department(dept3)

    dept1.add_employee(emp1)
    dept2.add_employee(emp2)
    dept3.add_employee(emp3)

    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. Remove Employee")
        print("3. Update Employee Profile")
        print("4. View Employee Details")
        print("5. Add Department")
        print("6. Remove Department")
        print("7. Update Department")
        print("8. View Department Details")
        print("9. Associate Employee in Department")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            emp_id = input("Enter Employee ID: ")
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            department = input("Enter Department: ")
            new_employee = Employee(emp_id, name, age, department)
            employee_dao.add_employee(new_employee)
            print("Employee added successfully!")

        elif choice == "2":
            emp_id = input("Enter Employee ID to remove: ")
            employee_dao.remove_employee(emp_id)
            print("Employee removed successfully!")

        elif choice == "3":
            emp_id = input("Enter Employee ID to update: ")
            employee = employee_dao.get_employee(emp_id)
            if not employee:
                print("Employee not found.")
            else:
                name = input("Enter new Name: ")
                age = int(input("Enter new Age: "))
                department = input("Enter new Department: ")
                employee.set_name(name)
                employee.set_age(age)
                employee.set_department(department)
                employee_dao.update_employee(emp_id, employee)
                print("Employee profile updated successfully!")

        elif choice == "4":
            print("All Employees:")
            print_employees(employee_dao.get_all_employees())

        elif choice == "5":
            dept_id = input("Enter Department ID: ")
            name = input("Enter Name: ")
            new_department = Department(dept_id, name)
            department_dao.add_department(new_department)
            print("Department added successfully!")

        elif choice == "6":
            dept_id = input("Enter Department ID to remove: ")
            department_dao.remove_department(dept_id)
            print("Department removed successfully!")

        elif choice == "7":
            dept_id = input("Enter Department ID to update: ")
            department = department_dao.get_department(dept_id)
            if not department:
                print("Department not found.")
            else:
                name = input("Enter new Name: ")
                department.set_name(name)
                department_dao.update_department(dept_id, department)
                print("Department updated successfully!")

        elif choice == "8":
            print("All Departments:")
            print_departments(department_dao.get_all_departments())

        elif choice == "9":
            associate_employee_in_department(employee_dao, department_dao)

        elif choice == "0":
            print("Exiting Employee Management System.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
