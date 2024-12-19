def area(a, b): 
    '''Принимает стороны a и b, возвращает площадь прямоугольника по формуле a*b'''
    if a > 0 and b > 0:
        return a * b
    return 0

def perimeter(a, b):
    '''Принимает стороны a и b, возвращает периметр прямоугольника по формуле 2*(a+b)'''
    if a > 0 and b > 0:
        return 2*(a + b)
    return 0