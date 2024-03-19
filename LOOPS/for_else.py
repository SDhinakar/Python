tuple1 = (2,56,7,55,10,63)
for i in tuple1:
    print(i)
    if(i%6==0):
        break
    else:
        print("Not divisible by 6")
else:
    print("The loop has ended completely.") # This will not be printed as the loop has ended before the completion of the loop

print("Out of for/else loop.")