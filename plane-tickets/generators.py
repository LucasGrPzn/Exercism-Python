"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number: int):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """

    index = 0
    seats = ["A", "B", "C", "D"]
    while number:
        yield seats[index]

        number -= 1
        if index == 3:
            index = 0
        else: 
            index += 1


def generate_seats(number: int):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """

    count = 0
    rows = number // 4 + 2
    seats = ["A", "B", "C", "D"]

    try:
        for row in range(1, rows):
            if row == 13:
                continue
            for seat in seats:
                yield str(row) + seat
                count += 1
            
                if count == number:
                    raise StopIteration
    except StopIteration:
        pass


def assign_seats(passengers: list[str]) -> dict:
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """

    number_of_passengers = len(passengers)
    seats = generate_seats(number_of_passengers)

    name_and_seat = {}

    for passenger in passengers:
        name_and_seat[passenger] = next(seats)

    return name_and_seat


def generate_codes(seat_numbers: list[str], flight_id: str):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """

    for seat in seat_numbers:
        ticket_code = seat + flight_id
        yield '{:0<12}'.format(ticket_code)
