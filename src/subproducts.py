from src.task import Product


class Smartphone(Product):

    def __init__(self, name, price, description, quantity, efficiency, model, memory, color):
        super().__init__(name, price, description, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):

    def __init__(self, name, price, description, quantity, country, germination_period, color):
        super().__init__(name, price, description, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
