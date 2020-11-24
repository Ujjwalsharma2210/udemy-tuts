low = 1
high = 100000

print("Chose a number between {} and {}".format(low, high))
input("Press ENTER to start.")

guesses = 1
while low != high:
    print("\t Guessing in the range of {} and {}".format(low, high))
    guess = low + (high - low) // 2
    high_low = input("My guess is {}. Should I guess higher or lower?"
                     "Enter h or l, or c i fmy guess was correct"
                     .format(guess)).casefold()

    if high_low == "h":
        # Guess higher. The low end of range becomes 1 greater than the guess.
        low = guess + 1
    elif high_low == "l":
        # Guess lower. The high end of the range becomes one less than the guess.
        high = guess - 1
    elif high_low == "c":
        print("I got it in {} guesses!".format(guesses))
        break

    else:
        print("Please enter h, l or c.")

    guesses = guesses + 1
else:
    print("You thought of the number {}".format(low))
    print("I got it in {} guesses".format(guesses))