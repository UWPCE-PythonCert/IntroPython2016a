#from Trapezoidal_Rule_N import quadratic
#from Trapezoidal_Rule_N import trapz
from Trapezoidal_Rule import quadratic
from Trapezoidal_Rule import trapz

def test_1():
    assert (int(trapz(quadratic,0,10,1,3,2)) == int((1/3)*(10**3)+(3/2)*(10**2)+2*10)) is True
