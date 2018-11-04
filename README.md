# Meal Plan Generator

This program is used to create rudimentary meal plans that are nutritionally balanced.

Provided with data on the macronutrient profiles of several foods, the user specifies their daily macronutrient requirements, the number of meals they wish to eat per day, and the foods they would like to include in their meal. Using the simplex algorithm functionality provided in scipy, the program outputs a meal containing some or all of the user-specified foods in amounts that will best fulfill the macronutrient targets.

```
chicken breast
    91 g
spinach
    249 g
yam
    75 g
peanut butter chunky
    50 g
521 calories
25 g fat,  41 g protein,  12 g fiber,  30 g net carbs
```

## Prerequisites

In addition to the Python Standard Library, this program requires numpy and scipy to carry out the optimization.

## Usage:

If the user knows their daily calorie requirement, they can use the provided macro_calculator() function in preferences.py to calculate their daily macronutrient targets. Otherwise, they can input their macronutrient goals into preferences.py as a dict.

The user then needs to add the foods they wish to include in their meal as a list of strings into main.py. These strings must correspond to entries in the ingredients.csv containing nutrient information of foods. This information can be obtained online from sites such as the USDA database. The information must be in grams.

Upon running, the program will print out the list of input foods and their amounts to match the macronutrient target as closely as possible. (Depending on the macronutrient goals and input foods, the output meals can turn out quite strange.)

## To do:

Be able to specify which foods are "unit" foods, and must be consumed in integer quantities, things like cans of tuna, clementines, string cheese, pudding cups, or eggs.

Be able to specify foods that MUST be in a particular meal, subtracting them from the macronutrient target.

Allow the user to add recipes. Have the program treat the recipes as if they were singular ingredients. Output the amounts in both grams and fractions of the recipe amount.

Add functionality to tag foods and handle them by category. Be able to filter foods that are meat, animal-based, or branded.