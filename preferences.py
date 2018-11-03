
def macro_calculator(daily_calories, bodyweight_pounds):
    protein = (0.8 * bodyweight_pounds)
    fat = (0.5 * bodyweight_pounds)
    net_carbs = ((daily_calories - (4 * protein) - (9 * fat)) / 4)
    fiber = 38
    meals_per_day = 3
    protein = int(protein / meals_per_day)
    fat = int(fat / meals_per_day)
    net_carbs = int(net_carbs / meals_per_day)
    fiber = int(fiber / meals_per_day)
    return {'Protein':protein, 'Fat':fat, 'Net carbs':net_carbs, 'Fiber':fiber}

# print(macro_calculator(1600, 160))

macro_targets = {'Protein': 64, 'Fat': 40, 'Net carbs': 46, 'Fiber': 19}
macro_targets = {'Protein': 42, 'Fat': 26, 'Net carbs': 30, 'Fiber': 12}