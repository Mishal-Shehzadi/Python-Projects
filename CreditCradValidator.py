sumOddDigits = 0
sumEvenDigits = 0
total = 0
 
cardNumber = input ("Enter a credit card #: ")
cardNumber = cardNumber.replace("-", "")
cardNumber = cardNumber.replace(" ", "")
cardNumber = cardNumber[::-1]

for x in cardNumber[::2]:
    sum_odd_digits += int(x)

for x in cardNumber [1::2]:
    x = int(x) * 2
    if(x>=10):
        sum_even_digits += (1 + (x % 10))
    else:
        sum_even_digits += x

total = sum_odd_digits + sum_even_digits
if (total % 10 == 0):
    print ("Valid!")
else:
    print ("Invalid")