class Employee:

    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name

    def display_employee(self):
        print("Employee ID:", self.employee_id)
        print("Employee Name:", self.name)