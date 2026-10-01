from Employee.Employee import Employee


class ClaimOfficer(Employee):

    def process_claim(self):
        print(self.name, "is processing claim")