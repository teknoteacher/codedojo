# coin_flip_unfair 12Feb2016
import random

# Ask user to choose heads or tails
print('Player is Heads, Computer is Tails')
pause = input("press a key to flip the coin")


# Establish outcome of the coin toss
coin = ['Heads', 'Tails', 'Tails', 'Tails']
flip = random.choice(coin)

# Compare choice to outcome then feedback to user

if flip == 'Heads':
    print("You win")

else:
    print("You lose")

print("the coin landed on",flip)
