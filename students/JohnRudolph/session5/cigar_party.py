def cigar_party(cigars, isweekend):
    if (40 <= cigars <= 60) and (isweekend is False):
        return True
    elif (40 <= cigars) and (isweekend is True):
        return True
    else:
        return False