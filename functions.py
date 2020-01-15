def format_name(first, last):
    my_name = first_name+" " + last_name
    full_name = my_name.strip()
    return full_name.title()


first_name = str(input("Enter your first name: "))
last_name = str(input("Enter your family name: "))
print("My full name is " + format_name(first_name, last_name))
