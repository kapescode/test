#Example 1: printing count up to 4

# count = 10

# while count > 0:
#     print(count)
#     count -= 1
#     #count = count +1

#Example 2
#   random_sent = "Hello there General Kenobi"
#   for letter in random_sent:
#        print(letter)


#Example 3 
# youtube_list = ["Aarons", "Zerka", "Miniminter", "KSI" ]

# for youtuber in youtube_list:
#     print("washed Youtuber", youtuber)

#Example 4
    #range(start, stop, step)

# for number in range(0,10,2):
#     print(number)

# #Example 5
random_sent = "Danny Aarons is braindead in among us"

random_sent_split = random_sent.split(" ")
print(random_sent_split)
for letter in random_sent_split: 
    print(letter)


#Example 6
print("This is example 6")

for i in range(1,4):
    for j in range(1,4):
        print(i*j, end="")
    print()
        
