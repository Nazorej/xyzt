# Это программа на Python
# 13x²+2x-t=0
# 23y²+2y-t=0
# 35z²+12z-t=-1
# x=-8, y=-6, z=-5, t=816

from sympy import symbols, Eq, solve

def solve_equation(coefficients, t_value):
    variable = symbols('variable', integer=True)
    eq = Eq(coefficients[0]*variable**2 + coefficients[1]*variable - t_value, coefficients[2])
    solutions = solve(eq)
    return [sol for sol in solutions if sol.is_integer]

# Коэффициенты для каждого уравнения
equations_coefficients = [
    (13, 2, 0),
    (23, 2, 0),
    (35, 12,-1)
]

variables = ['x', 'y', 'z']

# Проверяем каждое значение t
for t in range(1, 1001):
    solutions = []
    for coefficients in equations_coefficients:
        # Получаем решения для каждого уравнения
        equation_solutions = solve_equation(coefficients, t)
        solutions.append(equation_solutions)
    # Если для всех трех уравнений есть решения, выводим их
    if all(solutions):
        print(f'Для t = {t}, решениями являются:', ', '.join([f'{var}={sol[0]}' for var, sol in zip(variables, solutions)]))
