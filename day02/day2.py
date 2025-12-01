import sys

def parse_input(filename : str):
    with open(filename, 'r') as f:
        # Adjust parsing based on the specific problem's input format
        lines : list[str] = [line.strip() for line in f]
    return lines

def solve_part1(lines : list[str]):

    return f"Solve Part 1"

def solve_part2(lines : list[str]):

    return f"Solve Part 2"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_filename = "day02/"+sys.argv[1]
    else:
        input_filename = "day02/input.txt" # Default input file name

    puzzle_input : list[str] = parse_input(input_filename)

    part1_answer : str = solve_part1(puzzle_input)
    print(f"Part 1: {part1_answer}")

    part2_answer : str = solve_part2(puzzle_input)
    print(f"Part 2: {part2_answer}")