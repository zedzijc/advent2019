def number_length(number):
    return len(str(number))


def get_int_by_index(number, from_index, to_index):
    return int(str(number)[from_index:to_index])


def process_digit(index, max_index,
                  previous_digit, min_digit,
                  max_digit=10, double=False):
    passwords = 0
    for digit in range(min_digit, max_digit):
        # Are we at the end of the number?
        if index < max_index:
            # No, keep going.
            passwords += process_digit(index + 1, max_index, digit, digit,
                                       10, double or digit == previous_digit)
        else:
            # Yes, have we satisfied the repeating numbers requirement?
            if double or digit == previous_digit:
                passwords += 1
    return passwords


def get_possible_passwords():
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
                               leading_min_digit,
                               get_int_by_index(min_password, 1, 2))
    # Handle anything from 444444 to 799999
    passwords += process_digit(first_index,
                               password_length,
                               None,
                               leading_min_digit + 1,
                               leading_max_digit)
    print("Number of possible passwords are: {0}".format(passwords))
