import numpy as np
from scipy import optimize
import itertools

import fileio

from preferences import macro_targets

input_rows, labels = fileio.from_csv('ingredients.csv')
ingredients = {}
for row in [f for f in input_rows if f['Ingredient'] != '']:
    row['Unit weight'] = int(row['Unit weight'])
    row['Fat'] = int(row['Fat'])
    row['Protein'] = int(row['Protein'])
    row['Fiber'] = int(row['Fiber'])
    row['Net carbs'] = int(row['Net carbs'])
    ingredients[row['Ingredient']] = row
# print(ingredients)

proteins = ['chicken breast', 'salmon fillet', 'pork shoulder fresh raw lean only']
vegetables = ['broccoli', 'spinach', 'cabbage']
fillers = ['Kellogg\'s All-Bran Buds 1/3 cup', 'yam', 'peanut butter chunky', 'protein shake', 'apple with skin 3+1/4 diam', 'carrot', 'cottage cheese 1% milkfat']
for protein in proteins:
    assert protein in ingredients, protein
for vegetable in vegetables:
    assert vegetable in ingredients, vegetable
for filler in fillers:
    assert filler in ingredients, filler

for protein in proteins:
    for vegetable in vegetables:

        best_candidate = {'combination':[], 'units':(), 'x':500}    # x is just some big number

        for element in list(itertools.combinations(fillers, 2)):
            combination = [protein, vegetable] + list(element)

            left_array = []
            right_array = []

            for macronutrient in ['Protein', 'Fat', 'Fiber', 'Net carbs']:
                row = []
                for ingredient in combination:
                    row.append(ingredients[ingredient][macronutrient])

                left_array.append(row)
                right_array.append(macro_targets[macronutrient])

            A = np.array(left_array)
            B = np.array(right_array)
            x = optimize.nnls(A,B)

            candidate = {'combination':combination, 'units':list(x[0]), 'x':x[1]}

            if candidate['x'] < best_candidate['x']:    # we want to minimize the second number
                best_candidate = candidate
           
        print(best_candidate)
        for n, ingredient in enumerate(best_candidate['combination']):
            print(ingredient)
            print('    ' + str(int(round(best_candidate['units'][n] * ingredients[ingredient]['Unit weight']))) + ' g')
        calories = 0
        g_fat = 0
        g_protein = 0
        g_fiber = 0
        g_net_carbs = 0
        for n, ingredient in enumerate(best_candidate['combination']):
            calories += best_candidate['units'][n] * ingredients[ingredient]['Fat'] * 9
            calories += best_candidate['units'][n] * ingredients[ingredient]['Protein'] * 4
            calories += best_candidate['units'][n] * ingredients[ingredient]['Net carbs'] * 4

            g_fat += best_candidate['units'][n] * ingredients[ingredient]['Fat']
            g_protein += best_candidate['units'][n] * ingredients[ingredient]['Protein']
            g_fiber += best_candidate['units'][n] * ingredients[ingredient]['Fiber']
            g_net_carbs += best_candidate['units'][n] * ingredients[ingredient]['Net carbs']
        print(str(int(calories)) + ' calories')
        print(int(g_fat), 'g fat, ', int(g_protein), 'g protein, ', int(g_fiber), 'g fiber, ', int(g_net_carbs), 'g net carbs')
        print()
