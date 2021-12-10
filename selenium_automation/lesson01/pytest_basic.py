class Test_PyTest:
    def setup_class(cls):
        print("\nBefore Test Class")

    def teardown_class(cls):
        print("\nAfter Test Class")

    def setup_method(self):
        print("Before Test Case")

    def teardown_method(self):
        ("After Test Case")

    def test_1(setup):
        print("Test Case 1")

    def test_2(setup):
        print("Test Case 2")
