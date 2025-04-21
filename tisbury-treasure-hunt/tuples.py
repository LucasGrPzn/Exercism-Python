"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record: tuple) -> str:
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    :param record: tuple - with a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """

    coordinate = record[1]
    return coordinate


def convert_coordinate(coordinate: str) -> tuple:
    """Split the given coordinate into tuple containing its individual components.

    :param coordinate: str - a string map coordinate
    :return: tuple - the string coordinate split into its individual components.
    """

    components = coordinate[0], coordinate[1]
    return components


def compare_records(azara_record: tuple, rui_record: tuple) -> bool:
    """Compare two record types and determine if their coordinates match.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, tuple(coordinate_1, coordinate_2), quadrant) trio.
    :return: bool - do the coordinates match?
    """

    first_coordinate = azara_record[1]
    second_coordinate = rui_record[1][0] + rui_record[1][1]

    if first_coordinate == second_coordinate:
        return True
    return False


def create_record(azara_record: tuple, rui_record: tuple) -> tuple | str:
    """Combine the two record types (if possible) and create a combined record group.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: tuple or str - the combined record (if compatible), or the string "not a match" (if incompatible).
    """

    is_compatible = compare_records(azara_record, rui_record)

    if is_compatible:
        combined_record = azara_record + rui_record
        return combined_record
    return 'not a match'


def clean_up(combined_record_group: tuple) -> str:
    """Clean up a combined record group into a multi-line string of single records.

    :param combined_record_group: tuple - everything from both participants.
    :return: str - everything "cleaned", excess coordinates and information are removed.

    The return statement should be a multi-lined string with items separated by newlines.

    (see HINTS.md for an example).
    """

    multi_line_str = """"""
    aux_str = ''
    for group in combined_record_group:
        aux_str = f"('{group[0]}', '{group[2]}', {group[3]}, '{group[4]}')\n"
        multi_line_str += aux_str

    return multi_line_str
