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
        print_employees(department.get_employees())
        print()

def main():
    employee_dao = EmployeeDAO()
    department_dao = DepartmentDAO()

    # add employees
    emp1 = Employee("E001", "Gracie Sharma", 21, "HR")
    emp2 = Employee("E002", "Raghav GC", 20, "IT")
    emp3 = Employee("E003", "Yunish Shrestha", 21, "Finance")

    employee_dao.add_employee(emp1)
    employee_dao.add_employee(emp2)
    employee_dao.add_employee(emp3)

    # add departments
    dept1 = Department("D001", "HR")
    dept2 = Department("D002", "IT")
    dept3 = Department("D003", "Finance")

    department_dao.add_department(dept1)
    department_dao.add_department(dept2)
    department_dao.add_department(dept3)

    # add employees with departments
    dept1.add_employee(emp1)
    dept2.add_employee(emp2)
    dept3.add_employee(emp3)

    print("All Employees:")
    print_employees(employee_dao.get_all_employees())

    print("All Departments:")
    print_departments(department_dao.get_all_departments())

    # remove an employee
    employee_dao.remove_employee("E002")
    print("After removing an employee (E002):")
    print_employees(employee_dao.get_all_employees())

    # update employee's department
    emp1.set_department("IT")
    employee_dao.update_employee("E001", emp1)
    print("After updating employee's department (E001):")
    print_employees(employee_dao.get_all_employees())

    # update department's name
    dept2.set_name("Information Technology")
    department_dao.update_department("D002", dept2)
    print("After updating department's name (D002):")
    print_departments(department_dao.get_all_departments())

    # remove a department
    department_id = "D003" 
    department_dao.remove_department(department_id)
    print("After removing a department (D003):")
    print_departments(department_dao.get_all_departments())

if __name__ == "__main__":
    main()
