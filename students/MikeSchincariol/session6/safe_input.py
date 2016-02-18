def safe_input(prompt):
    try:
        res = input(prompt)
    except EOFError or KeyboardInterrupt as ex:
        res = None
    finally:
        return res

