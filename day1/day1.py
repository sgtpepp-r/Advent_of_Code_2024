# Advent of Code 2024 - Day 1

def main(args):

    # input is two columns, separate into list
    #input_list = [line.split(" ") for line in args]
    left_list = []
    right_list = []
    for line in args:
        new_line = (line.strip()).split()
        left_list.append(int(new_line[0]))
        right_list.append(int(new_line[1]))

    # part 1
    """
    # sort lists
    left_list =  sorted(left_list)
    right_list = sorted(right_list)

    # find difference between sorted values
    j = 0
    answer = 0
    for number in left_list:
        difference = (number - right_list[j])
        answer += abs(difference)
        j += 1 
    """

    # part 2
    i = len(left_list)
    sum = 0
    while i:
        count = 0
        for number in right_list:
            if number == left_list[i - 1]:
                count += 1
        sum += (count * left_list[i - 1])
        i -= 1
    
    return sum


if __name__ == "__main__":

    input_file = "input.txt"

    with open(input_file, "r") as f:
        lines = f.readlines()
        answer = main(lines)

    print(f"Answer: {answer}")
    print("Done.")
