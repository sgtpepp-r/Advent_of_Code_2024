import re

def main(args):
    
    pattern = "mul\([0-9]{1,3},[0-9]{1,3}\)"
    disable = "don't\(\)(.*?)(do\(\)|\n)"

    full_string = "".join(args)
    full_string = full_string.replace("\n", "")
    
    valid_string = re.sub(disable, "", full_string)
    answer = part_one(valid_string, pattern)

    return answer

def part_one(args, pattern):
    """
    get sum of products
    """
    sum = 0
    
    # find all mul() instructions and sum product
    match_list = re.findall(pattern, args)
    for match in match_list:
        product = match.replace("mul(", "").replace(")", "").split(",")
        sum += (int(product[0]) * int(product[1]))

    return sum

if __name__ == '__main__':

    input_file = "day3/input.txt"
    with open(input_file, "r") as f:
        lines = f.readlines()
        answer = main(lines)

    print(f"Answer: {answer}")
    print("Done.")