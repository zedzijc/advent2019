import argparse
from solutions import solver


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("day", type=int, choices=range(1, 25),
                        help="A calendar day")
    parser.add_argument("puzzle", type=int, choices=range(1, 3),
                        help="A daily puzzle")
    parser.add_argument("--input", type=str, help="Puzzle input")
    args = parser.parse_args()
    solver.solve(args.day, args.puzzle, args.input)


if __name__ == "__main__":
    parse_arguments()
