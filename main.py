from clases.member import Member
from clases.trainer import Trainer
from clases.plan import Plan
from clases.cashpayment import CashPayment
from clases.cardpayment import CardPayment
from clases.enrollment import Enrollment

members = []
trainers = []
plans = []

basic_plan = Plan(
    "Basic",
    80000,
    "1 training per day - 5 days per week"
)

standard_plan = Plan(
    "Standard",
    100000,
    "2 trainings per day - All week - nutrition guide"
)

premium_plan = Plan(
    "Premium",
    120000,
    "Unlimited access - nutrition guide - personal trainer"
)

plans.append(basic_plan)
plans.append(standard_plan)
plans.append(premium_plan)

enrollments = []

def show_menu():
    print("\n GYM SYSTEM")
    print("1. Add member")
    print("2. Add trainer")
    print("3. Show members")
    print("4. Show trainers")
    print("5. Show plans")
    print("6. Create enrollment")
    print("7. Exit")

def add_member():

    print("\n Add member")

    name = input("Enter member name: ")
    age = int(input("Enter member age: "))
    weight = float(input("Enter member weight: "))

    for member in members:

        if(member.get_name() == name):

            print("Member already exists")
            return

    member = Member(name, age, weight)

    members.append(member)

    print("Member added successfully")

def add_trainer():
    print("\n Add trainer")

    name = input("Enter trainer name: ")
    specialty = input("Enter trainer specialty: ")

    trainer = Trainer(name, specialty)

    trainers.append(trainer)

    print("Trainer added successfully")

def show_members():
    print("\n Members")

    for member in members:
        print(member.show_info())

def show_trainers():
    print("\n Trainers")

    for trainer in trainers:
        print(trainer.show_info())

def show_plans():
    print("\n Plans")

    for plan in plans:
        print(plan.show_info())

def create_enrollment():

    print("\n Create enrollment")

    member_name = input("Enter member name: ")

    member_found = None

    for member in members:

        if(member.get_name() == member_name):

            member_found = member
            break

    if(member_found is None):

        print("Member not found")
        return

    print("\n Available plans:")

    for plan in plans:
        print(plan.show_info())

    plan_name = input("\n Enter plan name: ")

    plan_found = None

    for plan in plans:

        if(plan.get_name() == plan_name):

            plan_found = plan
            break

    if(plan_found is None):

        print("Plan not found")
        return

    enrollment = Enrollment(member_found, plan_found)

    total = plan_found.get_price()

    print(f"\n Total: {total}")

    payment = None

    while(payment is None):

        payment_type = input("Enter payment method (cash/card): ")

        if(payment_type == "cash"):

            cash_received = float(input("Enter cash received: "))

            payment = CashPayment(total, cash_received)

        elif(payment_type == "card"):

            card_number = input("Enter card number: ")

            payment = CardPayment(total, card_number)

        else:

            print("Invalid payment method")

    print(payment.process_payment())

    enrollment.set_payment(payment)

    enrollments.append(enrollment)

    print("Enrollment created successfully")

    enrollment.show_info()

option = 0

while(option != 7):

    show_menu()

    option = int(input("\n Enter an option (1-7): "))

    if(option == 1):
        add_member()

    elif(option == 2):
        add_trainer()

    elif(option == 3):
        show_members()

    elif(option == 4):
        show_trainers()

    elif(option == 5):
        show_plans()

    elif(option == 6):
        create_enrollment()

    elif(option == 7):
        print("\n Closing system")

    else:
        print("\n Invalid option")

print("Bye")