Практическая работа № 11
import numpy as np 
 
# Заданные значения S и G 
S = 15
G = 6
S = S/10 
G = G/10 
 
# Коэффициенты полинома 
a0 = -S * (G**2 + S**2) 
a1 = (G + S)**2 
a2 = -(2*G - S) 
a3 = 1  # По условию задачи 
 
# Функция f(x), которую мы интегрируем 
def f(x): 
    return a0 + a1 * x + a2 * x**2 + a3 * x**3 
 
# Метод прямоугольников 
def rectangle_method(a, b, n): 
    h = (b - a) / n 
    result = sum(f(a + i * h) for i in range(n)) * h 
    return result 
 
# Метод трапеций 
def trapezoid_method(a, b, n): 
    h = (b - a) / n 
    result = (f(a) + f(b)) / 2 
    for i in range(1, n): 
        result += f(a + i * h) 
    result *= h 
    return result 
 
# Метод Симпсона 
def simpson_method(a, b, n): 
    h = (b - a) / n 
    result = (f(a) + f(b)) + 4 * sum(f(a + (2 * i - 1) * h) for i in range(1, n // 2 + 1)) + 2 * sum(f(a + 2 * i * h) for i in range(1, n // 2)) 
    result *= h / 3 
    return result 
 
# Интервал интегрирования и количество разбиений 
a = 0 
b = 3 
n = 1000  # Количество разбиений для точности 
 
# Вычисляем приближенное значение интеграла каждым методом 
S_rect = rectangle_method(a, b, n) 
S_trap = trapezoid_method(a, b, n) 
S_simp = simpson_method(a, b, n) 
 
print(f"Метод прямоугольников: {S_rect}") 
print(f"Метод трапеций: {S_trap}") 
print(f"Метод Симпсона: {S_simp}")
