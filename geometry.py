import math

def calculate_area(radius):
    return math.pi * radius ** 2

def calculate_rectangle_area(a: float, b: float) -> float:
    if a <= 0 or b <= 0:
        raise ValueError("Стороны должны быть больше нуля")
    return a * b

if __name__ == "__main__":
    print("Version A")

