"""
	Bonus task: load all the available coffee recipes from the folder 'recipes/'
	File format:
		first line: coffee name
		next lines: resource=percentage

	info and examples for handling files:
		http://cs.curs.pub.ro/wiki/asc/asc:lab1:index#operatii_cu_fisiere
		https://docs.python.org/3/library/io.html
		https://docs.python.org/3/library/os.path.html
"""

RECIPES_FOLDER = "recipes"

import os, os.path


def load():

    files = os.listdir(RECIPES_FOLDER)
    recipes = {}

    for file in files:

        f = open('recipes/' + file, 'r')

        recipe_name = f.readline().rstrip()
        dict = {}
        for line in f:
            x = line.rstrip().split('=')
            ingredient = x[0]
            value = int(x[1])
            dict[ingredient] = value

        recipes[recipe_name] = dict

    return recipes