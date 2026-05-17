class Trainer:

    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty

    def show_info(self):
        return f"Name: {self.name}, Specialty: {self.specialty}"