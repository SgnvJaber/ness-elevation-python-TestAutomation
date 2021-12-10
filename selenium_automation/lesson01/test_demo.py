import pytest

class Test_Demo:
    @classmethod
    def setup_class(cls):
        print("\nThis is Setup")

    @classmethod
    def teardown_class(cls):
        print("\nAfter Class")

    def test_demo01(self):
        print("Hello World")

    def test_demo02(self):
        print("Good Morning")

    def test_demo03(self):
        print("This Is A Test For fixture")

