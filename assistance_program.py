class AssistanceProgram:

    def __init__(self, program_name, status, grant_amount, eligible_treatments):
        self.name = program_name
        self.status = status
        self.grant_amount = grant_amount
        self.eligible_treatments = eligible_treatments

    def concat_treatments(self):
        return ','.join(self.eligible_treatments)

    def get_program_as_db_row(self):
        return self.name, self.eligible_treatments, self.status, self.grant_amount

    # helper function for testing
    # todo remove after done
    def print_info(self):
        print("Assistance Program Name: " + self.name + "\n")
        print("Eligible Treatments: ")
        print(*self.eligible_treatments, sep=", ")
        print("\n")
        print("Status: " + self.status + "\n")
        print("Grant Amount: " + self.grant_amount + "\n\n")
