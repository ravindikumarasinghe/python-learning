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

# get value from a string
name = "Ravindi"
print(name[1]) #print 1st index value {R=0, a=1, v=2,...d=5,i=6 as their indexes, [0] is the index of string "R"}
print(name[-1]) # print the last letter {R=-7, a=-6, v=-3,...d=-2,i=-1}
print(name[:])  # print from starting point to end
print(name[1:3])    # print string values form 1 to 3rd index as "oh", here 3rd index wont print but starting index will print

# also this can print by naming it as a variable
result = name[4]
print(result)

print(name[::])
print(name[2:])
print(name[2::2])