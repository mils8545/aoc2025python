import time

from day01 import day1
from day02 import day2
from day03 import day3
from day04 import day4
from day05 import day5
from day06 import day6
from day07 import day7
from day08 import day8
from day09 import day9

total = 0.0
print("Day - 1")
input_filename = "day01/input.txt" # Default input file name
puzzle_input : list[str] = day1.parse_input(input_filename)
start_time : float = time.time()
print(f"Part 1: {day1.solve_part1(puzzle_input)}")
end_time : float = time.time()
total += end_time - start_time
print(f"Part 1 took - {round((end_time - start_time) * 1000)} miliseconds")
start_time = time.time()
print(f"Part 2: {day1.solve_part2(puzzle_input)}")
end_time = time.time()
total += end_time - start_time
print(f"Part 2 took - {round((end_time - start_time) * 1000)} miliseconds")
print('--------------------------------------')

print("Day - 2")
input_filename = "day02/input.txt" # Default input file name
puzzle_input : list[str] = day1.parse_input(input_filename)
start_time : float = time.time()
print(f"Part 1: {day2.solve_part1(puzzle_input)}")
end_time : float = time.time()
total += end_time - start_time
print(f"Part 1 took - {round((end_time - start_time) * 1000)} miliseconds")
start_time = time.time()
print(f"Part 2: {day2.solve_part2(puzzle_input)}")
end_time = time.time()
total += end_time - start_time
print(f"Part 2 took - {round((end_time - start_time) * 1000)} miliseconds")
print('--------------------------------------')

print("Day - 3")
input_filename = "day03/input.txt" # Default input file name
puzzle_input : list[str] = day1.parse_input(input_filename)
start_time : float = time.time()
print(f"Part 1: {day3.solve_part1(puzzle_input)}")
end_time : float = time.time()
total += end_time - start_time
print(f"Part 1 took - {round((end_time - start_time) * 1000)} miliseconds")
start_time = time.time()
print(f"Part 2: {day3.solve_part2(puzzle_input)}")
end_time = time.time()
total += end_time - start_time
print(f"Part 2 took - {round((end_time - start_time) * 1000)} miliseconds")
print('--------------------------------------')

print("Day - 4")
input_filename = "day04/input.txt" # Default input file name
puzzle_input : list[str] = day1.parse_input(input_filename)
start_time : float = time.time()
print(f"Part 1: {day4.solve_part1(puzzle_input)}")
end_time : float = time.time()
total += end_time - start_time
print(f"Part 1 took - {round((end_time - start_time) * 1000)} miliseconds")
start_time = time.time()
print(f"Part 2: {day4.solve_part2(puzzle_input)}")
end_time = time.time()
total += end_time - start_time
print(f"Part 2 took - {round((end_time - start_time) * 1000)} miliseconds")
print('--------------------------------------')

print("Day - 5")
input_filename = "day05/input.txt" # Default input file name
puzzle_input : list[str] = day1.parse_input(input_filename)
start_time : float = time.time()
print(f"Part 1: {day5.solve_part1(puzzle_input)}")
end_time : float = time.time()
total += end_time - start_time
print(f"Part 1 took - {round((end_time - start_time) * 1000)} miliseconds")
start_time = time.time()
print(f"Part 2: {day5.solve_part2(puzzle_input)}")
end_time = time.time()
total += end_time - start_time
print(f"Part 2 took - {round((end_time - start_time) * 1000)} miliseconds")
print('--------------------------------------')

print("Day - 6")
input_filename = "day06/input.txt" # Default input file name
puzzle_input : list[str] = day1.parse_input(input_filename)
start_time : float = time.time()
print(f"Part 1: {day6.solve_part1(puzzle_input)}")
end_time : float = time.time()
total += end_time - start_time
print(f"Part 1 took - {round((end_time - start_time) * 1000)} miliseconds")
start_time = time.time()
print(f"Part 2: {day6.solve_part2(puzzle_input)}")
end_time = time.time()
total += end_time - start_time
print(f"Part 2 took - {round((end_time - start_time) * 1000)} miliseconds")
print('--------------------------------------')

print("Day - 7")
input_filename = "day07/input.txt" # Default input file name
puzzle_input : list[str] = day1.parse_input(input_filename)
start_time : float = time.time()
print(f"Part 1: {day7.solve_part1(puzzle_input)}")
end_time : float = time.time()
total += end_time - start_time
print(f"Part 1 took - {round((end_time - start_time) * 1000)} miliseconds")
start_time = time.time()
print(f"Part 2: {day7.solve_part2(puzzle_input)}")
end_time = time.time()
total += end_time - start_time
print(f"Part 2 took - {round((end_time - start_time) * 1000)} miliseconds")
print('--------------------------------------')

print("Day - 8")
input_filename = "day08/input.txt" # Default input file name
puzzle_input : list[str] = day1.parse_input(input_filename)
start_time : float = time.time()
print(f"Part 1: {day8.solve_part1(puzzle_input)}")
end_time : float = time.time()
total += end_time - start_time
print(f"Part 1 took - {round((end_time - start_time) * 1000)} miliseconds")
start_time = time.time()
print(f"Part 2: {day8.solve_part2(puzzle_input)}")
end_time = time.time()
total += end_time - start_time
print(f"Part 2 took - {round((end_time - start_time) * 1000)} miliseconds")
print('--------------------------------------')
print(f"Total runtime - {round(total * 1000)} miliseconds")

print("Day - 9")
input_filename = "day09/input.txt" # Default input file name
puzzle_input : list[str] = day1.parse_input(input_filename)
start_time : float = time.time()
print(f"Part 1: {day9.solve_part1(puzzle_input)}")
end_time : float = time.time()
total += end_time - start_time
print(f"Part 1 took - {round((end_time - start_time) * 1000)} miliseconds")
start_time = time.time()
print(f"Part 2: {day9.solve_part2(puzzle_input)}")
end_time = time.time()
total += end_time - start_time
print(f"Part 2 took - {round((end_time - start_time) * 1000)} miliseconds")
print('--------------------------------------')
print(f"Total runtime - {round(total * 1000)} miliseconds")