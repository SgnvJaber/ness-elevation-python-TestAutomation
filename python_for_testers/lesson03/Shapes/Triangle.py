class Triangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return ((self.height * self.width) / 2)
