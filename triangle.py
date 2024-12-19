def area(a, h):
    '''Принимает сторону a и высоту h, возвращает площадь треугольника по формуле a*h'''
    if a > 0 and h > 0:
        return a * h / 2
    return 0

def perimeter(a, b, c):
    '''Принимает стороны a, b и c, возвращает периметр треугольника по формуле a + b + c'''
    if a > 0 and b > 0 and c > 0:
        return a + b + c
    return 0