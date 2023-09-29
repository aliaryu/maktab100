import argparse
import random
import os
os.system("cls" if os.name == "nt" else "clear")

parser = argparse.ArgumentParser()

parser.add_argument("-s", "--start", type=int, required=True, help="start number")
parser.add_argument("-e", "--end",   type=int, required=True, help="end number")
parser.add_argument("-g", "--guess", type=int, required=True, help="number of guess")

args = parser.parse_args()

if args.guess <= 0:
    print("At least one 'guess' must be allowed to play,")
    print(f"You have entered '{args.guess}' for -g/--guess,    :D")
elif args.start >= args.end:
    print("The 'start' number cannot be greater than or equal the 'end' number,")
    print(f"You have entered '{args.start}' for -s/--start & '{args.end}' for -e/--end'")
else:
    guesses = 0
    random_number = random.randint(args.start, args.end)
    print(f"Game ON, You have {args.guess} chances to find\nthe number between {args.start} and {args.end}! Go ;p")

    while guesses < args.guess:
        guesses += 1
        try:
            guess = int(input(">>> "))
            if guess == random_number:
                print("You Win! GG.")
                break
            else:
                if guesses >= args.guess:
                    print(f"You Lose ~ Correct number was: {random_number}")
                    break
                else:
                    if guess > random_number:
                        print("Enter lower number")
                    else:
                        print("Enter higher number")
        except:
            print("Enter integer number")
