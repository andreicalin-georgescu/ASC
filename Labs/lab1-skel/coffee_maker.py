"""
A command-line controlled coffee maker.
"""

import sys
from load_recipes import load


"""
Implement the coffee maker's commands. Interact with the user via stdin and print to stdout.

Requirements:
    - use functions
    - use __main__ code block
    - access and modify dicts and/or lists
    - use at least once some string formatting (e.g. functions such as strip(), lower(),
    format()) and types of printing (e.g. "%s %s" % tuple(["a", "b"]) prints "a b"
    - BONUS: read the coffee recipes from a file, put the file-handling code in another module
    and import it (see the recipes/ folder)

There's a section in the lab with syntax and examples for each requirement.

Feel free to define more commands, other coffee types, more resources if you'd like and have time.
"""

"""
Tips:
*  Start by showing a message to the user to enter a command, remove our initial messages
*  Keep types of available coffees in a data structure such as a list or dict
e.g. a dict with coffee name as a key and another dict with resource mappings (resource:percent)
as value
"""

# Commands
EXIT = "exit"
LIST_COFFEES = "list"
MAKE_COFFEE = "make"  #!!! when making coffee you must first check that you have enough resources!
HELP = "help"
REFILL = "refill"
RESOURCE_STATUS = "status"
LOAD = "load"
commands = [EXIT, LIST_COFFEES, MAKE_COFFEE, REFILL, RESOURCE_STATUS, LOAD, HELP]

# Coffee examples
ESPRESSO = "espresso"
AMERICANO = "americano"
CAPPUCCINO = "cappuccino"

# Resources examples
WATER = "water"
COFFEE = "coffee"
MILK = "milk"

# Coffee maker's resources - the values represent the fill percents
RESOURCES = {WATER: 100, COFFEE: 100, MILK: 100}

"""
Example result/interactions:

I'm a smart coffee maker
Enter command:
list
americano, cappuccino, espresso
Enter command:
status
water: 100%
coffee: 100%
milk: 100%
Enter command:
make
Which coffee?
espresso
Here's your espresso!
Enter command:
refill
Which resource? Type 'all' for refilling everything
water
water: 100%
coffee: 90%
milk: 100%
Enter command:
exit
"""

def run(command):
    command = command.lower()

    global available, RECIPES
    global refill

    if command == RESOURCE_STATUS:
        for key in RESOURCES:
            print('%s: %s%%' % (key, RESOURCES[key]))

    elif command == LIST_COFFEES:
        print(coffee_types)

    elif command == REFILL:
        refill = 1
        print("Which resource? Type 'all' for refilling everything")
        resource = sys.stdin.readline().strip().lower()
        if resource == "all":
            for key in RESOURCES:
                RESOURCES[key] = 100
        else:
            RESOURCES[resource] = 100

    elif command == LOAD:
        RECIPES = load()
        print(RECIPES)

    elif command == MAKE_COFFEE:
        print("Which coffee?")
        current_coffee = sys.stdin.readline().strip().lower()

        try:
            RECIPES
        except NameError:
            print("No recipes loaded. Please use load command first")
        else:
            if current_coffee == "espresso":
                if RESOURCES[WATER] < RECIPES[ESPRESSO][WATER] or RESOURCES[COFFEE] < RECIPES[ESPRESSO][COFFEE] \
                    or RESOURCES[MILK] < RECIPES[ESPRESSO][MILK]:
                    print("Not enough resources: can't make coffee")
                else:
                    RESOURCES[WATER] -=  RECIPES[ESPRESSO][WATER]
                    RESOURCES[COFFEE] -= RECIPES[ESPRESSO][COFFEE]
                    print("Here's your espresso")
            elif current_coffee == "cappuccino":
                if RESOURCES[WATER] < RECIPES[CAPPUCCINO][WATER] or RESOURCES[COFFEE] < RECIPES[CAPPUCCINO][COFFEE] \
                    or RESOURCES[MILK] < RECIPES[CAPPUCCINO][MILK]:
                    print("Not enough resources: can't make coffee")
                else:
                    RESOURCES[WATER] -= RECIPES[CAPPUCCINO][WATER]
                    RESOURCES[COFFEE] -= RECIPES[CAPPUCCINO][COFFEE]
                    RESOURCES[MILK] -= RECIPES[CAPPUCCINO][MILK]
                    print("Here's your cappuccino")

            else:
                if RESOURCES[WATER] < RECIPES[AMERICANO][WATER] or RESOURCES[COFFEE] < RECIPES[AMERICANO][COFFEE] \
                    or RESOURCES[MILK] < RECIPES[AMERICANO][MILK]:
                    print("Not enough resources: can't make coffee")
                else:
                    RESOURCES[WATER] -= RECIPES[AMERICANO][WATER]
                    RESOURCES[COFFEE] -= RECIPES[AMERICANO][COFFEE]
                    print("Here's your americano")
    else:
        print(commands)

if __name__ == "__main__":
    print("I'm a simple coffee maker")
    print("Enter command:")

    coffee_types = [ESPRESSO, AMERICANO, CAPPUCCINO]

    available = 0
    refill = 0

    input = sys.stdin.readline().strip()
    while input != EXIT:
        run(input)
        input = sys.stdin.readline().strip()
    print("Machine closing. Bye, bye!")