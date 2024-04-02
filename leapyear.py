# Krijg de input en converteer naar integer
jaar = input("Welk jaar?")
jaar = int(jaar)

# Check of het jaar een schrikkeljaar is
if jaar % 4 == 0 and jaar % 100 != 0 or jaar % 400 == 0:
    print(jaar, " is een schrikkeljaar!")
    print(str(jaar) + " is een schrikkeljaar!")
else:
    print("Het is geen schrikkeljaar.")