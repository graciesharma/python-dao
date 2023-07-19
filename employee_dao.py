class EmployeeDAO:
    def __init__(self):
        self.employee_data = {}

    def add_employee(self, employee):
        self.employee_data[employee.get_emp_id()] = employee

    def remove_employee(self, employee_id):
        del self.employee_data[employee_id]

    def update_employee(self, employee_id, new_employee):
        self.employee_data[employee_id] = new_employee

    def get_employee(self, employee_id):
        return self.employee_data.get(employee_id)

    def get_all_employees(self):
        return list(self.employee_data.values())
