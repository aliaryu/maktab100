import argparse

parser = argparse.ArgumentParser()

parser.add_argument("numbers", nargs="+", type=float, help="list of grades for average")
parser.add_argument("-f", "--float", type=int, help="specify the number of decimal places")

args = parser.parse_args()
default_round = 2

if args.float:
    default_round = args.float
    avg = round(sum(args.numbers) / len(args.numbers), default_round)
    print("Average Grades: ", avg)
else:
    avg = round(sum(args.numbers) / len(args.numbers), default_round)
    print("Average Grades: ", avg)
