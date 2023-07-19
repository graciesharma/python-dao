class DepartmentDAO:
    def __init__(self):
        self.department_data = {}

    def add_department(self, department):
        self.department_data[department.get_dept_id()] = department

    def remove_department(self, dept_id):
        del self.department_data[dept_id]

    def update_department(self, dept_id, new_department):
        self.department_data[dept_id] = new_department

    def get_department(self, dept_id):
        return self.department_data.get(dept_id)

    def get_all_departments(self):
        return list(self.department_data.values())
