def get_box_area(width, length, height):
    area = width * length * height
    print(area)

def get_triangle_area(base, height):
    area = 1/2 * base * height
    print(area)

def get_circle_area(radius):
    area = 22/7 * pow(radius, 2)
    print(area)

triangle_area_1 = get_triangle_area(4, 4)
circle_area_1 = get_circle_area(7)