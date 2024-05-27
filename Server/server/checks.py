from typing import Any


def check_data_integrity(data: Any):
    """
    Check for data integrity
    e.g. our data has `request` as a field,
    if its value is instance of a list
    """
    pass


def check_client_in_game(data: Any):
    """
    Check that will ask database or server
    whether the client is in a game.
    So we are able to avoid passing through the whole branch
    the handling of `GAME` requests
    """
    pass


def check_client_paired(data: Any):
    """
    Check intended to ask the server is the client
    is actually paired with another client.
    It will be used to avoid trying to send messages to a disconnected
    pair.
    """
    pass
