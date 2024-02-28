def happy_birthday(name, age):
    """define function with input parameters"""
    print("Happy Birthday", name)
    print("You are", age, "years old\n")

#calls the functions with these arguments
happy_birthday("dick", 21)
happy_birthday("dumbass", 30)
happy_birthday("cock", 23)


def add(x, y):
    """define a function to sum two arguments"""
    z = x + y
    return z    #sends out the computed sum

print(add(1,2)) #call the function and print out the answer

def create_name(first, last):
    """define a function to create a full name by adding first and last name together.
    also capitalises the first letter automatically"""
    first = first.capitalize() #capitalises both strings
    last = last.capitalize()
    return first + " " + last #return as a combined string

#call the combined string "full_name" with a first and last name
full_name = create_name("spongebob", "squarepants")
print(full_name) #prints out the full_name