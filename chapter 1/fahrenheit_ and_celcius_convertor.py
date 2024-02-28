#literally what the file name says lol
# F = 1.8C + 32
# C = 5/9 * (F - 32)

print("\nim finna convert between celcius and fahrenheit for you lol\n")

while True:
    # get the input temperature saved as "conversion_type" variable
    # bracketting the whole thing and putting .lower() converts the input to lowercase, 
    # making it NOT case sensitive
    conversion_type = input(("are you trying to convert celcius or fahrenheit? (input F or C): ")).lower()

    if conversion_type == "f":
        #input fahrenheit temperature and save as integer variable "F"
        F = int (input("key in temperature: "))
        C = 5/9 * (F-32)        #convert to C
        C = round(C, 2)         #convert to 2 decimal points
        print(C, "*C", sep="")

    elif conversion_type == "c":
        #input celcius temperature and save as integer variable "C"
        C = int (input("key in temperature: "))
        F = 1.80 * C + 32       #convert to F
        F = round(F, 2)         #convert to 2 decimal points
        print(F, "*F", sep="")
    else:
        print("\nwrong input bro. try again.")