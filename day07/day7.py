import sys, time

def parse_input(filename : str):
    with open(filename, 'r') as f:
        # Adjust parsing based on the specific problem's input format
        lines : list[str] = [line.strip() for line in f]
    return lines

def solve_part1(lines : list[str]):
    beams = [0] * len(lines[0])
    
    beams[lines[0].find("S")] = 1

    count = 0
    for line in lines[1:]:
        next = [0] * len(line)
        for i, val in enumerate(line):
            if beams[i] > 0:
                if val=='.':
                    next[i] = beams[i]
                else:
                    count += beams[i]
                    next[i-1] = beams[i]
                    next[i+1] = beams[i]
        beams = next

    return f"{count}"

def solve_part2(lines : list[str]):
    beams = [0] * len(lines[0])
    
    beams[lines[0].find("S")] = 1

    count = 1
    for line in lines[1:]:
        next = [0] * len(line)
        for i, val in enumerate(line):
            if beams[i] > 0:
                if val=='.':
                    next[i] += beams[i]
                else:
                    count += beams[i] 
                    next[i-1] += beams[i]
                    next[i+1] += beams[i]
        beams = next

    return f"{count}"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_filename = "day07/"+sys.argv[1]
    else:
        input_filename = "day07/input.txt" # Default input file name

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