import sys, time

def parse_input(filename : str):
    with open(filename, 'r') as f:
        # Adjust parsing based on the specific problem's input format
        lines : list[str] = [line[:-1] for line in f]
    return lines

def solve_part1(lines : list[str]):
    separators : list[int] = []
    result = 0
    for i in range(len(lines[0])):
        separators.append(True)
    for line in lines:
        for i in range(len(line)):
            if line[i] != " ":
                separators[i] = False

    nums : list[list[str]]= []
    for line in lines[:-1]:
        last = 0
        current : list[str]= []
        for i in range(len(separators)):
            if separators[i]:
                current.append(line[last:i])
                last = i + 1
        current.append(line[last:])
        nums.append(current)

    operators : list[str] = []
    operators.append(lines[-1][0])
    for i in range(len(separators)):
        if separators[i]:
            operators.append(lines[-1][i+1])

    for col in range(len(operators)):
        if operators[col] == '*':
            prod : int = 1
            for row in nums:
                prod = prod * int(row[col])
            result = result + prod
        else:
            sum = 0
            for row in nums:
                sum = sum + int(row[col])
            result = result + sum
                
    return f"{result}"

def solve_part2(lines : list[str]):
    separators : list[int] = []
    result = 0
    for i in range(len(lines[0])):
        separators.append(True)
    for line in lines:
        for i in range(len(line)):
            if line[i] != " ":
                separators[i] = False

    nums : list[list[str]]= []
    for line in lines[:-1]:
        last = 0
        current : list[str]= []
        for i in range(len(separators)):
            if separators[i]:
                current.append(line[last:i])
                last = i + 1
        current.append(line[last:])
        nums.append(current)

    operators : list[str] = []
    operators.append(lines[-1][0])
    for i in range(len(separators)):
        if separators[i]:
            operators.append(lines[-1][i+1])

    for col in range(len(operators)):
        if operators[col] == '*':
            prod : int = 1
            for i in range(len(nums[0][col])):
                t = ""
                for row in range(len(nums)):
                    t += nums[row][col][i]
                
                prod = prod * int(t)
            result = result + prod
        else:
            sum : int = 0
            for i in range(len(nums[0][col])):
                t = ""
                for row in range(len(nums)):
                    t += nums[row][col][i]
                
                sum = sum + int(t)
            result = result + sum
                
    return f"{result}"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_filename = "day06/"+sys.argv[1]
    else:
        input_filename = "day06/input.txt" # Default input file name

    puzzle_input : list[str] = parse_input(input_filename)

    start_time : float = time.time()
    part1_answer : str = solve_part1(puzzle_input)
    print(f"Part 1: {part1_answer}")
    end_time : float = time.time()
    print(f"Part 1 took - {round((end_time - start_time) * 1000)} miliseconds")

    start_time = time.time()
    part2_answer : str = solve_part2(puzzle_input)
    print(f"Part 2: {part2_answer}")
    end_time = time.time()
    print(f"Part 2 took - {round((end_time - start_time) * 1000)} miliseconds")