# This is a basic one file python script with main function

def main():
    # Initialize sumofall variable
    sumofall = 0
    # Read the contents of the file
    contents = open("adventureday1_1.txt", "r").read()
    # Split the contents into lines
    lines = contents.split("\n")
    # Iterate over each line
    for line in lines:
        # Get the first and last number from the line
        first_number, last_number = getFirstAndLastNumber(line)
        # Add the sum of the first and last number to sumofall
        sumofall += int(str(first_number) + str(last_number))
    # Print the final sum
    print(sumofall)

def getFirstAndLastNumber(letter: str):
    numbers = [int(x) for x in letter if x.isdigit()]
    return numbers[0], numbers[-1]

if __name__ == "__main__":
    main()
