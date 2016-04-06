# Heads & Tails Never Win 12Feb2016
import random

# Ask user to choose heads or tails
print('Choose Heads or Tails')
user = input()

# Establish outcome of the coin toss
coin = ['Heads', 'Tails']
flip = random.choice(coin)

# Compare choice to outcome then feedback to user

if user[0].upper() == "T":
    print("You lose")
    print("the coin landed on Heads")

if user[0].upper() == "H":
    print("You lose")
    print("the coin landed on Tails")

