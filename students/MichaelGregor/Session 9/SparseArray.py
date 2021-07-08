

class SparseArray(object):

    def __init__(self, array):
        if array == None:
            return self._array
        else:
            self._array = array

    def __getitem__(self, key):
        try:
            return self._array[key]
        except IndexError:
            return 0

    def __setitem__(self, key, value):
        try:
            if value is not 0:
                self._array[key] = value
        except IndexError:
            num_diff = (key - len(self._array))
            for index in range(num_diff):
                self._array.append(0)
            self._array.append(value)

    def __delitem__(self, key):
        del self._array[key]

    def __len__(self):
        return len(self._array)

    def append(self, item):
        self._array.append(item)


def main():

    sa = SparseArray([1,2,0,0,0,0,3,0,0,4])
    print(len(sa))
    sa.append(5)
    print("index 10 is {}".format(sa[10]))
    sa[2] = 9
    print("index 2 is {}".format(sa[2]))
    del sa[2]
    print("index 2 is {}".format(sa[2]))
    sa[15] = 20
    print("index 15 is {}".format(sa[15]))
    print("index 12 is {}".format(sa[12]))
    sa[15] = 0
    print("index 15 is {}".format(sa[15]))
    value = sa[25]
    print(value)


if __name__ == "__main__":
    main()


