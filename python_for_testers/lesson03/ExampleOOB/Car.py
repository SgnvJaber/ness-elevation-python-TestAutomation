class Car:
    # manufacturer=None
    # model=None
    # year=None
    # price=None
    # hasAbs=None

    def __init__(self, manufacturer, model, year, price, hasAbs):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.price = price
        self.hasAbs = hasAbs

    def print(self):
        print(self.manufacturer + " " + self.model + " " + str(self.year) + " " + str(self.price))
        print(self.getAbs())

    def getAbs(self):
        if (self.hasAbs):
            return "Car has ABS System"
        else:
            return "Car does NOT have ABS System"
