import math

def area(r):
    '''Принимает радиус r, возвращает площадь окружности по формуле pi*r*r'''
    if r > 0:
        return math.pi * r * r
    return 0

def perimeter(r):
    '''Принимает радиус r, возвращает периметр окружности по формуле 2*pi*r'''
    if r > 0:
        return 2 * math.pi * r
    return 0