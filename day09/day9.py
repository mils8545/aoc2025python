import sys, time, math

def parse_input(filename : str):
    with open(filename, 'r') as f:
        # Adjust parsing based on the specific problem's input format
        lines : list[str] = [line.strip() for line in f]
    return lines

class Point:
    def __init__(self, x: int, y: int, z : int = 0):
        self.x = x
        self.y = y
        self.z = z
    def distanceTo(self : 'Point', other : 'Point'):
        return math.sqrt(pow(self.x - other.x, 2) + pow(self.y - other.y, 2) + pow(self.z - other.z, 2))
    def rectArea(self : 'Point', other : 'Point'):
        return (abs(self.x - other.x) + 1) * (abs(self.y - other.y) + 1)
    def __str__(self) -> str:
        return f"x:{self.x}, y:{self.y}, z:{self.z}"

class Edge:
    def __init__(self, p1: Point, p2: Point):
        if p1.x == p2.x:
            self.type = "Vert"
            if p1.y < p2.y:
                self.p1 = p1
                self.p2 = p2
            else:
                self.p1 = p2
                self.p2 = p1
        else:
            self.type = "Hor"
            if p1.x < p2.x:
                self.p1 = p1
                self.p2 = p2
            else:
                self.p1 = p2
                self.p2 = p1

    def __str__(self) -> str:
        return f"{self.p1} : {self.p2}"

class Rect:
    def __init__(self, p1 : Point, p2 : Point):
        self.x1 = min(p1.x, p2.x)
        self.x2 = max(p1.x, p2.x)
        self.y1 = min(p1.y, p2.y)
        self.y2 = max(p1.y, p2.y)
    def inside(self, e : Edge):
        # Both points inside rectangle
        if e.p1.x > self.x1 and e.p2.x < self.x2 \
            and e.p1.y > self.y1 and e.p2.y < self.y2:
            return True
        if e.type == "Vert":
            # Edge is left/right of rectangle
            if e.p1.x <= self.x1 or e.p1.x >= self.x2:
                return False
            # Edge crosses top of rectangle
            if e.p1.y < self.y1 and e.p2.y > self.y1:
                return True
            # Edge crosses bottom of rectangle
            if e.p1.y < self.y2 and e.p2.y > self.y2:
                return True
            # Edge starts on top or ends on bottom of rectangle
            if e.p1.y == self.y1 or e.p2.y == self.y2:
                return True
        else:
            # Edge is above or below rectangle
            if e.p1.y <= self.y1 or e.p1.y >= self.y2:
                return False
            # Edge crosses left edge of rectangle
            if e.p1.x < self.x1 and e.p2.x > self.x1:
                return True
            # Edge crosses right edge of rectangle
            if e.p1.x < self.x2 and e.p2.x > self.x2:
                return True
            # Edge starts on left edge or ends on right edge of rectangle
            if e.p1.x == self.x1 or e.p2.x == self.x2:
                return True
        return False
    
    def __str__(self):
        return f"{self.x1}, {self.y1}, {self.x2}, {self.y2}"

def solve_part1(lines : list[str]):
    points : list[Point] = []
    for line in lines:
        xstr, ystr = line.split(",")
        points.append(Point(int(xstr), int(ystr)))

    max_area = 0
    for i in range(len(points)-1):
        for j in range(i + 1, len(points)):
            area = points[i].rectArea(points[j])
            if area > max_area:
                max_area = area

    return f"The largest rectangle is {max_area} tiles in size"

def solve_part2(lines : list[str]):
    points : list[Point] = []
    for line in lines:
        xstr, ystr = line.split(",")
        points.append(Point(int(xstr), int(ystr)))
    edges : list[Edge] = []
    for i in range(len(points)):
        edges.append(Edge(points[i],points[(i+1)%len(points)]))

    max_area = 0

    for i in range(len(points)-1):
        for j in range(i + 1, len(points)):
            area = points[i].rectArea(points[j])
            if area > max_area:
                rect = Rect(points[i], points[j])
                good = True
                for edge in edges:
                    if rect.inside(edge):
                        good = False
                        break
                if good:
                    max_area = area

    return f"The largest rectangle is {max_area} tiles in size"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_filename = "day09/"+sys.argv[1]
    else:
        input_filename = "day09/input.txt" # Default input file name

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