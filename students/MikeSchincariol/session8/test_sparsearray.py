from sparsearray import Sparsearray


def test_sa_creation():
    sa = Sparsearray([1,2,0,0,0,0,3,0,0,4])
    assert sa.__repr__() == "Sparsearray([1, 2, 0, 0, 0, 0, 3, 0, 0, 4])"

def test_sa_len():
    sa = Sparsearray([1,2,0,0,0,0,3,0,0,4])
    assert len(sa) == 10

def test_sa_setitem0():
    sa = Sparsearray([1,2,0,0,0,0,3,0,0,4])
    sa[5] = 12
    assert sa.__repr__() == "Sparsearray([1, 2, 0, 0, 0, 12, 3, 0, 0, 4])"

def test_sa_setitem1():
    sa = Sparsearray([1,2,0,0,0,0,3,0,0,4])
    sa[3] = 0
    assert sa.__repr__() == "Sparsearray([1, 2, 0, 0, 0, 0, 3, 0, 0, 4])"

def test_sa_setitem2():
    sa = Sparsearray([1,2,0,0,0,0,3,0,0,4])
    sa[0] = 0
    assert sa.__repr__() == "Sparsearray([0, 2, 0, 0, 0, 0, 3, 0, 0, 4])"

def test_sa_getitem0():
    sa = Sparsearray([1,2,0,0,0,0,3,0,0,4])
    assert sa[13] == None

def test_sa_getitem0():
    sa = Sparsearray([1,2,0,0,0,0,3,0,0,4])
    assert sa[0] == 1

def test_sa_getitem1():
    sa = Sparsearray([1,2,0,0,0,0,3,0,0,4])
    assert sa[1] == 2

def test_sa_getitem2():
    sa = Sparsearray([1,2,0,0,0,0,3,0,0,4])
    assert sa[2] == 0

def test_sa_getitem3():
    sa = Sparsearray([1,2,0,0,0,0,3,0,0,4])
    assert sa[9] == 4

def test_sa_delitem0():
    sa = Sparsearray([1,2,0,0,0,0,3,0,0,4])
    del sa[1]
    assert sa.__repr__() == "Sparsearray([1, 0, 0, 0, 0, 0, 3, 0, 0, 4])"
