__author__ = 'ThomasGaffney'
if __name__ == "__main__":

    translator = str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
                               'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm')

    print(str.translate('Zntargvp sebz bhgfvqr arne pbeare', translator))

    assert str.translate('Zntargvp sebz bhgfvqr arne pbeare', translator) = 'Magnetic from outside near corner'

else: raise Exception("This file was not created to be imported")