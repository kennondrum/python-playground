#Program to take user input and display a personalised greeting

welcometext = "\n\nHello!\n To generate a personalised greeting, we'll ask you some questions about you :)\n"

print(welcometext)

name = input("First off, what's your name?: ")
age  = int(input("What's your age this year?: ")) # let's do: "x years old born in xxxx"
birthyear = 2023-age
country = input("Where are you from?: ")
hobby = input("What is your favourite hobby?: ")

print("\nHi", name, "from", country, sep=' ', end='\n')
print("You're", age, "years old, born in", birthyear, end=".\n")
print("You also love", hobby, end="!\n")


''' old code lol
print("\n\nHi " +str(name), "from", country,"!")
print("You're " +str(age), "years old, born in", birthyear, ".")
print("And you LOVE", hobby, "\n")
'''