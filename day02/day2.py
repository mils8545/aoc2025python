import sys, time

def parse_input(filename : str):
    with open(filename, 'r') as f:
        # Adjust parsing based on the specific problem's input format
        lines : list[str] = [line.strip() for line in f]
    return lines

def solve_part1(lines : list[str]):
    sum : int = 0
    ranges : list[tuple[int,int]]= []
    for range_string in lines[0].split(","):
        ranges.append((int(range_string.split("-")[0]),(int(range_string.split("-")[1]))))

    for first, last in ranges:
        for i in range(first, last+1):
            i_str : str = str(i)
            if len(i_str) % 2 == 0:
                half : int = len(i_str) // 2
                if i_str[0:half] == i_str[half:]:
                    sum += i
    
    return f"The sum of the invalid IDs is: {sum}"

def solve_part2(lines : list[str]):
    sum : int = 0
    ranges : list[tuple[int,int]]= []
    for range_string in lines[0].split(","):
        ranges.append((int(range_string.split("-")[0]),(int(range_string.split("-")[1]))))

    for first, last in ranges:
        for i in range(first, last+1):
            i_str : str = str(i)
            for j in range(1,len(i_str)//2+1):
                if i_str[0:j] * (len(i_str) // j) == i_str:
                    sum += i
                    break
    
    return f"The sum of the invalid IDs is: {sum}"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_filename = "day02/"+sys.argv[1]
    else:
        input_filename = "day02/input.txt" # Default input file name

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