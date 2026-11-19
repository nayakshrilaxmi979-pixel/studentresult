from cie2 import studentresult
def test_total():
    assert(80, 90, 70)[0] == 240

def test_average():
    assert(80, 90, 70)[1] == 80

def test_percentage():
    assert(80,90,70)[2]== 80