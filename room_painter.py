COVERAGE = 400
length = float(input("Enter the length of the room in feet: "))
width = float(input("Enter the width of the room in feet: "))
height = float(input("Enter the height of the room in feet: "))
coats = float(input("Enter the number of coats of paint: "))
surface_area = (length*width) + (2*length*height) +(2*width*height)
coverage_needed = surface_area*coats
cans_of_paint_required = coverage_needed/COVERAGE
print("Amount of paint needed is " + str(cans_of_paint_required))
if float(cans_of_paint_required) - int(cans_of_paint_required) != 0:
    cans_to_buy = int(cans_of_paint_required) + 1
print("The number of cans needed to paint this room is " + str(cans_to_buy))
