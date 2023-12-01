# This is a basic one file python script with main function

def main():
    sumofall = 0
    contents = open("adventureday1_1.txt", "r").read()
    lines = contents.split("\n")
    for line in lines:
        first_number, last_number = getFirstAndLastNumber(line)
        sumofall += int(str(first_number) + str(last_number))
    print(sumofall)

def getFirstAndLastNumber(letter: str):
    numbers = [int(x) for x in letter if x.isdigit()]
    return numbers[0], numbers[-1]

if __name__ == "__main__":
    main()
