#define function with input parameters
def happy_birthday(name, age):
    print("Happy Birthday", name)
    print("You are", age, "years old\n")

#calls the functions with these arguments
happy_birthday("dick", 21)
happy_birthday("dumbass", 30)
happy_birthday("cock", 23)

#define function to add two arguments
def add(x, y):
    z = x + y
    return z    #sends out the sum

print(add(1,2)) #call the function and print out the answer

#define function to create a full name
def create_name(first, last):
    first = first.capitalize() #capitalises both strings
    last = last.capitalize()
    return first + " " + last #return as a combined string

#call the combined string "full_name"
full_name = create_name("spongebob", "squarepants")
print(full_name) #prints out the full_name