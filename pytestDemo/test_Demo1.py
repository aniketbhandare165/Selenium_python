# Any pytest file should start with test_ or end with _test
# pytest method names should start with test
#Any code should be wrapped in method only
# method name should have sense
# -k stands for method names execution, -s logs in out put -v stands for more info metadata
# you can run specific file with py.test <filename>
# you can mark (tag) test @pytest.mark.smoke and then run with -m
# you can skip tests with @pytest.mark.skip
# if we need to run any test case because it is prerequisite for next test case and we don't wat it to show fail mark it like
# @pytest.mark.xfail
# fixture are used as setup and tear down methods for tear cases - conftest file to generalize fixture
# and make it available to all test cases
# datadriven and parameterization can be done with return statements in tuple format
#when you define fixture scope to class only, it will run once before class is initiated and at the end after class level is executed

import pytest


@pytest.mark.smoke
def test_firstprogram(setup):
    print("Hello")
@pytest.mark.xfail
def test_GreetCreditCard():
    print("Good morning")

def test_crossBrowser(crossBrowser):
    # print(crossBrowser)
    print(crossBrowser[1])