# #This is my very first python program
# # 'print' method use to show the message 
# print("Hello Ravindi\nWelcome to Python Programming\n")

# # assign values for variables and print them seperatly try this
# x = 1
# a, b, c = "Ravindi", "Rohan", "Apple"

# print(a)
# print(b)
# print(c)


# #try a simple for loop 
# # for the String value "Ravindi" all the letters print in the console from one by one downwards
# for x in "Ravindi" : 
#     print (x)

# # to retrieve the data type of the variable try out the following method called 'type'
# a = 1
# print(type(a))

# #if you need to print two or more variables in one line follow this method
# name = "Ravindi"
# age = 23
# print ("My name is {} and i'm {} old".format(name,age))


# #taking data from outside
# name = str(input("What's your name?"))
# print(name)




# #simple addition calculator
# num1 = int(input("Enter 1st number: "))
# num2 = int(input("Enter 2st number: "))
# answer = num1+num2
# print(answer)


# #print same thing alone a line
# print("\n{x}star{x}\n".format(x="*"*10))



# 3 > 2 answer is True
# 4 < 1 answer is False
# 1 == 3 answer is False.... This checks if this is true or false

# x = 5
# y = 10

# if(y==x):
#     print("Yes")
# elif(y>x):
#     print("OK")
# else:
#     print("No")



# marks = int(input("Enter marks: "))

# if (marks<35):
#     print

# Slicing
# get value from a string
name = "Ravindi"
print(name[1]) #print 1st index value {R=0, a=1, v=2,...d=5,i=6 as their indexes, [0] is the index of string "R"}
print(name[-1]) # print the last letter {R=-7, a=-6, v=-3,...d=-2,i=-1}

print(name[1:3])    # print string values form 1 to 3rd index as "oh", here 3rd index wont print but starting index will print

# also this can print by naming it as a variable
result = name[4]
print(result)

print(name[:])  # print from starting point to end
print(name[::]) # print from starting point to end
print(name[2:]) # print from starting point(here given index) to end
print(name[::2])   # print from starting point to end 2 by 2 (here, "Rvni" by skipping letters between them)
print(name[2::2])   # print from starting point to end 2 by 2 (here, "vni" by skipping letters between them)
print(name[::-1])   # print from last to first, backwards)


# simple functions
word = "          dore fa sola tido          "
print(word.upper())
print(word.lower())
print(word.strip())
print(word.isalpha)


x = "Sri Lanka's documented history spans 3,000 years, with evidence of prehistoric human settlements dating back at least 125,000 years.[12] It has a rich cultural heritage, and the first known Buddhist writings of Sri Lanka, the Pāli Canon, date back to the Fourth Buddhist council in 29 BCE.[13][14] Its geographic location and deep harbours made it of great strategic importance from the time of the ancient Silk Road through to the modern Maritime Silk Road.[15][16][17] Its location as a major trading hub made it known to both the Far East as well as to Europe from as far back as the Anuradhapura period. The country's trade in luxury goods and spices attracted traders of many nations, creating Sri Lanka's diverse population. During a period of great political crisis, the Portuguese, whose arrival in Sri Lanka was largely accidental, sought to control the island's maritime regions and its lucrative external trade. The Portuguese possessions were later taken over by the Dutch. The Dutch possessions were then taken by the British, who later extended their control over the whole island, colonising it from 1815 to 1948. A national movement for political independence arose in the early 20th century, and in 1948, Ceylon became a republic and adopted its current name in 1972. Sri Lanka's recent history has been marred by a 26-year civil war, which ended decisively when the Sri Lanka Armed Forces defeated the Liberation Tigers of Tamil Eelam in 2009.[18]Sri Lanka is a multinational state, home to diverse cultures, languages, and ethnicities. The Sinhalese form the majority of the nation's population; and the large minority of Tamils have also played an influential role in the island's history, while Moors, Burghers, Malays, Chinese, and the indigenous Vedda are also established groups.[19] It has had a long history of international engagement, as a founding member of the SAARC, and a member of the United Nations, the Commonwealth of Nations, the G77, and the Non-Aligned Movement. Sri Lanka is the sole South Asian country rated high on the Human Development Index, with the second highest per capita income in the region."
print(x.count("s"))
print(x.count("S"))

print("Rohan"+"1998") # string concatination

name = "Rohan"
age = 1998
print(name+str(age))