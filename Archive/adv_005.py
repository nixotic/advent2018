with open('Data/input005.txt', 'r') as file:
    poly = file.readline()


def reducer(dat):
    newdat = ''
    old = '-'  # not a letter
    for char in dat:
        if old is '-':
            old = char
        elif abs(ord(char) - ord(old)) != 32:  # need to remove chars if they are capital/lower pairs
            newdat += old
            old = char
        else:
            old = '-'
    if old is not '-':
        newdat += old

    if newdat != dat:
        newdat = reducer(newdat)

    return newdat


# print(len(reducer(poly)))
chars = ['aA', 'bB', 'cC', 'dD', 'eE', 'fF', 'gG', 'hH',
         'iI', 'jJ', 'kK', 'lL', 'mM', 'nN', 'oO', 'pP',
         'qQ', 'rR', 'sS', 'tT', 'uU', 'vV', 'wW', 'xX',
         'yY', 'zZ']
results = []
import sys
sys.setrecursionlimit(5000)
for pair in chars:
    testPoly = poly.replace(pair[0], '')
    testPoly = testPoly.replace(pair[1], '')
    d = len(reducer(testPoly))
    results.append([pair, d])
    print(pair + ':' + str(d))

print(results)

sys.setrecursionlimit(1000)