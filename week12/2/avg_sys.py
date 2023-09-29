import sys

args = sys.argv[1:]

try:
    avg = round(sum(float(num) for num in args) / len(args), 2)
    print("Average Grades: ", avg)
except Exception as error:
    print(error)
