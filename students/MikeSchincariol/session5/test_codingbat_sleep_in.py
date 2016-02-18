from codingbat_sleep_in import sleep_in


def test_sleep_in_1():
    assert sleep_in(False, False) == True

def test_sleep_in_2():
    assert sleep_in(False, True) == True

def test_sleep_in_3():
    assert sleep_in(True, False) == False

def test_sleep_in_4():
    assert sleep_in(True, True) == True
