

myInput = (2, 123.4567, 10000)
print("file_00{} , floatr2: ,{:.2f}, center15,{:>15.2e}".format(myInput[0], myInput[1], myInput[2]))

for x in range(1):
    myTuple = (float(input("what is age")),str(input("what is your name")),float(input("what was your age last year")))
    print("the first 3 numbers are: {:$< 8.2f}, {:&^12s}, {:*>+12.2f}".format(*myTuple))
# the ^<> mean center right or left justify with a column width of that many numbered spaces
# e = scientific notation, d = decimal to the digits you specify, s = string  and g=


''' see 7.1.3.1. Format Specification Mini-Language:
https://docs.python.org/2.6/library/string.html#formatstrings

The general form of a standard format specifier is:

format_spec ::=  [[fill]align][sign][#][0][width][.precision][type]
fill        ::=  <a character other than '}'>
align       ::=  "<" | ">" | "=" | "^"
sign        ::=  "+" | "-" | " "
width       ::=  integer
precision   ::=  integer
type        ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"

'''