from solutions.common.util import Coordinate


class Wire(object):
    """
    A class representing a wire which may have
    many horizontal and vertical paths.
    """

    def __init__(self, paths):
        self.horizontal_paths = []
        self.vertical_paths = []
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
        for path in paths:
            direction = path[0].upper()
            distance = int(path[1:])

            if direction == "R":
                self._add_horizontal_path(
                    WirePath(current_y,
                             range(current_x, current_x + distance)))
                current_x += distance

            elif direction == "L":
                self._add_horizontal_path(
                    WirePath(current_y,
                             range(current_x - distance, current_x)))
                current_x -= distance

            elif direction == "U":
                self._add_vertical_path(
                    WirePath(current_x,
                             range(current_y, current_y + distance)))
                current_y += distance

            elif direction == "D":
                self._add_vertical_path(
                    WirePath(current_x,
                             range(current_y - distance, current_y, )))
                current_y -= distance

    def get_horizontal_paths(self):
        return self.horizontal_paths

    def get_vertical_paths(self):
        return self.vertical_paths


class WireHandler(object):
    """
    Holds wires, for now assuming two, and determines their interceptions.
    """

    def __init__(self, wire_schema_a, wire_schema_b):
        self.wire_a = Wire(wire_schema_a)
        self.wire_b = Wire(wire_schema_b)

    def get_intersections(self):
        intersections = []
        for horizontal_path in self.wire_a.get_horizontal_paths():
            intersections += self._horizontal_intersections(horizontal_path)
        for vertical_path in self.wire_a.get_vertical_paths():
            intersections += self._vertical_intersections(vertical_path)
        return intersections

    def _horizontal_intersections(self, horizontal_path):
        # We could theoretically intersect multiple times with a single line
        return [Coordinate(horizontal_path.get_fixed_value(),
                           vertical_path.get_fixed_value())
                for vertical_path in self.wire_b.get_vertical_paths()
                if vertical_path.intersects(horizontal_path)]

    def _vertical_intersections(self, vertical_path):
        # We could theoretically intersect multiple times with a single line
        return [Coordinate(horizontal_path.get_fixed_value(),
                           vertical_path.get_fixed_value())
                for horizontal_path in self.wire_b.get_horizontal_paths()
                if horizontal_path.intersects(vertical_path)]


class WirePath(object):
    """
    A class representing a straight path of a wire.
    Assumes that they can not go diagonally.
    """

    def __init__(self, fixed_value, path_range):
        self.fixed_value = fixed_value
        self.path_range = path_range

    def get_fixed_value(self):
        return self.fixed_value

    def get_path_range(self):
        return self.path_range

    def intersects(self, other_path):
        return (other_path.get_fixed_value() in self.path_range and
                self.fixed_value in other_path.get_path_range())
