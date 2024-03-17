#while loops

count = 3                               #Total number in count
while count < 10:                       #loop will continue as the count is <10
    print("Count is: ", count)              
    count += 4                          #inciremental value, can be changed, and will go back to the loop until this condition is satisfied or not


#For loops
    pokemon_list = ["DannyAarons", "Charmander", "Squirtle", "Sneako"]
for pokemon in pokemon_list:
	print(pokemon)

#range functions
#the numbers represent (start, stop, step)
#If not provided start value it will be default to 0, and incriment step will default to 1

for i in range(1,10,2):
    print(i)
