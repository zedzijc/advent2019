from solutions.common.parse import parse_csv_to_list
from solutions.common.util import strings_to_integers


def _restore_gravity_assist_program(intcode, noun=12, verb=2):
    # As per the required restoration in the problem specification.
    intcode[1] = noun
    intcode[2] = verb


def _process_intcode(intcode):
    """
    Processes a series of instructions.
    An intcode instruction consists of an operator,
    two memory value positions, and a memory result position"""
    code_size = 4
    index = 0
    while index + 3 < len(intcode):
        operator = intcode[index]
        value_a = intcode[index + 1]
        value_b = intcode[index + 2]
        result = intcode[index + 3]
        if operator == 1:
            intcode[result] = intcode[value_a] + intcode[value_b]
        elif operator == 2:
            intcode[result] = intcode[value_a] * intcode[value_b]
        elif operator == 99:
            return intcode[0]
        else:
            raise RuntimeError("Unsupported intcode operator: {0}".format(
                operator))
        index += code_size


def _get_intcode(puzzle_input):
    return (strings_to_integers(parse_csv_to_list(puzzle_input)[0]))


def get_intcode_value(puzzle_input):
    intcode = _get_intcode(puzzle_input)
    _restore_gravity_assist_program(intcode)
    print("Intcode program result: {0}".format(_process_intcode(intcode)))


def get_moon_gravity_assist(puzzle_input):
    original_intcode = _get_intcode(puzzle_input)
    for noun in range (0, 100):
        for verb in range (0, 100):
            intcode = original_intcode.copy()
            _restore_gravity_assist_program(intcode, noun, verb)
            if (_process_intcode(intcode.copy()) == 19690720):
                print("Moon gravity assist result: {0}".format(100 * noun + verb))
