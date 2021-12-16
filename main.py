import datetime
import json
import os.path
import traceback
from action import Automation

BASE_PATH = os.path.dirname(__file__)
ROUTINE_FILE = os.path.join(BASE_PATH, "routine.json")
VERBOSE = 0
HEADLESS = 1
ON_ERROR_PROCEED = 0
routines = dict()


def printf(message):
    if VERBOSE == 1:
        print(message)
        with open("log.log", "a+") as f:
            date = datetime.datetime.now()
            f.write(date.strftime("%d/%m/%Y, %H:%M:%S") + ": " + message + "\n")

    else:
        with open("log.log", "a+") as f:
            date = datetime.datetime.now()
            f.write(date.strftime("%d/%m/%Y, %H:%M:%S") + ": " + message + "\n")


def getVariable(dictionary, key):
    try:
        value = dictionary[key]
        return value
    except KeyError:
        return False
    except Exception:
        printf("Exception:")
        printf(traceback.format_exc())
        return False


def main():
    global VERBOSE, HEADLESS, ON_ERROR_PROCEED
    if not os.path.isfile(ROUTINE_FILE):
        print("File 'routine.json' is not present on the directory.")
        print("Exiting...")
        exit(1)

    else:
        with open(ROUTINE_FILE, "r") as f:
            routines = json.load(f)

        VERBOSE = getVariable(routines, "verbose") if getVariable(routines, "verbose") is not False else 0
        HEADLESS = getVariable(routines, "headless") if getVariable(routines, "headless") is not False else 1
        ON_ERROR_PROCEED = getVariable(routines, "on_error_proceed") if getVariable(routines, "on_error_proceed") is not False else 0

        printf("Starting...")

        at = Automation(HEADLESS, ON_ERROR_PROCEED, routines)
        at.runActions()


if __name__ == "__main__":
    main()
