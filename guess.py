import random
secret_number = random.randint(1,100)

count = 0
while True:
    guess = int(input('Guess a number between 1 and 100: '))
    count = count + 1 # count += 1

    if guess < secret_number:
        print('Higher..')
    elif guess > secret_number:
        print('Lower..')
    else:
        print(f'Correct! Guessed in {count} times')
        break