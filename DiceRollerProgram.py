import random

diceArt = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),

    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘")  ,

     3: (
         "┌─────────┐",
         "│  ●      │",
         "│    ●    │",
         "│      ●  │",
         "└─────────┘") ,

    4: (
         "┌─────────┐",
         "│  ●   ●  │",
         "│         │",
         "│  ●   ●  │",
         "└─────────┘"),

    5: (
         "┌─────────┐",
         "│  ●   ●  │",
         "│    ●    │",
         "│  ●   ●  │",
         "└─────────┘") ,

    6: (
         "┌─────────┐",
         "│  ●   ●  │",
         "│  ●   ●  │",
         "│  ●   ●  │",
         "└─────────┘") 

}

dice = []
total = 0
NumOfDice = int (input("How many dice?: "))

for die in range (NumOfDice):
    dice.append(random.randint(1, 6))

# for die in range(NumOfDice):
#     for line in diceArt.get(dice[die]):
#         print (line,)

for line in range(5):
    for die in dice:
        print (diceArt.get(die)[line], end = " ")
    print ()

for die in dice:
    total += die
print (f"Total: {total}")