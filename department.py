class Department:
    def __init__(self, dept_id, name):
        self.dept_id = dept_id
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee):
        self.employees.remove(employee)

    def update_employee(self, employee, new_employee):
        index = self.employees.index(employee)
        self.employees[index] = new_employee

    def get_employees(self):
        return self.employees

    def get_dept_id(self):
        return self.dept_id

    def set_dept_id(self, dept_id):
        self.dept_id = dept_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name
