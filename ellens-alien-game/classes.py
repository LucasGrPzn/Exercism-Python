"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Number of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """

    total_aliens_created = 0

    def __init__(self, x_axis: int, y_axis: int):
        Alien.total_aliens_created += 1

        self.x_coordinate = x_axis
        self.y_coordinate = y_axis
        self.health = 3

    def hit(self):
        self.health -= 1

    def is_alive(self):
        if self.health <= 0:
            return False
        return True

    def teleport(self, new_x: int, new_y: int):
        self.x_coordinate = new_x
        self.y_coordinate = new_y

    def collision_detection(self, other_object):
        pass


def new_aliens_collection(coordinates: list[tuple]):
    alien_name = ["alien" + str(item[0]) for item in enumerate(coordinates)]

    for index, coordinate in enumerate(coordinates):
        alien_name[index] = Alien(*coordinate)

    return alien_name
