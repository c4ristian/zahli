"""
This script runs the application Zahli.

Examples
--------
>>> python main.py

Silent mode:
>>> python main.py -s
"""

# Imports
import logging
import argparse
import speech_recognition as sr
import pyttsx3
import zahli


def _parse_cmd_args():
    """
    This method parses the command line arguments of the program.
    :return: The parsed command line arguments.
    """
    parser = argparse.ArgumentParser(description='Zahli speech bot.')
    parser.add_argument("-s", action='store_true', help="Activate silent mode.")

    args = parser.parse_args()
    return args


def _listen_to_user(micro, recognizer):
    """
    This function listens to the user and returns its input.

    :param micro: A microphone or None. If None is handed over,
        the application runs in silent mode as chat bot.
    :param recognizer: The recognizer for speech processing or None. If None is handed over,
        the application runs in silent mode.
    :return: The user input.
    """
    if micro is not None and recognizer is not None:
        with micro as source:
            audio = recognizer.listen(source, phrase_time_limit=5)

        logging.info("Sende Anfrage...")
        message = recognizer.recognize_google(audio, language="de")
    else:
        message = input(">>> ")

    logging.info(f"Ergebnis: {message}")

    return message


def _main():
    """
    This function runs the application.

    :return: None.
    """
    # Parse command line args
    args = _parse_cmd_args()
    silent = args.s

    # Initialization
    engine = None
    recognizer = None
    micro = None

    if not silent:
        engine = pyttsx3.init()

        recognizer = sr.Recognizer()
        recognizer.pause_threshold = 0.8
        recognizer.phrase_threshold = 0.2
        recognizer.dynamic_energy_threshold = False
        recognizer.energy_threshold = 10

        micro = sr.Microphone()

    # Start conversation
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

    response = zahli.process_message(None)
    _write_and_say(response, engine)

    while "wiedersehen" not in response.lower():
        try:
            message = _listen_to_user(micro, recognizer)
            response = zahli.process_message(message)
        except (sr.UnknownValueError, sr.WaitTimeoutError):
            response = "Das habe ich nicht verstanden"

        _write_and_say(response, engine)


def _write_and_say(message: str, engine):
    """
    This function writes and says a message.

    :param message: The message.
    :param engine: The speech engine.
    :return: None.
    """
    logging.info(message)

    if engine is not None:
        engine.say(message)
        engine.runAndWait()


# Main method to start the export
if __name__ == '__main__':
    _main()
