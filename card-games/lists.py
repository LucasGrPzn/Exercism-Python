"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number: int) -> list:
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """

    list_rounds = list(range(number, number + 3))
    return list_rounds


def concatenate_rounds(rounds_1: list, rounds_2: list):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    all_rounds = rounds_1 + rounds_2
    return all_rounds


def list_contains_round(rounds: list, number: int) -> bool:
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """

    if number in rounds:
        return True
    return False


def card_average(hand: list) -> float:
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """

    cards_in_hand = len(hand)
    average = sum(hand) / cards_in_hand
    return round(average, 2)


def approx_average_is_average(hand: list) -> bool:
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """

    cards_in_hand = len(hand)
    true_average = sum(hand) / cards_in_hand

    average_first_last = (hand[0] + hand[-1]) / 2
    
    middle_card = hand[cards_in_hand // 2]

    if true_average in (average_first_last, middle_card):
        return True
    return False


def average_even_is_average_odd(hand: list) -> bool:
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    even_sum = 0
    even_count = 0
    odd_sum = 0
    odd_count = 0

    for index, number in enumerate(hand):
        if index % 2 == 0:
            even_sum += number
            even_count += 1
        else:
            odd_sum += number
            odd_count += 1
    
    calculation = even_sum / even_count == odd_sum / odd_count

    if calculation:
        return True
    return False


def maybe_double_last(hand: list):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    if hand[-1] == 11:
        hand[-1] = 22
    return hand
