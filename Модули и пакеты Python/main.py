import arithmetic
from geometry.pythagorean_theorem import is_right_triangle

a_side = 3
b_side = 4
c_side = 5

print("Сторона a =", a_side)
print("Сторона b =", b_side)
print("Сторона c =", c_side)

if is_right_triangle(a_side, b_side, c_side):
    print("Это прямоугольный треугольник.")
else:
   print("Это не прямоугольный треугольник.")

print()
print("2 в квадрте = ", arithmetic.power.power2(2))