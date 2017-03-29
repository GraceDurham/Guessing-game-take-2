from random import randint


name = raw_input("Howdy, what's your name?")
print "%s, I am thinking of a number between 1 and 100. Try to guess my number." % name
my_number = randint(1,100)
number_guesses = 0

while True:
    your_guess = int(raw_input("Your guess?"))
    number_guesses = number_guesses + 1
    
    if your_guess < 1 or your_guess > 100:
        print " Hey now that is not a number between 1 or 100. Please follow the instructions and pick a number between 1 and 100."

    else:   
        if your_guess < my_number:
            print "Your guess is too low. try again."
        
        elif your_guess > my_number:
            print "Your guess is too high. try again."
        
        else:
            print "Well done, %s! You found my number in %s tries." % (name,number_guesses)
            break