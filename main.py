import random
n = random.randrange(1,50)
guess = int(input("Write any number: "))
while n!= guess:
    if guess < n:
        print("Too low")
        guess = int(input("Write number again: "))
    elif guess > n:
        print("Too high!")
        guess = int(input("Write number again: "))
    else:
      break
print("the answer is correct!!")
