
from hello import sub_xy

def test_sub_xy():
    assert 0 == sub_xy(1, 1)
    assert 2 == sub_xy(3, 1)

test_sub_xy()