# Exceptions Lab
# Student: Chi Kin Ho
# Date: Sunday, February 7, 2016


def safe_input():
    try:
        data = input("Enter a value: ")
    except (KeyboardInterrupt, EOFError) :
        return None
    else:
        return data


data = safe_input()
print(data)

