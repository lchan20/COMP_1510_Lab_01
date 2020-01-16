def format_name(first, last):
    my_name = (str(first.strip()) + " " + str(last.strip()))
    return my_name.title()


def tripler(anything):
    return 3*str(anything)


def this_year(number):
    first_step = int(number)*30
    second_step = first_step*67
    third_step = second_step/int(number)
    return int(third_step + 10)


def base_conversion():
    base = int(input("Enter a base you want to convert to (2-9): "))
    max_base_10 = (base ** 4) - 1
    print("The maximum base 10 number for your chosen base is " + str(max_base_10))
    num_base_10 = int(input("Enter a number that is less than or equal to " + str(max_base_10) + ": "))
    last_digit = num_base_10 % base
    num_base_10 = num_base_10 // base
    third_digit = num_base_10 % base
    num_base_10 = num_base_10 // base
    second_digit = num_base_10 % base
    num_base_10 = num_base_10 // base
    first_digit = num_base_10 % base
    new_num_str = str(first_digit) + str(second_digit) + str(third_digit) + str(last_digit)
    new_num_int = int(new_num_str)
    print("The converted base " + str(base) + " number is " + new_num_str)
    print(new_num_int)


def main():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your family name: ")
    print("My full name is " + format_name(first_name, last_name))
    something = input("Enter something you want tripled: ")
    print("This is " + something + " tripled: " + tripler(something))
    random_number = input("Enter a random number to get the number of the current year: ")
    print("The current year is: " + str(this_year(random_number)))
    base_conversion()
    print("complete!")


if __name__ == '__main__':
    main()
