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
    result : int = 0
    width = len(lines[0])
    height = len(lines)
    for y in range(height):
        for x in range(width):
            if lines[y][x] == '@':
                count = 0
                for newx, newy in neighbours(x, y, width, height):
                    if lines[newy][newx] == '@':
                        count += 1
                if count < 4:
                    result += 1

    return f"There are {result} moveable rolls of paper"

def solve_part2(lines : list[str]):
    grid : list[list[str]]= []
    for line in lines:
        grid.append(list(line))
    result : int = 0
    width = len(grid[0])
    height = len(grid)
    done = False
    while not done:
        remove : list[tuple[int,int]] = []
        for y in range(height):
            for x in range(width):
                if grid[y][x] == '@':
                    count = 0
                    for newx, newy in neighbours(x, y, width, height):
                        if grid[newy][newx] == '@':
                            count += 1
                    if count < 4:
                        remove.append((x,y))
                        result += 1
        if len(remove) == 0:
            done = True
        for x, y in remove:
            grid[y][x] = '.'

    return f"There are {result} moveable rolls of paper"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_filename = "day04/"+sys.argv[1]
    else:
        input_filename = "day04/input.txt" # Default input file name

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