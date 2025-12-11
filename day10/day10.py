import sys, time
from z3 import Int, IntVector, Optimize, Sum, sat # type: ignore

def parse_input(filename : str):
    with open(filename, 'r') as f:
        # Adjust parsing based on the specific problem's input format
        lines : list[str] = [line.strip() for line in f]
    return lines

def lightswitchflick(l: str, switch : list[int]):
    result = ""
    for i in range(len(l)):
        if i in switch:
            if l[i] == '.':
                result += '#'
            else:
                result += '.'
        else:
            result += l[i]
    return result

# Taken from https://gist.github.com/HexTree/0827398e16a39f6c1a7e62cabc782579
def get_ip_solution(goal : list[int], buttons : list[list[int]]): 
    n = len(goal)
    X = IntVector('x', len(buttons))

    s = Optimize()
    for _k in range(len(buttons)):
        s.add([x >= 0 for x in X]) # type: ignore

    A : list[list[int]] = []
    for button in buttons:
        row = [0 for _ in range(n)]
        for w in button:
            row[w] = 1
        A.append(row)

    for i in range(n):
        s.add(Sum(X[k]*A[k][i] for k in range(len(buttons))) == goal[i]) # type: ignore
    s.minimize(Sum(X)) # type: ignore

    # Check for satisfiability and get the model
    if s.check() == sat: # type: ignore
        model = s.model()
        return sum(model[k].as_long() for k in model) # type: ignore
    else:
        print("No solution found.")

def solve_part1(lines : list[str]):
    lights : list[str] = []
    switches : list[list[list[int]]] = []
    for line in lines:
        entries = line.split(" ")
        lights.append(entries[0][1:-1])
        switchlist : list[list[int]] = []
        for switchstr in entries[1:-1]:
            switchlist.append(list(map(int, switchstr.strip("()").split(","))))
        switches.append(switchlist)

    total = 0
    for i in range(len(lights)):

        seen : set[str] = set()
        seen.add("." * len(lights[i]))
        queue : list[tuple[str, int]] = [("." * len(lights[i]), 0)]
        target = lights[i]
        slist = switches[i]
        done = False
        while not done:
            current, pushes = queue.pop(0)
            if current == target:
                done = True
                total += pushes
            else:
                for switch in slist:
                    result = lightswitchflick(current,switch)
                    if result not in seen:
                        queue.append((result,pushes + 1))
                        seen.add(result)
    return f"The fewest presses required to set the lights is {total}"

def solve_part2(lines : list[str]):
    joltages : list[list[int]] = []
    switches : list[list[list[int]]] = []
    for line in lines:
        entries = line.split(" ")
        joltages.append(list(map(int, entries[-1].strip("{}").split(","))))
        switchlist : list[list[int]] = []
        for switchstr in entries[1:-1]:
            switchlist.append(list(map(int, switchstr.strip("()").split(","))))
        switches.append(switchlist)
    
    total : int = 0

    for i in range(len(joltages)):
        total += get_ip_solution(joltages[i], switches[i]) # type: ignore

    return f"The fewest presses required to set the joltages is {total}"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_filename = "day10/"+sys.argv[1]
    else:
        input_filename = "day10/input.txt" # Default input file name

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