import sys, time, math

def parse_input(filename : str):
    with open(filename, 'r') as f:
        # Adjust parsing based on the specific problem's input format
        lines : list[str] = [line.strip() for line in f]
    return lines

class Point:
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z
    def distanceTo(self : 'Point', other : 'Point'):
        return math.sqrt(pow(self.x - other.x, 2) + pow(self.y - other.y, 2) + pow(self.z - other.z, 2))
    def __str__(self):
        return f"x:{self.x}, y:{self.y}, z:{self.z}"
    
def solve_part1(lines : list[str]):
    if len(lines) > 50:
        connection_count = 1000
    else:
        connection_count = 10
    nodecount = len(lines)
    groups : list[int] = []
    nodes : list[Point] = []
    for i in range(nodecount):
        groups.append(i)
        xstr, ystr, zstr = lines[i].split(',')
        nodes.append(Point(int(xstr), int(ystr), int(zstr)))

    distances : list[tuple[float, int, int]] = []
    for i in range(nodecount-1):
        for j in range(i + 1, nodecount):
            distances.append((nodes[i].distanceTo(nodes[j]), i, j))
    
    distances.sort()

    for i in range(connection_count):
        _, first, second = distances[i]
        if groups[first] != groups[second]:
            gnum = groups[first]
            other = groups[second]
            for i in range(len(groups)):
                if groups[i] == other:
                    groups[i] = gnum

    circuits : dict[int, int]= {}
    for group in groups:
        if group in circuits:
            circuits[group] += 1
        else:
            circuits[group] = 1

    result = list(circuits.values())
    result.sort(reverse = True)

    return f"The product of the number of boxes in the largest 3 circuits is {result[0] * result[1] * result[2]}"

def solve_part2(lines : list[str]):
    nodecount = len(lines)
    groups : list[int] = []
    nodes : list[Point] = []
    for i in range(nodecount):
        groups.append(i)
        xstr, ystr, zstr = lines[i].split(',')
        nodes.append(Point(int(xstr), int(ystr), int(zstr)))

    distances : list[tuple[float, int, int]] = []
    for i in range(nodecount-1):
        for j in range(i + 1, nodecount):
            distances.append((nodes[i].distanceTo(nodes[j]), i, j))
    
    distances.sort()

    newconn = 0

    j = 0
    while True:
        _, first, second = distances[j]
        if groups[first] != groups[second]:
            newconn += 1
            if newconn == nodecount - 1:
                return f"The product of the x coordinates of the last two connected boxes is {nodes[first].x * nodes[second].x}"
            gnum = groups[first]
            other = groups[second]
            for i in range(len(groups)):
                if groups[i] == other:
                    groups[i] = gnum
        j += 1

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_filename = "day08/"+sys.argv[1]
    else:
        input_filename = "day08/input.txt" # Default input file name

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