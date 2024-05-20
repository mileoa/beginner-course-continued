from arithmetic.power import power

def is_right_triangle(a_leg, b_leg, c_hypotenuse):
    return power(a_leg, 2) + power(b_leg, 2) == power(c_hypotenuse, 2)