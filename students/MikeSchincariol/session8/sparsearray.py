

class Sparsearray(object):


    def __init__(self, iterable):
        self.max_idx = None        # None means the array is empty
        self.array = {}            # The dict that holds the array data

        # Iterate over the supplied list of values and put the non-zero
        # items in the dict
        for idx,val in enumerate(iterable):
            if val > 0:
                self.array[idx] = val

        # Adjust the max index that the array knows about
        # to account for the initial values
        self.max_idx = len(iterable)-1


    def __len__(self):
        """ Returns the length of the sparse array
        """
        return self.max_idx+1


    def __contains__(self, x):
        """  Returns True if the value 'x' is in the sparse array
        """
        if self.max_idx is None:
            return False
        elif x == 0 and len(self) != len(self.array):
            # Looking for a 0. Since this is a sparse array, we
            # can't look in the array itself to see if the value '0'
            # is present because it is not stored. The only way we
            # can detect that a '0' is in the array is by a mismatch
            # on the length of the array versus the last index of
            # the array.
            return True
        else:
            return x in self.array


    def __setitem__(self, k, v):
        """ Sets item 'k' equal to value 'v'
        """
        # If the value is 0, we never store it and if item 'k' already
        # existed as a non-zero value, we have to remove it. Finally,
        # if the value is non-zero, store it in the array.
        if v == 0 and k in self.array:
            del self.array[k]
        elif v > 0:
            self.array[k] = v

        # Update the last index of the array
        if k > self.max_idx:
            self.max_idx = k


    def __getitem__(self, k):
        """ Returns the value of item 'k', if 'k' is in the array
        """
        # If the item 'k' is outside the bounds of the array, then
        # it was never added to the array. If 'k' is inside the
        # bounds of the array, the array will have it if the value
        # associated with the item 'k' is non-zero.
        if k > self.max_idx:
            return None
        elif k in self.array:
            return self.array[k]
        else:
            return 0

    def __delitem__(self, k):
        """ Removes item 'k' from the array
        """
        if k in self.array:
            del self.array[k]



    def __iter__(self):
        """ Iterates over the list of items returning one at a time.
        """
        for idx in range(len(self)):
            if idx in self.array:
                yield self.array[idx]
            else:
                yield 0

    def __str__(self):
        # Used the same string as returned by __repr__
        self.__repr__(self)

    def __repr__(self):
        l = [x for x in self]
        return "Sparsearray({})".format(l)





