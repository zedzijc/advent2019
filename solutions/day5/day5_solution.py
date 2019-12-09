from solutions.common.parse import parse_csv_to_list
from solutions.common.util import strings_to_integers


def _get_operator(opcodes):
    string_code = str(opcodes)
    if len(string_code) == 1:
        return opcodes
    if string_code[1] == 0:
        return int(string_code[0])
    return int(string_code[-2:])


def _parameter_modes(opcodes):
        # Reverse the opcodes
        opcodes = str(opcodes)[::-1]
        parameter_modes = [0, 0, 0]
        index = 0
        # Parameter modes start from index 2
        for parameter_mode in opcodes[2:]:
            parameter_modes[index] = int(parameter_mode)
            index += 1
        return parameter_modes


def _process_intcode(intcode):
    """
    Processes a series of instructions.
    Allows for intcodes of various lengths according to day 5 requirements.
    """
    index = 0
    while index + 3 < len(intcode):
        operator = _get_operator(intcode[index])
        if operator == 1 or operator == 2:
            code_size = 4
            parameter_modes = _parameter_modes(intcode[index])
            parameters = [intcode[index + 1],
                          intcode[index + 2],
                          intcode[index + 3]]
            value_a = (parameters[0] if parameter_modes[0] == 1
                       else intcode[parameters[0]])
            value_b = (parameters[1] if parameter_modes[1] == 1
                       else intcode[parameters[1]])
            if operator == 1:
                intcode[parameters[2]] = value_a + value_b
            else:
                intcode[parameters[2]] = value_a * value_b
        elif operator == 3 or operator == 4:
            code_size = 2
            value_a = intcode[index + 1]
            if operator == 3:
                # The only input instruction has value 1 as per puzzle info.
                intcode[value_a] = 1
            elif operator == 4:
                parameter_modes = _parameter_modes(intcode[index])
                if parameter_modes[0] == 1:
                    diagnostic_code = value_a
                else:
                    diagnostic_code = intcode[value_a]
                print("Diagnostic code: {0}".format(diagnostic_code))
        elif operator == 99:
            return
        else:
            raise RuntimeError("Unsupported intcode operator: {0}".format(
                operator))
        index += code_size


def _get_intcodes(puzzle_input):
    intcodes = []
    for raw_intcode in parse_csv_to_list(puzzle_input):
        intcodes.append(strings_to_integers(raw_intcode))
    return intcodes


def get_intcode_diagnostic_codes(puzzle_input):
    for intcode in _get_intcodes(puzzle_input):
        _process_intcode(intcode)
