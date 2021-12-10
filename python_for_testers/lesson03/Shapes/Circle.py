class Circle:
    def __init__(self, pi, radius):
        self.pi = pi
        self.radius = radius

    def calculate_area(self):
        return (self.pi * self.radius * self.radius)
