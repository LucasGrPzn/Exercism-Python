"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args: int) -> list:
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    wagons = list(args)
    return wagons


def fix_list_of_wagons(each_wagons_id: list, missing_wagons: list) -> list:
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    last1, last2, first, *rest = each_wagons_id

    new_order_wagons = first, *missing_wagons, *rest, last1, last2

    return list(new_order_wagons)


def add_missing_stops(routing: dict, **kwargs) -> dict:
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    value_stops = list(kwargs.values())
    route_with_stops = {**routing, "stops": value_stops}

    return route_with_stops


def extend_route_information(route: dict, more_route_information: dict) -> dict:
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    route_with_info = {**route, **more_route_information}
    return route_with_info


def fix_wagon_depot(wagons_rows: list[list[tuple]]) -> list[list[tuple]]:
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    organized = list(zip(*wagons_rows))
    for index, item in enumerate(organized):
        organized[index] = list(item)
    return organized
