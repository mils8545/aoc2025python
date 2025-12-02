import sys, time

def parse_input(filename : str):
    with open(filename, 'r') as f:
        # Adjust parsing based on the specific problem's input format
        lines : list[str] = [line.strip() for line in f]
    return lines

def solve_part1(lines : list[str]):
    current : int = 50
    count : int = 0
    dirs : dict[str, int] = {'L': -1, 'R': 1}

    for line in lines:
        current += dirs[line[0:1]] * int(line[1:])
        current %= 100
        if current == 0:
            count += 1

    return f"The dial lands at 0 - {count} times"

def solve_part2(lines : list[str]):
    current : int = 50
    count : int = 0
    dirs : dict[str, int] = {'L': -1, 'R': 1}

    for line in lines:
        dir = dirs[line[0:1]]
        distance = int(line[1:])
        while distance >= 100:
            count += 1
            distance -= 100
        new : int = current + dir * distance
        if current != 0 and (new <= 0 or new >= 100):
            count += 1
        current = new % 100    

    return f"The dial passes through 0 - {count} times"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_filename = "day01/"+sys.argv[1]
    else:
        input_filename = "day01/input.txt" # Default input file name

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