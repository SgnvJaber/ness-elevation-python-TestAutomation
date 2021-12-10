from python_for_testers.lesson03.Mobile.MobileDevice import MobileDevice

device1 = MobileDevice("Galaxy A31", "A", "11.2", True, 1000, 73, 159)
device1.print_parameters()
print("Area:", device1.calculateArea())
device1.pictureQuality()
device2 = MobileDevice("Iphone 11 Prop", "I", "14.2", True, 4000, 70, 143)
device2.print_parameters()
print("Area:", device2.calculateArea())
device2.pictureQuality()
device3 = MobileDevice("Bad Phone", "A", "0.2", False, 40, 10, 13)
device3.print_parameters()
print("Area:", device3.calculateArea())
device3.pictureQuality()
