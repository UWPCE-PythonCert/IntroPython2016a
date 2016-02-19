def trapz(fun, a, b, N, **kwargs):

    h = ((b-a)/N)
    area = 0

    while a < b:
        area += (h/2) * (fun(a, **kwargs) + fun(a+h, **kwargs))
        a = a + h

    return area

