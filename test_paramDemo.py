import pytest
@pytest.mark.parametrize("a,b,final",[(2,6,8)])
def testlogin(a,b,final):
    assert a+b==final
