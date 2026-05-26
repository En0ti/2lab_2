import math

def calculate_area(radius):
    return math.pi * radius ** 2

def calculate_rectangle_area(a, b):
    return a * b

if __name__ == "__main__":
    print(f"Area: {calculate_area(5)}")

