from solutions.common.parse import parse_input_as_list
from solutions.common.util import strings_to_integers
import math


def get_module_fuel_consumption(mass):
    """
    Divide module mass by three, round down, and subtract 2.
    """
    return math.floor(mass / 3) - 2


def compute_required_fuel(puzzle_input):
    """
    Solution to Day 1 Puzzle 1
    Computes and prints the total fuel required to
    launch a list of modules based on their mass.
    """
    masses = strings_to_integers(parse_input_as_list(puzzle_input))
    required_fuel = 0

    for mass in masses:
        required_fuel += get_module_fuel_consumption(mass)
    print("Required fuel is {0}".format(required_fuel))
