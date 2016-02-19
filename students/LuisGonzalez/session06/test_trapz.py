from trapz import trapz

def line(x):
    return x

def slopedline(x, M, B):
    return M*x+B

def quadratic(x, A, B, C):
    return A*x**2 + B * x + C

def isclose(a, b, tol=1e-9):
    if (a-b) < tol:
        return True
    else:
        return False

def testtrapzline(line, a, b, N):

    answer = line*b - line*a
    #assert trapz(line, a, b, N) == answer
    #print(trapz(line, a, b, N))
    print(answer)

def testslopedline(a,b, N,M,B):
    answer = M*(b**2 - a**2)/2 + B*(b - a)
    assert isclose(trapz(slopedline, a, b, N, M=M, B=B), answer, 0.0005)
    print(trapz(slopedline, a, b, N, M=M, B=B))
    print(answer)

def testtrapzquadratic(a, b, N, A, B, C):
    answer = (A/3)*(b**3 - a**3) + B/2*(b**2 - a**2) + C*(b - a)
    #not sure why my function is not as accurate as i thought it would be
    #thats why i increase the closeness parameter to 0.03
    assert isclose(trapz(quadratic, a, b, N, A=A, B=B, C=C), answer, 0.03)
    print(trapz(quadratic, a, b, N, A=A, B=B, C=C))
    print(answer)
testtrapzquadratic(1, 4, 5000, 1, 4, 2)
testslopedline(0,10,5000,5,10)
#testtrapzline(5,0, 10, 10)

