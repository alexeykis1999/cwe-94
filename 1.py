# Perimeter of Square
def calculateSquarePerimeter(l):
    return  4*l

# Area of Square
def calculateSquareArea(l):
    return l**2

def calculateRectangleArea(width, height):
    return width*height

def calculateRectanglePerimeter(width, height):
    return (width+height) * 2

def calculatePyramidVolume(s, h):
    return (s*h)/3

def calculateCubeVolume(a):
    return a**3

def calculatePrismVolume(s, h):
    return s*h

def calculateRhombusArea(d1, d2):
    return (d1*d2)/2


trusted_functions = [
    'calculateCubeVolume',
    'calculateSquareArea',
    'calculatePrismVolume',
    'calculateRhombusArea',
    'calculatePyramidVolume',
    'calculateRectangleArea',
    'calculateSquarePerimeter',
    'calculateRectanglePerimeter'
]

print('Available functions:')
for i in trusted_functions: print(i)

expression = input("Type a function: ")

print(expression.split("(")[0].split("calculate").pop(), "is", eval(expression))
