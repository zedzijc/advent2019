from solutions.common.parse import parse_csv_to_list
from solutions.common.util import strings_to_integers

"""
def get_next_intcode_instruction(intcode, starting_index):
    if starting_index + 3 < len(intcode):
        operation = intcode[starting_index]
        first_value = intcode[starting_index + 1]
        other_value = intcode[starting_index + 2]
        result = intcode[starting_index + 3]
"""


def _restore_gravity_assist_program(intcode):
    # As per the required restoration in the problem specification.
    intcode[1] = 12
    intcode[2] = 2


def _get_instructions(intcode):
    instructions = []
    """
    An intcode instruction consists of an operator,
    two memory value positions, and a memory result position"""
    code_size = 4
    index = 0
    while index + 3 < len(intcode):
        instructions.append(intcode[index:index + code_size])
        index += code_size
    return instructions


def _process_intcode(intcode):
    # Processes a series of intcode.
    for operator, value_a, value_b, result in _get_instructions(intcode):
        if operator == 1:
            intcode[result] = intcode[value_a] + intcode[value_b]
        elif operator == 2:
            intcode[result] = intcode[value_a] * intcode[value_b]
        elif operator == 99:
            return intcode[0]
        else:
            raise RuntimeError("Unsupported intcode operator: {0}".format(
                operator))


def get_intcode_value(puzzle_input):
    intcode = (strings_to_integers(parse_csv_to_list(puzzle_input)[0]))
    _restore_gravity_assist_program(intcode)
    print(_process_intcode(intcode))
