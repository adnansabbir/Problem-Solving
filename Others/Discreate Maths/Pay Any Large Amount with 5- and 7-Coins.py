# Suppose you have unlimited number of 5 and 7. Make a list number with these coins that at add up to a total n
def change(amount):
    assert (amount >= 24)

    if amount == 24:
        return [5, 5, 7, 7]
    if amount == 25:
        return [5, 5, 5, 5, 5]
    if amount == 26:
        return [7, 7, 7, 5]
    if amount == 27:
        return [7, 5, 5, 5, 5]
    if amount == 28:
        return [7, 7, 7, 7]

    coins = change(amount - 5)
    coins.append(5)
    return coins


print(sum(change(5)))
