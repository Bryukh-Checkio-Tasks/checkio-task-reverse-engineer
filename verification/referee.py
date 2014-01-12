from math import hypot
from random import randint
from checkio.signals import ON_CONNECT
from checkio import api
from checkio.referees.multicall import CheckiORefereeMulti

from tests import TESTS
import re

MAX_STEP = 50


def initial_referee(data):
    data["step_count"] = 0
    data["input"] = []
    return data


def process_referee(referee_data, user_result):
    expression = referee_data['expression']

    referee_data['step_count'] += 1
    if referee_data['step_count'] > MAX_STEP:
        referee_data.update({"result": False, "result_addon": "Too many steps."})
        return referee_data
    if (not isinstance(user_result, (list, tuple)) or len(user_result) != 3 or
            not isinstance(user_result[1], int) or not isinstance(user_result[2], int) or
            not isinstance(user_result[0], str)):
        referee_data.update({"result": False, "result_addon": "The function should return a list with three values."})
        return referee_data
    guess, x, y = user_result
    guess = guess.replace("/", "//")
    referee_data["guess"] = guess
    if not re.match(r"\A[xy +*/()-]*\Z", guess):
        referee_data.update({"result": False, "result_addon": "Your guess does not look like an expression."})
        return referee_data
    try:
        result_expr = eval(expression)
    except ZeroDivisionError:
        result_expr = "ZeroDivisionError"

    try:
        result = eval(guess)
    except ZeroDivisionError:
        result = "ZeroDivisionError"
    except Exception as er:
        referee_data.update({"result": False, "result_addon": "We got the error when evaluate your expression: {0}.".format(er)})
        return referee_data

    referee_data["input"].append([x, y, result_expr])
    referee_data.update({"result": True, "result_addon": "Next Step"})
    return referee_data


def is_win_referee(referee_data):
    if not referee_data["result"]:
        return False
    guess = referee_data['guess']
    expression = referee_data['expression']
    for _ in range(10):
        x, y = randint(-100, 100), randint(-100, 100)
        try:
            result_guess = eval(guess)
        except ZeroDivisionError:
            result_guess = "ZeroDivisionError"

        try:
            result_expr = eval(expression)
        except ZeroDivisionError:
            result_expr = "ZeroDivisionError"

        if result_guess != result_expr:
            return False
    return True


api.add_listener(
    ON_CONNECT,
    CheckiORefereeMulti(
        tests=TESTS,
        initial_referee=initial_referee,
        process_referee=process_referee,
        is_win_referee=is_win_referee,
    ).on_ready)
