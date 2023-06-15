def get_straight_from_set(set_of_ranks):
    """
    Takes in set of strings of 'A','2','3'...,'J', 'Q', 'K' and returns highest rank in straight if exists.
    Otherwise return False.

    >>> set_of_ranks_1 = {'A', '2', '4', '3', '5', '10', 'J', 'Q', 'K'}
    >>> get_straight_from_set(set_of_ranks_1)
    'A'
    >>> set_of_ranks_2 = {'A', '2', '4', '3', '5', '10', 'J', 'Q'}
    >>> get_straight_from_set(set_of_ranks_2)
    '5'
    >>> set_of_ranks_3 = {'A', '2', '3'}
    >>> get_straight_from_set(set_of_ranks_3)
    False
    >>> set_of_ranks_4 = {'7', '2', '3', '5', '9'}
    >>> get_straight_from_set(set_of_ranks_4)
    False
    """

    set_AKQJ10 = {"A", "K", "Q", "J", "10"}
    if set_AKQJ10.issubset(set_of_ranks):
        return "A"
    else:
        number_list = rank_string_to_value_list(list(set_of_ranks))
        number_list.sort(reverse=True)
        for i in range(len(number_list) - 4):
            if number_list[i] - number_list[i + 4] == 4:
                return value_to_rank_string(number_list[i])
        return False


def highest_rank(set_of_ranks):
    """
    >>> ranks = ['2','K', '3']
    >>> highest_rank(ranks)
    'K'
    """
    # Takes in list of strings of 'A','2','3'...,'J', 'Q', 'K' and returns highest rank
    number_list = rank_string_to_value_list(set_of_ranks)
    number_list.sort(reverse=True)
    return value_to_rank_string(number_list[0])


def rank_string_to_value_list(list_of_ranks):
    # Given list of ranks from 'A','2','3'...,'J', 'Q', 'K', return values
    rank_to_value_map = {
        "A": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 11,
        "Q": 12,
        "K": 13,
    }
    return list(map(rank_to_value_map.get, list_of_ranks))


def value_to_rank_string(rank_value):
    value_to_rank_map = {
        1: "A",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "10",
        11: "J",
        12: "Q",
        13: "K",
    }
    return value_to_rank_map[rank_value]


def value_to_rank_string_list(list_of_values):
    """
    >>> value_to_rank_string_list([1, 2, 3, 6])
    ['A', '2', '3', '6']
    """
    value_to_rank_map = {
        1: "A",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "10",
        11: "J",
        12: "Q",
        13: "K",
    }
    return list(map(value_to_rank_map.get, list_of_values))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
