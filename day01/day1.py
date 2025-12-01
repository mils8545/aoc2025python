import sys

def parse_input(filename):
    """Reads and parses the input file."""
    with open(filename, 'r') as f:
        # Adjust parsing based on the specific problem's input format
        lines = [line.strip() for line in f]
    return lines

def solve_part1(lines):
    """Solves Part 1 of the puzzle."""
    current = 50
    count = 0
    dirs = {'L': -1, 'R': 1}

    for line in lines:
        current += dirs[line[0:1]] * int(line[1:])
        current %= 100
        if current == 0:
            count += 1

    # Implement your solution for Part 1 here
    return f"The dial lands at 0 - {count} times"

def solve_part2(lines):
    """Solves Part 2 of the puzzle."""
    current = 50
    count = 0
    dirs = {'L': -1, 'R': 1}

    for line in lines:
        dir = dirs[line[0:1]]
        distance = int(line[1:])
        while distance >= 100:
            count += 1
            distance -= 100
        new = current + dir * distance
        if current != 0 and (new <= 0 or new >= 100):
            count += 1
        current = new %100    

    return f"The dial passes through 0 - {count} times"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_filename = "day01/"+sys.argv[1]
    else:
        input_filename = "day01/input.txt" # Default input file name

    puzzle_input = parse_input(input_filename)

    part1_answer = solve_part1(puzzle_input)
    print(f"Part 1: {part1_answer}")

    part2_answer = solve_part2(puzzle_input)
    print(f"Part 2: {part2_answer}")