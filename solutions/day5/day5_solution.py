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


def _process_intcode(intcode, input_value):
    """
    Processes a series of instructions.
    Allows for intcodes of various lengths according to day 5 requirements.
    """
    single_params = [3, 4]
    double_params = [5, 6]
    triple_params = [1, 2, 7, 8]
    index = 0
    while index < len(intcode):
        operator = _get_operator(intcode[index])
        if operator in triple_params or operator in double_params:
            code_size = 4
            parameter_modes = _parameter_modes(intcode[index])
            parameters = [intcode[index + 1],
                          intcode[index + 2],
                          intcode[index + 3]]
            value_a = (parameters[0] if parameter_modes[0] == 1
                       else intcode[parameters[0]])
            value_b = (parameters[1] if parameter_modes[1] == 1
                       else intcode[parameters[1]])
            if operator in triple_params:
                value_c = 0
                if operator == 1:
                    value_c = value_a + value_b
                elif operator == 2:
                    value_c = value_a * value_b
                elif operator == 7:
                    if value_a < value_b:
                        value_c = 1
                else:
                    if value_a == value_b:
                        value_c = 1
                intcode[parameters[2]] = value_c
            elif operator in double_params:
                code_size = 3
                if operator == 5:
                    if value_a != 0:
                        index = value_b
                        continue
                elif operator == 6:
                    if value_a == 0:
                        index = value_b
                        continue
        elif operator in single_params:
            code_size = 2
            value_a = intcode[index + 1]
            if operator == 3:
                intcode[value_a] = input_value
            elif operator == 4:
                parameter_modes = _parameter_modes(intcode[index])
                if parameter_modes[0] == 1:
                    diagnostic_code = value_a
                else:
                    diagnostic_code = intcode[value_a]
                print("Diagnostic code: {0}".format(diagnostic_code))
        elif operator == 99:
            return intcode[0]
        else:
            raise RuntimeError("Unsupported intcode operator: {0}".format(
                operator))
        index += code_size


def _get_intcodes(puzzle_input):
    intcodes = []
    for raw_intcode in parse_csv_to_list(puzzle_input):
        intcodes.append(strings_to_integers(raw_intcode))
    return intcodes


def _get_diagnostic_codes(puzzle_input, input_value):
    for intcode in _get_intcodes(puzzle_input):
        _process_intcode(intcode, input_value)


def get_intcode_diagnostic_codes_a(puzzle_input):
    _get_diagnostic_codes(puzzle_input, 1)


def get_intcode_diagnostic_codes_b(puzzle_input):
    _get_diagnostic_codes(puzzle_input, 5)
