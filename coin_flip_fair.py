# Heads & Tails 1.1 12Feb2016
import random

# Ask user to choose heads or tails
print('Choose Heads or Tails')
user = input()

# Establish outcome of the coin toss
coin = ['Heads', 'Tails']
flip = random.choice(coin)

# Compare choice to outcome then feedback to user

if flip[0] == user[0].upper():
    print("You win")

else:
    print("You lose")

print("the coin landed on",flip)
