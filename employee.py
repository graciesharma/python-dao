class Employee:
    def __init__(self, emp_id, name, age, department):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.department = department

    def get_emp_id(self):
        return self.emp_id

    def set_emp_id(self, emp_id):
        self.emp_id = emp_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_department(self):
        return self.department

    def set_department(self, department):
        self.department = department
