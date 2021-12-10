class MobileDevice:

    def __init__(self,model, os, version, has_flash, price,screenWidth,screenHeight):
        self.model=model
        self.os=os
        self.version=version
        self.has_flash=has_flash
        self.price=price
        self.screenWidth=screenWidth
        self.screenHeight = screenHeight

    def print_parameters(self):
        print(self.model + " " + self.os + " " + self.version + " " + str(self.has_flash) + " " + str(self.price))

    def calculateArea(self):
        return self.screenWidth * self.screenHeight

    def pictureQuality(self):
        if (self.has_flash):
            print("Good Quality")
        else:
            print("Bad Quality")
