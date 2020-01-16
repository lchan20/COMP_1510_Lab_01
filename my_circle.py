PI = 3.14159
radius = 0
radius = float(input("enter a radius value for a circle: "))
double_radius = 2*radius
circumference = 2*PI*radius
print("circumference is " + str(circumference))
area = PI*radius*radius
print("area is " + str(area))
double_radius_area = PI*double_radius*double_radius
double_radius_circumference = 2*PI*double_radius
circumference_ratio = double_radius_circumference/circumference
area_ratio = double_radius_area/area
print("The circumference is increased by " + str(circumference_ratio) + " when radius is doubled")
print("The area is increased by " + str(area_ratio) + " When radius is doubled")
