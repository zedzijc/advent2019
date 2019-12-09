class Coordinate(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y


def smaller_than(a, b):
    """
    Smaller than function that treats comparison to None as True
    """
    if b is None:
        return True
    return a < b


def strings_to_integers(strings):
    integers = []
    for string in strings:
        try:
            integers.append(int(string))
        except TypeError:
            pass
    return integers


def get_manhattan_distance(from_coordinate, to_coordinate=Coordinate(0, 0)):
    return (abs(from_coordinate.get_x() - to_coordinate.get_x()) +
            abs(from_coordinate.get_y() - to_coordinate.get_y()))
