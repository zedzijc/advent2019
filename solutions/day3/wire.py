from solutions.common.util import Coordinate, smaller_than


class Wire(object):
    """
    A class representing a wire which may have
    many horizontal and vertical paths.
    """

    def __init__(self, paths):
        self.horizontal_paths = []
        self.vertical_paths = []
        # Stores the length of the wire to the starting point of each path
        self.path_wire_length = {}
        self._add_paths(paths)

    def _add_path(self, path, container):
        container.append(path)

    def _add_vertical_path(self, vertical_path):
        self._add_path(vertical_path, self.vertical_paths)

    def _add_horizontal_path(self, horizontal_path):
        self._add_path(horizontal_path, self.horizontal_paths)

    def _add_paths(self, paths):
        """
        Adds all paths to a wire. Assumes that they are formatted according to
        XY... where X is a letter and Y is one or more digits, example: R860
        """
        current_x = 0
        current_y = 0
        total_wire_path_length = 0
        for path in paths:
            direction = path[0].upper()
            distance = int(path[1:])
            wire_path = None

            if direction == "R":
                wire_path = WirePath(current_y,
                                     current_x,
                                     current_x + distance)
                self._add_horizontal_path(wire_path)
                current_x += distance

            elif direction == "L":
                wire_path = WirePath(current_y,
                                     current_x,
                                     current_x - distance)
                self._add_horizontal_path(wire_path)
                current_x -= distance

            elif direction == "U":
                wire_path = WirePath(current_x,
                                     current_y,
                                     current_y + distance)
                self._add_vertical_path(wire_path)
                current_y += distance

            elif direction == "D":
                wire_path = WirePath(current_x,
                                     current_y,
                                     current_y - distance)
                self._add_vertical_path(wire_path)
                current_y -= distance

            # Add information about the total length of wiring for puzzle 3:2
            self.path_wire_length[wire_path] = total_wire_path_length
            total_wire_path_length += distance

    def get_horizontal_paths(self):
        return self.horizontal_paths

    def get_vertical_paths(self):
        return self.vertical_paths

    def get_path_wire_length(self, path):
        return self.path_wire_length[path]


class WireHandler(object):
    """
    Holds wires, for now assuming two, and determines their interceptions.
    """

    def __init__(self, wire_schema_a, wire_schema_b):
        self.RUNONCE = 0
        self.wire_a = Wire(wire_schema_a)
        self.wire_b = Wire(wire_schema_b)

    def get_intersections(self):
        intersections = []
        for horizontal_path in self.wire_a.get_horizontal_paths():
            intersections += self._horizontal_intersections(horizontal_path)
        for vertical_path in self.wire_a.get_vertical_paths():
            intersections += self._vertical_intersections(vertical_path)
        return intersections

    def get_shortest_wire_length(self):
        shortest_wiring_length = None
        for horizontal_path in self.wire_a.get_horizontal_paths():
            for wiring_length in self._horizontal_intersection_wire_lengths(
                    horizontal_path):
                if smaller_than(wiring_length, shortest_wiring_length):
                    shortest_wiring_length = wiring_length
        for vertical_path in self.wire_a.get_vertical_paths():
            for wiring_length in self._vertical_intersection_wire_lengths(
                    vertical_path):
                if smaller_than(wiring_length, shortest_wiring_length):
                    shortest_wiring_length = wiring_length
        return shortest_wiring_length

    def _horizontal_intersection_wire_lengths(self, horizontal_path):
        """
        Finds the total wiring length from the start of a wire to
        each intersection between given path and
        all orthogonal paths in the other wire.
        We could theoretically intersect multiple times with a single line,
        hence returns a list.
        """

        return [self.wire_a.get_path_wire_length(horizontal_path) +
                self.wire_b.get_path_wire_length(vertical_path) +
                self._get_intra_path_wiring_distance(horizontal_path,
                                                     vertical_path)
                for vertical_path in self.wire_b.get_vertical_paths()
                if vertical_path.intersects(horizontal_path)]

    def _vertical_intersection_wire_lengths(self, vertical_path):
        """
        Finds the total wiring length from the start of a wire to
        each intersection between given path and
        all orthogonal paths in the other wire.
        We could theoretically intersect multiple times with a single line,
        hence returns a list.
        """

        return [self.wire_a.get_path_wire_length(vertical_path) +
                self.wire_b.get_path_wire_length(horizontal_path) +
                self._get_intra_path_wiring_distance(horizontal_path,
                                                     vertical_path)
                for horizontal_path in self.wire_b.get_horizontal_paths()
                if horizontal_path.intersects(vertical_path)]

    def _horizontal_intersections(self, horizontal_path):
        """
        Finds the coordinates of all intersections between given path and
        all orthogonal paths in the other wire.
        We could theoretically intersect multiple times with a single line,
        hence returns a list.
        """
        return [self._get_coordinate(horizontal_path, vertical_path)
                for vertical_path in self.wire_b.get_vertical_paths()
                if vertical_path.intersects(horizontal_path)]

    def _vertical_intersections(self, vertical_path):
        """
        Finds the coordinates of all intersections between given path and
        all orthogonal paths in the other wire.
        We could theoretically intersect multiple times with a single line,
        hence returns a list.
        """
        return [self._get_coordinate(horizontal_path, vertical_path)
                for horizontal_path in self.wire_b.get_horizontal_paths()
                if horizontal_path.intersects(vertical_path)]

    def _get_coordinate(self, horizontal_path, vertical_path):
        return Coordinate(horizontal_path.get_fixed_value(),
                          vertical_path.get_fixed_value())

    def _get_intra_path_wiring_distance(self, horizontal_path, vertical_path):
        """
        Calculates the internal wiring distance within the intersecting paths.
        """

        return ((abs(horizontal_path.get_fixed_value() -
                     vertical_path.get_from_value())) +
                (abs(vertical_path.get_fixed_value() -
                     horizontal_path.get_from_value())))


class WirePath(object):
    """
    A class representing a straight path of a wire.
    Assumes that they can not go diagonally.
    """

    def __init__(self, fixed_value, from_value, to_value):
        self.fixed_value = fixed_value
        """
        We need to keep track of whether or not
        a wire path is heading up or down, left or right for puzzle 3:2.
        I.e. a path going left will have a higher from value than to value.
        """
        self.from_value = from_value
        self.to_value = to_value

    def get_fixed_value(self):
        return self.fixed_value

    def get_from_value(self):
        return self.from_value

    def get_path_range(self):
        # +1 since range is not including the end value
        if self.from_value < self.to_value:
            return range(self.from_value, self.to_value + 1)
        else:
            return range(self.to_value, self.from_value + 1)

    def intersects(self, other_path):
        return (other_path.get_fixed_value() in self.get_path_range() and
                self.fixed_value in other_path.get_path_range())
