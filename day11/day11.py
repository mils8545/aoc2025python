import sys, time

def parse_input(filename : str):
    with open(filename, 'r') as f:
        # Adjust parsing based on the specific problem's input format
        lines : list[str] = [line.strip() for line in f]
    return lines

def solve_part1(lines : list[str]):
    devices : dict[str, list[str]] = {}
    for line in lines:
        entries = line.split(" ")
        devices[entries[0][:-1]] = entries[1:]
    total = 0
    
    queue = ['you']
    while len(queue) > 0:
        current = queue.pop(0)
        if current == 'out':
            total += 1
            continue
        for edge in devices[current]:
            queue.append(edge)
    return f"The number of paths from you to out is {total}"

devices : dict[str, list[str]] = {}
memo : dict[str, int] = {}

def paths(start: str, target: str, required: list[str] = []) -> int:
    if start == target:
        if len(required) == 0:
            return 1
        else:
            return 0
    key = start + "," + target + "," + ",".join(required)
    if key in memo:
        return memo[key]
    if start in required:
        required = required.copy()
        required.remove(start)
    total = 0
    for edge in devices[start]:
        total += paths(edge, target, required)
    memo[key] = total
    return total

def solve_part2(lines : list[str]):
    for line in lines:
        entries = line.split(" ")
        devices[entries[0][:-1]] = entries[1:]
    result = paths("svr", "out", ["dac", "fft"])
    return f"The number of paths from svr to out through fft and dac is {result}"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_filename = "day11/"+sys.argv[1]
    else:
        input_filename = "day11/input.txt" # Default input file name

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