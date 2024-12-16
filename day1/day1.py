# Advent of Code 2024 - Day 1

def part_one(left_list, right_list):
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

    return answer

def part_two(left_list, right_list):
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
    answer_one =  part_one(left_list, right_list)

    # part 2
    answer_two = part_two(left_list, right_list)

    return answer_one, answer_two


if __name__ == "__main__":

    input_file = "day1/input.txt"

    with open(input_file, "r") as f:
        lines = f.readlines()
        answer = main(lines)

    print(f"Answer 1: {answer[0]}")
    print(f"Answer 2: {answer[1]}")
    print("Done.")
