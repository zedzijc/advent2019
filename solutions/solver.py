from solutions.day1.day1_solution import get_required_fuel, get_total_required_fuel
from solutions.day2.day2_solution import get_intcode_value, get_moon_gravity_assist
from solutions.day3.day3_solution import find_most_central_intersection, find_shortest_wiring_distance
from solutions.day4.day4_solution import get_possible_passwords, get_limited_passwords
from solutions.day5.day5_solution import get_intcode_diagnostic_codes_a, get_intcode_diagnostic_codes_b


solutions = {1: {1: get_required_fuel,
                 2: get_total_required_fuel},
             2: {1: get_intcode_value,
                 2: get_moon_gravity_assist},
             3: {1: find_most_central_intersection,
                 2: find_shortest_wiring_distance},
             4: {1: get_possible_passwords,
                 2: get_limited_passwords},
             5: {1: get_intcode_diagnostic_codes_a,
                 2: get_intcode_diagnostic_codes_b},
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
        if puzzle_input is None:
            solutions[day][puzzle]()
        else:
            solutions[day][puzzle](puzzle_input)
    else:
        print("Combination of Day: {0} and Puzzle: {1} "
              "is not yet implemented".format(day, puzzle))
