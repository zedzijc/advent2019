from solutions.common.parse import parse_input_as_list
from solutions.common.util import strings_to_integers
import math


def get_required_fuel(puzzle_input):
    """
    Solution to Day 1 Puzzle 1
    Computes and prints the total fuel required to
    launch a list of modules based on their mass.
    """
    _compute_required_fuel(puzzle_input)


def get_total_required_fuel(puzzle_input):
    """
    Solution to Day 1 Puzzle 2:
    Computes and prints the total fuel required to
    launch a list of modules based on their mass.
    Also takes into consideration that the added fuel requires additional fuel,
    and so on, when recursive is set to True.
    """
    _compute_required_fuel(puzzle_input, True)


def _get_module_fuel_consumption(mass):
    """
    Divide module mass by three, round down, and subtract 2.
    """
    return math.floor(mass / 3) - 2


def _get_total_module_fuel_consumption(mass):
    """
    Divide module mass by three, round down, and subtract 2.
    """
    fuel_consumption = math.floor(mass / 3) - 2
    # Get any additionally required fuel, from adding fuel based on mass.
    if fuel_consumption > 0:
        return (fuel_consumption +
                _get_total_module_fuel_consumption(fuel_consumption))
    # Never return negative fuel required.
    return 0


def _compute_required_fuel(puzzle_input, recursive=False):
    masses = strings_to_integers(parse_input_as_list(puzzle_input))
    required_fuel = 0

    for mass in masses:
        if recursive:
            required_fuel += _get_total_module_fuel_consumption(mass)
        else:
            required_fuel += _get_module_fuel_consumption(mass)
    print("Required fuel is {0}".format(required_fuel))
