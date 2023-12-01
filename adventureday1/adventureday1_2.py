
def main():
    sumofall = 0
    contents = open("adventureday1_1.txt", "r").read()
    lines = contents.split("\n")
    for line in lines:
        first_number, last_number = find_start_index(line)
        sumofall += int(str(first_number) + str(last_number))
    print(sumofall)

def find_start_index(string):
    number_mapping = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }

    orders = []
    for key in number_mapping:
        if key in string.lower():
            my_array_regular = [str(string.lower().index(key)), str(number_mapping.get(key))]
            my_array_reverse = [str(string.lower().rindex(key)), str(number_mapping.get(key))]
            if(my_array_regular != my_array_reverse):
                orders.append(my_array_regular)
                orders.append(my_array_reverse)
            else:
                orders.append(my_array_regular)

    for num in range(10):
        if str(num) in string.lower():
            my_array_reg = [str(string.lower().index(str(num))), str(num)]
            my_array_rev = [str(string.lower().rindex(str(num))), str(num)]
            if(my_array_reg != my_array_rev):
                orders.append(my_array_reg)
                orders.append(my_array_rev)
            else:
                orders.append(my_array_reg)
    sorted_array = sorted(orders, key=lambda x: int(x[0]))

    return sorted_array[0][1], sorted_array[-1][1]

if __name__ == "__main__":
    main()
