class Plan:

    def __init__(self, name, price, benefits):
        self.name = name
        self.price = price
        self.benefits = benefits

    def show_info(self):

        return f"""

Plan: {self.name}
Price: ${self.price}
Benefits: {self.benefits}
"""

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price