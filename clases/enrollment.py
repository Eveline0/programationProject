class Enrollment:

    def __init__(self, member, plan):
        self.member = member
        self.plan = plan
        self.payment = None

    def set_payment(self, payment):
        self.payment = payment

    def show_info(self):

        print("\n Enrollment information")
        print(self.member.show_info())
        print(self.plan.show_info())