#from Trapezoidal_Rule_N import quadratic
#from Trapezoidal_Rule_N import trapz
from Trapezoidal_Rule import quadratic
from Trapezoidal_Rule import trapz

import math

def test_1():
    assert math.isclose(int(trapz(quadratic,0,10,1000000,1,3,2)), int((1/3)*(10**3)+(3/2)*(10**2)+2*10),rel_tol=1e-9, abs_tol=0.0) is True
