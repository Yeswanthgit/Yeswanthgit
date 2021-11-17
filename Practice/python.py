allGuests = {'Alice': {'apples': 9, 'bananas': 12},
             'Bob': {'ham sand witches': 5, 'apples': 19},
             'Yeswanth': {'cups': 4, 'pies': 7}}


def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought


print('Number of things being brought:')
print('Apples'+str(totalBrought(allGuests, 'apples')))
print('Bananas'+str(totalBrought(allGuests, 'bananas')))
print('Ham sand witches'+str(totalBrought(allGuests, 'ham sand witches')))
print('Pies'+str(totalBrought(allGuests, 'pies')))
print('Cups'+str(totalBrought(allGuests, 'cups')))
