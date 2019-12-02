import csv


def parse_csv_to_list(puzzle_input):
    with open(puzzle_input, 'r') as csv_file:
        return(list(csv.reader(csv_file)))


def parse_input_as_list(puzzle_input):
    return open(puzzle_input).read().splitlines()
