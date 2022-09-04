# Any pytest file should start with test_ or end with _test
# Pytest method names should starts with test
# Any code should wrapped in method only
# Method name should have sense
# -k stands for method names execution, -s logs in output, -v (verbos) stands for more info metadata
# We can run specific file with py.test <filename>
# We can mark (tag) tests with @pytest.mark.smoke and then run with -m
# We can skip tests with @pytest.mark.skip
# If we want to run a tests and don't want the result for it --> @pytest.mark.xfail
# Fixtures are used for setup and tear down methods cases- conftest file to generalize fixtures
# and make it available to all test cases (fixtures name into parameters of method)
# Datadriven and parameterization can be done with return statements in tuple format
# When we define fixture scope to class only, it will run once before class is initiate and at the end
# -----------------------------mentor@rahulshettyacademy.com-----------------------------------


import pytest


@pytest.mark.smoke
# @pytest.mark.skip
def test_fistProgram():
    message = "Hello"
    assert message == "Hi", "Test failed because strings do not match"


def test_firstGreetCreditCard():
    a, b = 4, 6
    assert a+2 == b, "Addition do not matched"


