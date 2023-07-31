#literally what the file name says lol
# F = 1.8C + 32
# C = 5/9 * (F - 32)

print("\nim finna convert between celcius and fahrenheit  for you lol\n")

conversion_type = input("are you trying to convert celcius or fahrenheit? (input F or C): ")

if conversion_type == "F":
    F = int (input("key in temperature: "))
    C = 5/9 * (F-32)
    print(C, "C", sep="")

C = int (input("key in temperature: "))
F = 1.8 * C + 32
print(F, "F", sep="")