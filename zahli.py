"""
This module provides common functions and class of the application zahli.
"""

# Imports
import re


def process_message(message):
    """
    This function processes a certain message formulated by the user and returns
    a response messages.

    :param message: The message of the user or None. If None is handed over, the chat bot
        returns a welcome message.
    :return: A response message.
    """
    if message is None:
        response = welcome()
    elif is_praise_message(message):
        response = "Sehr gerne"
    elif is_error_message(message):
        response = "Sorry"
    elif is_exit_message(message):
        response = "Auf Wiedersehen"
    else:
        response = extract_eval(message)

    return response


def welcome():
    """
    This function returns a welcome message.

    :return: A welcome message as str.
    """
    return "Hallo ich bin Zahli, stelle mir eine Aufgabe:"


def extract_eval(message: str):
    """
    This function extracts an expression from a message, evaluates it and
    returns the result. If no expression could be evaluated, an excuse message
    is returned.

    :param message: The message to evaluate.
    :return: The evaluated expression or an excuse message.
    """
    expr = extract_expression(message)
    result = None

    if expr is not None:
        try:
            result = eval(expr)
            result = str(result).replace(".", ",")
            result = str(result).replace("True", "Wahr")
            result = str(result).replace("False", "Falsch")
        except(ValueError, SyntaxError):
            result = None

    if result is not None:
        response = f"Die Loesung ist {result}"
    else:
        response = "Leider weiss ich die Loesung nicht"

    return response


def extract_expression(message: str):
    """
    This method extracts an expression from a message formulated by the user.

    :param message: The message as str.
    :return: The expression or None, if no expression could be extracted.
    """
    expr = None

    if message is not None:
        index = None

        # Lower message
        message = message.lower()

        # Clean German characters
        message = re.sub("ü", "ue", message)
        message = re.sub("ö", "oe", message)
        message = re.sub("ä", "ae", message)
        message = re.sub("ß", "ss", message)

        # Clean numbers
        message = re.sub(r"\beins\b", "1", message)
        message = re.sub(r"\bzwei\b", "2", message)
        message = re.sub(r"\bdrei\b", "3", message)
        message = re.sub(r"\bvier\b", "4", message)
        message = re.sub(r"\bfünf\b", "5", message)
        message = re.sub(r"\bfuenf\b", "5", message)
        message = re.sub(r"\bsechs\b", "6", message)
        message = re.sub(r"\bsieben\b", "7", message)
        message = re.sub(r"\bacht\b", "2", message)
        message = re.sub(r"\bneun\b", "9", message)
        message = re.sub(r"\bnull\b", "0", message)

        # Clean operators
        message = re.sub(r"\bkleiner als\b", "<", message)
        message = re.sub(r"\bkleiner\b", "<", message)

        message = re.sub(r"\bgroesser als\b", ">", message)
        message = re.sub(r"\bgroesser\b", ">", message)

        message = re.sub(r"=", "==", message)
        message = re.sub(r"\bist gleich\b", "==", message)
        message = re.sub(r"\bgleich\b", "==", message)

        # Clean floats
        message = re.sub(",", ".", message)

        # Clean operators
        message = message.replace("x", "*")
        message = re.sub(r"\bplus\b", "+", message)
        message = re.sub(r"\bmal\b", "*", message)
        message = re.sub(r"\bdurch\b", "/", message)
        message = re.sub(r"\bgeteilt durch\b", "/", message)
        message = re.sub(r"\bhoch\b", "**", message)

        first_bracket = re.search(r"\(", message)
        first_digit = re.search(r"\d", message)

        if first_bracket is not None:
            index = first_bracket.start()
        elif first_digit is not None:
            index = first_digit.start()

        if index is not None:
            # Extract term
            expr = message[index:].strip()

    return expr


def is_exit_message(message: str):
    """
    This function returns True of the user has requested to exit the application.

    :param message: The user message.
    :return: True, if the user has requested to exit the application.
    """
    exit_commands = ("ende", "wiedersehen", "tschüss", "ciao", "exit")
    return any(command in message.lower() for command in exit_commands)


def is_error_message(message: str):
    """
    This function returns True of the user has complained about an error.

    :param message: The user message.
    :return: True, if the user has complained about an error.
    """
    error_phrases = ("nein", "nicht", "falsch", "stimmt nicht", "schlecht")
    return any(phrase in message.lower() for phrase in error_phrases)


def is_praise_message(message: str):
    """
    This function returns True of the user has praised the bot.

    :param message: The user message.
    :return: True if the user has praised the chat bot.
    """
    phrases = ("gut", "super", "spitze", "prima", "danke", "richtig")
    return any(phrase in message.lower() for phrase in phrases)
