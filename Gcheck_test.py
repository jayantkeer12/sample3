import pytest
def testlogin():
    print("log in")
@pytest.mark.sanity  # these are the custom markker
def testCheck():
    print("check in")