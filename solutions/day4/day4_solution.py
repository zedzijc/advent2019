def number_length(number):
    return len(str(number))


def get_int_by_index(number, from_index, to_index):
    return int(str(number)[from_index:to_index])


def validate(password, additional_sequence_limitation):
    repeated_letter_count = 1
    previous_letter = None
    sequence_sizes = []
    for letter in password:
        if letter == previous_letter:
            repeated_letter_count += 1
        else:
            # If we are ending a sequence, store its size
            if repeated_letter_count > 1:
                sequence_sizes.append(repeated_letter_count)
            previous_letter = letter
            repeated_letter_count = 1
    if repeated_letter_count > 1:
        sequence_sizes.append(repeated_letter_count)
    if not additional_sequence_limitation:
        # Day 4 puzzle 1
        return len(sequence_sizes) > 0
    # Day 4 puzzle 2
    # Verify that there is at least one sequence with length exactly 2
    return len([sequence for sequence in sequence_sizes if sequence == 2]) > 0


def process_digit(index, max_index, min_digit,
                  max_digit=10, partial_password="", limitation=False):
    passwords = 0
    for digit in range(min_digit, max_digit):
        password = partial_password + str(digit)
        # Are we at the end of the number?
        if index < max_index:
            # No, keep going.
            passwords += process_digit(index + 1, max_index, digit,
                                       10, password, limitation)
        else:
            # Yes, have we satisfied the repeating numbers requirement?
            if validate(password, limitation):
                passwords += 1
    return passwords


def get_passwords(additional_sequence_limitation=False):
    min_password = 353096
    max_password = 843212

    password_length = number_length(max_password)
    leading_min_digit = get_int_by_index(min_password, 0, 1)
    leading_max_digit = get_int_by_index(max_password, 0, 1)
    passwords = 0
    first_index = 1
    second_index = 2
    # Handle anything from 355555 up to 399999
    passwords += process_digit(second_index,
                               password_length,
                               get_int_by_index(min_password, 1, 2),
                               partial_password=str(leading_min_digit),
                               limitation=additional_sequence_limitation)
    # Handle anything from 444444 to 799999
    passwords += process_digit(first_index,
                               password_length,
                               leading_min_digit + 1,
                               max_digit=leading_max_digit,
                               limitation=additional_sequence_limitation)
    print("Number of possible passwords are: {0}".format(passwords))


def get_limited_passwords():
    get_passwords(True)


def get_possible_passwords():
    get_passwords(False)
