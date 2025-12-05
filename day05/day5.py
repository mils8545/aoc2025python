import sys, time

def parse_input(filename : str):
    with open(filename, 'r') as f:
        # Adjust parsing based on the specific problem's input format
        lines : list[str] = [line.strip() for line in f]
    return lines

def neighbours(x: int, y: int, width: int, height: int) -> list[tuple[int, int]]:
    options = [(1,0), (1,1), (1,-1), (0,1), (-1,0), (-1,-1), (-1,1), (0,-1)]
    result : list[tuple[int,int]] = []
    for option in options:
        newx : int = x  + option[0]
        newy : int = y + option[1]
        if newx >= 0 and newx < width and newy >= 0 and newy < height:
            result.append((newx, newy))
    return result

def solve_part1(lines : list[str]):
    ranges : list[tuple[int,int]] = []
    ingredients : list[int] = []

    for line in lines:
        if "-" in line:
            left, right = line.split("-")
            ranges.append((int(left), int(right)))
            continue
        if len(line) > 0:
            ingredients.append(int(line))

    count : int = 0

    for ingredient in ingredients:
        for r in ranges:
            left, right = r
            if ingredient >= left and ingredient <= right:
                count += 1
                break

    return f"{count}"

def solve_part2(lines : list[str]):
    ranges : list[tuple[int,int]] = []

    for line in lines:
        if "-" in line:
            left, right = line.split("-")
            ranges.append((int(left), int(right)))
            continue

    ranges.sort()

    current = 0
    while current < len(ranges):
        left = ranges[current][0]    
        right = ranges[current][1]
        i = current + 1
        added = False
        while i < len(ranges) and right + 1 >= ranges[i][0]:
            right = max(ranges[i][1], right)
            del ranges[i]
            added = True
        if added:
            ranges[current] = (left, right)
        else:
            current += 1
    
    result = 0

    for range in ranges:
        result += range[1] - range[0] + 1

    return f"{result}"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_filename = "day05/"+sys.argv[1]
    else:
        input_filename = "day05/input.txt" # Default input file name

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