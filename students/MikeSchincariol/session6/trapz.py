def trapz(fun, a, b, num_steps, **kwargs):
    """
    Compute the area under the curve defined by
    y = fun(x), for x between a and b

    :param fun: the function to evaluate
    :type fun: a function that takes a single parameter

    :param a: the start point for the integration
    :type a: a numeric value

    :param b: the end point for the integration
    :type b: a numeric value

    :param num_steps: The number of integratiion steps to undertake.
    :type num_steps: a numeric integer value

    :param kwargs: Arguments passed to 'fun' when calling 'fun'
    :type kwargs: Keyword arguments
    """
    STEP_SIZE = (b-a)/num_steps

    sum = 0
    for i in range(0, num_steps):
        left = a + (i * STEP_SIZE)
        right = a + ((i+1) * STEP_SIZE)
        sum += fun(left, **kwargs) + fun(right, **kwargs)

    sum = sum * STEP_SIZE / 2
    return sum


