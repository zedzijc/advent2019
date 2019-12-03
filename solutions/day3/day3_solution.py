from solutions.day3.wire import WireHandler
from solutions.common.parse import parse_csv_to_list
from solutions.common.util import get_manhattan_distance


def find_most_central_intersection(puzzle_input):
    wire_schemas = parse_csv_to_list(puzzle_input)
    wire_handler = WireHandler(wire_schemas[0], wire_schemas[1])
    intersections = wire_handler.get_intersections()

    print("Shortest manhattan distance to an intersection is: {0}".format(
        find_shortest_manhattan_distance(intersections)))


def find_shortest_manhattan_distance(intersections):
    shortest_manhattan_distance = None
    for intersection in intersections:
        manhattan_distance = get_manhattan_distance(intersection)
        if shortest_manhattan_distance is None:
            shortest_manhattan_distance = manhattan_distance
        else:
            if manhattan_distance < shortest_manhattan_distance:
                shortest_manhattan_distance = manhattan_distance
    if shortest_manhattan_distance == 0:
        print("Warning: Either there is an intersection at (0,0), " +
              "or something has gone wrong!")
    return shortest_manhattan_distance
