class Member:

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def show_info(self):
        return f"Name: {self.name}, Age: {self.age}, Weight: {self.weight}"

    def get_name(self):
        return self.name