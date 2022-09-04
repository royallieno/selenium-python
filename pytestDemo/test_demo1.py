# Any pytest file should start with test_ or end with _test
# Pytest method names should starts with test
# Any code should wrapped in method only
# Method name should have sense
# -k stands for method names execution, -s logs in output, -v stands for more info metadata
# We can run specific file with py.test <filename>
# We can mark (tag) tests as @pytest.mark.smoke and then run with -m
# We can skip tests with @pytest.mark.skip
# If we want to run a tests and don't want the result for it --> @pytest.mark.xfail
# Fixtures are used for setup and tear down methods cases- conftest file to generalize fixtures
# and make it available to all test cases

import pytest


@pytest.mark.smoke
def test_fistProgram(setup):
    print("Hello")


@pytest.mark.xfail
def test_secondGreetCreditCard():
    print("Good Morning")


def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])