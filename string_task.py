# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.
#
# Example input: 'read'
# Example output: 'reading'


def verbing(s):
    if len(s) > 3:
        if s[-3:] == "ing":
            s = s[:-3] + "ly"
        else:
            s += "ing"
    return s


# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
#
# Example input: 'This dinner is not that bad!'
# Example output: 'This dinner is good!'
def not_bad(s):
    fr_not, fr_bad = -1, -1
    for i in range(len(s) - 3):
        if fr_not == -1 and s[i:i+3] == "not":
            fr_not = i

        if fr_bad == -1 and s[i:i+3] == "bad":
            fr_bad = i

    if(fr_not != -1 and fr_bad != -1 and fr_not < fr_bad):
        s = s[:fr_not] + "good" + s[fr_bad + 3:]
    return s


# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
#
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
#
# Example input: 'abcd', 'xy'
# Example output: 'abxcdy'
def front_back(a, b):
    n, m = len(a), len(b)
    return a[:-(n // 2)] + b[:-(m // 2)] + a[-(n // 2):] + b[-(m // 2):]

a, b = 'abcde', 'xyz'
print(front_back(a, b))
