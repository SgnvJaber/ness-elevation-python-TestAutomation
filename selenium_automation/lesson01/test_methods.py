import pytest

def setup_module(module):
    print("Setup module")
def teardown_module(module):
    print("teardown module")

class Test_PYTest1:
    def setup_class(self):
        print("setup class a")
    def test_a1(self):
        print("test a1")
class Test_PYTest2:
    def setup_class(self):
        print("setup class v")
    def test_a1(self):
        print("test b1")





class Test_PyTest:
    def setup_method(self):
        print("\nBefore Test Case")

    def teardown_method(self):
        print("\nAfter Test Case")

    def setup_class(self):
        print("\nBefore Test Class")

    def teardown_class(self):
        print("\nAfter Test Class")

    def test_demo(self):
        print("This is a demo")

    def test_demo2(self):
        print("This is demo2")
