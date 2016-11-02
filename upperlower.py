s=['adam','LiSA','baT']
def suit(x):
    return x[0].upper() + x[1:].lower()
print(map(suit,s))
