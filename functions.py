def format_name(first, last):
    my_name = (str(first) + " " + str(last))
    full_name = my_name.strip()
    return full_name.title()


def tripler(anything):
    return 3*str(anything)


def this_year(number):
    first_step = int(number)*30
    second_step = first_step*67
    third_step = second_step/int(number)
    return int(third_step + 10)


def main():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your family name: ")
    print("My full name is " + format_name(first_name, last_name))
    something = input("Enter something you want tripled: ")
    print("This is " + something + " tripled: " + tripler(something))
    random_number = input("Enter a random number to get the number of the current year: ")
    print("The current year is: " + str(this_year(random_number)))
    print("complete!")


if __name__ == '__main__':
    main()