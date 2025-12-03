import sys, time

def parse_input(filename : str):
    with open(filename, 'r') as f:
        # Adjust parsing based on the specific problem's input format
        lines : list[str] = [line.strip() for line in f]
    return lines

def cell_joltage(cellstr: str, count: int):
    joltage : int = 0
    lindex : int = 0
    for i in range(count):
        cellmax : int = 0
        for j in range(lindex, len(cellstr) - (count-i) - 1):
            cellval = int(cellstr[j])
            if cellval > cellmax:
                cellmax = cellval
                lindex = j
        joltage = joltage * 10 + cellmax
        lindex = lindex + 1
    return joltage

def solve_part1(lines : list[str]):
    sum : int = 0
    for line in lines:
        sum += cell_joltage(line, 2)

    return f"The maximum jolatage from 2 cells in each bank is: {sum}"

def solve_part2(lines : list[str]):
    sum : int = 0
    for line in lines:
        sum += cell_joltage(line, 12)
    
    return f"The maximum joltage activating 12 cells is {sum}"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_filename = "day03/"+sys.argv[1]
    else:
        input_filename = "day03/input.txt" # Default input file name

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