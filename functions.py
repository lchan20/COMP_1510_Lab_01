def format_name(first, last):
    my_name = first_name+" " + last_name
    full_name = my_name.strip()
    return full_name.title()


first_name = str(input("Enter your first name: "))
last_name = str(input("Enter your family name: "))
print("My full name is " + format_name(first_name, last_name))


def tripler(anything):
    return 3*str(anything)


something = input("Enter something you want tripled: ")
print("This is " + something + " tripled: " + tripler(something))


def this_year(number):
    first_step = int(number)*30
    second_step = first_step*67
    third_step = second_step/number
    return int(third_step + 10)


random_number = int(input("Enter a random number to get the number of the current year: "))
print("The current year is: " + str(this_year(random_number)))




