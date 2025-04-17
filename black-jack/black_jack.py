"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""

card_values = {
    "J": 10, 
    "Q": 10, 
    "K": 10, 
    "A": 1,
    "2": 2, 
    "3": 3, 
    "4": 4, 
    "5": 5,
    "6": 6, 
    "7": 7, 
    "8": 8, 
    "9": 9, 
    "10": 10
    }

def value_of_card(card: str) -> int:
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    return card_values[card]


def higher_card(card_one: str, card_two:str) -> str | tuple:
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    if card_values[card_one] == card_values[card_two]:
        return card_one, card_two
    if card_values[card_one] > card_values[card_two]:
        return card_one
    return card_two


def value_of_ace(card_one: str, card_two: str) -> int:
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    sum_cards = card_values[card_one] + card_values[card_two]
    if card_one == "A" or card_two == "A":
        sum_cards += 10

    if sum_cards + 11 <= 21:
        return 11
    return 1


def is_blackjack(card_one: str, card_two: str) -> bool:
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    is_ace = False
    if card_one == "A" or card_two == "A":
        is_ace = True
    
    is_21 = (card_values[card_one] + card_values[card_two]) == 11 # It's 11 because the value of "A" in card_values is 1

    if (is_ace and is_21):
        return True
    return False


def can_split_pairs(card_one: str, card_two: str) -> bool:
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """

    if card_values[card_one] == card_values[card_two]:
        return True
    return False


def can_double_down(card_one: str, card_two: str) -> bool:
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """

    list_doble_down = [9, 10, 11]

    if card_values[card_one] + card_values[card_two] in list_doble_down:
        return True
    return False
