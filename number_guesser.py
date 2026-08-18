import random

while True:
    print("\n" + "="*40)
    print("      WELCOME TO NUMBER GUESSER")
    print("="*40)

    n = random.randint(1, 100)
    attempts = 0
    low = 1
    high = 100

    while True:
        user = input(f"Guess a number ({low}-{high}) or press 'q' to quit: ")

        if user.lower() == "q":
            print("Thanks for playing!")
            exit()

        try:
            g = int(user)
        except ValueError:
            print("⚠️  Invalid! Please enter a number.")
            continue

        if g < 1 or g > 100:
            print("⚠️  Please enter a number between 1 and 100.")
            continue

        attempts += 1

        if g == n:
            print("\n" + "="*30)
            print("YOU WON!")
            print("="*30)
            print(f"Correct Number : {n}")
            print(f"Attempts       : {attempts}")

            if attempts <= 5:
                print("Performance    : Excellent!")
            elif attempts <= 10:
                print("Performance    : Good!")
            else:
                print("Performance    : Keep Practicing!")

            break

        elif g > n:
            print("Too High!")
            high = min(high, g - 1)

        else:
            print("Too Low!")
            low = max(low, g + 1)

    play = input("\nPlay Again? (y/n): ")

    if play.lower() != "y":
        print("Goodbye! ")
        break