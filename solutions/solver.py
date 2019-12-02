from solutions.day1.day1_solution import get_required_fuel, get_total_required_fuel
from solutions.day2.day2_solution import get_intcode_value


solutions = {1: {1: get_required_fuel, 2: get_total_required_fuel},
             2: {1: get_intcode_value},
             3: {},
             4: {},
             5: {},
             6: {},
             7: {},
             8: {},
             9: {},
             10: {},
             11: {},
             12: {},
             13: {},
             14: {},
             15: {},
             16: {},
             17: {},
             18: {},
             19: {},
             20: {},
             21: {},
             22: {},
             23: {},
             24: {}}


def has_solution(day, puzzle):
    return day in solutions and puzzle in solutions[day]


def solve(day, puzzle, puzzle_input):
    if has_solution(day, puzzle):
        solutions[day][puzzle](puzzle_input)
    else:
        print("Combination of Day: {0} and Puzzle: {1} "
              "is not yet implemented".format(day, puzzle))
