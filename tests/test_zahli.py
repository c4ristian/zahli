"""
This module provides test cases for the application Zahli.
"""

# Imports
import zahli


def test_process_message():
    """
    Test case for the function parse_question.

    :return: None.
    """
    # Input None
    response = zahli.process_message(None)
    assert response == "Hallo ich bin Zahli, stelle mir eine Aufgabe:"

    # Exit messages
    assert zahli.process_message("tschüss") == "Auf Wiedersehen"
    assert zahli.process_message("also ende zahli") == "Auf Wiedersehen"
    assert zahli.process_message("auf wiedersehen") == "Auf Wiedersehen"

    # Valid calculations
    assert zahli.process_message("wieviel ist 1 + 1") == "Die Loesung ist 2"
    assert zahli.process_message("was ist 5x2") == "Die Loesung ist 10"
    assert zahli.process_message("wieviel ist 3 hoch 2") == "Die Loesung ist 9"
    assert zahli.process_message("wieviel ist eins hoch drei") == "Die Loesung ist 1"
    assert zahli.process_message("fünf durch zwei") == "Die Loesung ist 2,5"
    assert zahli.process_message("was ist 5 ** 3") == "Die Loesung ist 125"

    # Boolean expressions
    assert zahli.process_message("ist 5 kleiner als 3") == "Die Loesung ist Falsch"
    assert zahli.process_message("ist 5 größer 3") == "Die Loesung ist Wahr"
    assert zahli.process_message("ist 5 groesser 3") == "Die Loesung ist Wahr"
    assert zahli.process_message("5=3") == "Die Loesung ist Falsch"
    assert zahli.process_message("5 ist gleich 5") == "Die Loesung ist Wahr"

    # Error messages
    assert zahli.process_message("Das ist falsch") == "Sorry"

    # Praise messages
    assert zahli.process_message("DAS WAR SUPER") == "Sehr gerne"

    # Invliad calculations
    assert zahli.process_message("wieviel ist 1 + x") == \
           "Leider weiss ich die Loesung nicht"

    assert zahli.process_message("meine name ist christian") == \
           "Leider weiss ich die Loesung nicht"
