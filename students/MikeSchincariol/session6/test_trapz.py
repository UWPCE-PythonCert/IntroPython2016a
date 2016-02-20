from trapz import trapz

# Curves to use during testing
def line(x):
    return 5

def sloped_line(x, M, B):
    return M*x+B

def quadratic(x, A, B, C):
    return A*x**2 + B * x + C


# Function for testing if 2 values are "close enough" to be considered
# the same
def isclose(a, b, tol=1e-9):
    if (a-b) < tol:
        return True
    else:
        return False

# Tests that exercise the trapz() method with various curves
def test_trapz_line():
    assert trapz(line, 0, 10, 100) == 50

def test_Sloped_line():
    a = 0
    b = 10
    slope = 5
    offset = 10
    ans = slope*(b**2 - a**2)/2 + offset*(b - a)
    assert isclose(trapz(sloped_line, a, b, 100, M=slope, B=offset), ans)

def test_trapz_quadratic(**kwargs):
    a = 0
    b = 10
    A = 1
    B = 2
    C = 3
    ans = A/3*(b**3 - a**3) + B/2*(b**2 - a**2) + C*(b - a)
    assert isclose(trapz(quadratic, a, b, 1000, A=A, B=B, C=C), ans, 0.001)
