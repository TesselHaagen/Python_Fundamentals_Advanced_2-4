import random

dice1 = random.randint(1,6)
dice2 = random.randint(1,6)
dice3 = random.randint(1,6)
dice4 = random.randint(1,6)
dice5 = random.randint(1,6)

print("De worp is: ", dice1, dice2, dice3, dice4, dice5)

total = dice1+dice2+dice3+dice4+dice5
print("De som is: ", total)


i = 0
total = 0
while i < 5:
    dice = random.randint(1,6)
    print(dice)
    total += dice
    i += 1

print("Total: ", total)