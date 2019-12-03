from solutions.day1.day1_solution import get_required_fuel, get_total_required_fuel
from solutions.day2.day2_solution import get_intcode_value, get_moon_gravity_assist
from solutions.day3.day3_solution import find_most_central_intersection, find_shortest_wiring_distance


solutions = {1: {1: get_required_fuel, 2: get_total_required_fuel},
             2: {1: get_intcode_value, 2: get_moon_gravity_assist},
             3: {1: find_most_central_intersection,
                 2: find_shortest_wiring_distance},
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
