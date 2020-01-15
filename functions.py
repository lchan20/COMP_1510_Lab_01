def format_name(first_name, last_name):
    my_name = first_name+" " + last_name
    return my_name.title()


first_name = str(input("Enter your first name: "))
last_name = str(input("Enter your family name: "))
print(format_name(first_name, last_name))

