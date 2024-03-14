name1=input("Enter your name: ")
name2=input("Enter their name: ")

combined_string=name1+name2
lower_case_string=combined_string.lower()

t=lower_case_string.count("t")
r=lower_case_string.count("r")
u=lower_case_string.count("u")
e=lower_case_string.count("e")
# print(type(t)) #int
true=t+r+u+e

l=lower_case_string.count("l")
o=lower_case_string.count("o")
v=lower_case_string.count("v")
e=lower_case_string.count("e")
love=l+o+v+e
print(type(love))

love_score=int(str(true)+str(love))
if(love_score>80 and love_score<100):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif(love_score>=40 and love_score<=750):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")