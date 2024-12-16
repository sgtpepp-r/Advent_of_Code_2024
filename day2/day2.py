def main(args):
    
    count = 0

    for line in args:
        numbers = line.split()
        i = len(numbers) - 1
        j = len(numbers) - 2

        valid = is_valid(numbers, i, j)

        if not valid:
            for number in range(len(numbers)):
                new = numbers[:number]+numbers[number+1:]
                i = len(new) - 1
                j = len(new) - 2
                if is_valid(new, i, j):
                    count += 1
                    break
                
        if valid:
            count += 1

    return count

def is_valid(numbers, i, j):
    while j >= 0:
        inc_or_dec = (int(numbers[len(numbers) - 1]) - int(numbers[len(numbers) - 2]))
        difference = int(numbers[i]) - int(numbers[j])
        valid = True
            # check increasing or decreasing
        if inc_or_dec < 0:
            flag = True
        else:
            flag = False

            # check difference is negative and between 1 and 3
        if flag and ((difference not in range(-3, 0)) or difference == 0):
            valid = False
            break
            # check difference is positive and between 1 and 3
        elif not flag and((difference not in range(1, 4)) or (difference == 0)):
            valid = False
            break
        else:
            i -= 1
            j -= 1
            continue
    return valid

if __name__ == "__main__":

    input_file = "day2/input.txt"

    with open(input_file, "r") as f:
        lines = f.readlines()
        answer = main(lines)

    print(f"Answer: {answer}")
    print("Done.")