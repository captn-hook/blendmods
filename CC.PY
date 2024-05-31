def isValid(cardNumber):
    length = len(cardNumber)
    sum = 0
    parity = length % 2
    for i in range(length):
        digit = int(cardNumber[i])
        if i % 2 != parity:
            sum += digit
        elif digit > 4:
            sum += 2 * digit - 9
        else:
            sum += 2 * digit
    return int(cardNumber[-1]) == (10 - (sum % 10))

cc = ' 4485 0803 6191 2635 '

print(isValid(cc.replace(' ', ''))) # True