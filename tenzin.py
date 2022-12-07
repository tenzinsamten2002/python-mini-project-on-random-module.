"""Project 5:

The task is to create a script that generates a random number between a fixed range, and if the 

user guesses the number right in three chances, then user wins otherwise user lose.

This game user can play as many numbers of times and whenever user wins a score is to be 

given to the user.

At the end the users score must be displayed on the screen.

Hint: Make use of random module to design the game

Abstract steps:

1.The user enters the lower and upper bounds of the range.

2. As a result, the compiler generates a random integer between the range and stores it in 

a variable for future use.
A while loop will be created for repetitive guessing.

3. When a user guesses a number that is greater than a randomly selected number, the 

user receives the message “have one more try”. Your guess was too high.

4. If the user guesses a number smaller than a randomly selected number, the user gets an 

output of “have one more try “. Your guess was too small”

5. In addition, if the user guesses within a minimum number of attempts, they get a 

“Congrat’s” message and also get the winning scores.

6. If the user fails to guess the integer in the minimum number of guesses, he/she will 

receive a “Better Luck Next Time!

(Student is free to decide the input and output layout for this mini project)"""






import random
print("\n\n\n\t\t\tTHE GUESSING GAME\n\n\n")
score = 0
while True:
    low = int(input("\nLower Bound: "))
    hi = int(input("Upper Bound: "))

    if low > hi:
        print("\nLower Bound Must Be Less Than Upper Bound.\n")    
        print("Please Try Aagin.\n")
        continue

    if abs(hi-low)<2:
        print("\nThe Range Is Too Small. Please Give A Larger Range.\n")
        continue

    ran_num = random.randrange(low, hi)
    print("\nAwesome! I've thought of a number between", low, "and", hi)
    print("Now you have 3 chances to guess it.\n\n")
    for i in range(3):
        guess = int(input("Your Guess: "))
        if guess == ran_num:
            print("\nYou guessed it! You win!\n+1 Added To Your Total Score\n")
            score += 1
            break
        elif guess < ran_num:
            print("Your Guess Was Too Low!")
        else:
            print("Your Guess Too High!")
        if i == 2:
            print("\nYou Lose! The Number Was", ran_num)
        else:
            print("Try Once More.")
    print("\nUp For Another Round? Or Exit? (Type Yes Or No)")
    response = input()
    if response.lower() == "yes":
        continue
    else:
        print("\n\nThanks For Playing! Your Total Score Is:", score)
        break
print("Press Any Key To Exit.")
input()
