
def getnonchars(txtstring):
    '''
    Get a list of nonalphachars in string
    '''
    nonchar = []
    for word in txtstring.split(' '):
        for let in word:
            if (ord(let) < ord('A') or ord(let) > ord('z')) and (let not in nonchar):
                nonchar.append(let)
    return(nonchar)


def removenonchar(nonchar, txtstring):
    '''
    Removes non alphas from words
    '''
    for char in nonchar:
        if char in txtstring:
            txtstring = txtstring.replace(char, ' ')
    return txtstring


def splittxtstring(txtstring):
    '''
    Splits text string into list of individual words in string
    '''
    txtsplit = []
    for word in (txtstring.split(' ')):
        if len(word) > 0:
            txtsplit.append(word)

    return txtsplit


def groupwords(txtsplit):
    '''
    Create dictionary with 2 word pairs as key and 3rd word as value
    '''
    groupwords = {}
    for (i, word) in enumerate(txtsplit):
        if i > (len(txtsplit) - 3):
            pass
        else:
            wordpair = '{} {}'.format(txtsplit[i], txtsplit[i + 1])
            wordafter = txtsplit[i + 2]
            if wordpair in groupwords:
                groupwords[wordpair].append(wordafter)
            else:
                groupwords['{}'.format(wordpair)] = [wordafter]
    return groupwords

if __name__ == '__main__':
    # import txt file for kata trigram
    smalltxt = open('sherlock_small.txt.', 'r')
    # reat in txt and remove and line returns
    txtstring = smalltxt.read().replace('\n', ' ')
    # identify nonalpha chars in txt string
    nonchars = getnonchars(txtstring)
    # remove nonalpha chars from string
    ftxtstring = removenonchar(nonchars, txtstring)
    # append each word in string to list
    txtsplit = splittxtstring(ftxtstring)
    print(groupwords(txtsplit))
