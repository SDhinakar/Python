numbers=[10,0,-1,7,9,4,18]
names=["jem","jane","jake","jill"]
mix_list=[10,0,-1,7,"jem",10.89]

print(type(numbers))

print(mix_list)
print(mix_list[0])
print(len(mix_list))

print(mix_list[-2]) #negative index starts from the end of the list
print(mix_list[1:3]) #slicing (index : index-1 )
print(mix_list[0:6:2]) #slicing with step

numbers.sort()
print(numbers) # sort should be done before printing
print(min(numbers)) #min and max can be used on list of same type
print(max(numbers))

names.sort()
print(names) #sort can't be done on mixed list

numbers.append(20) #add at the end

numbers.insert(2,30) #insert at index 2

numbers.extend([45,58,787,45]) #insert multiple elements at the end
print(numbers)

numbers[1:4]={45,46,47} #replace multiple elements
print(numbers)

numbers.remove(45) #remove first occurance of 45 and it wont return anything
print(numbers)

print(numbers.pop(5)) #remove last element and return it
print(numbers)

print(numbers.index(45)) #return index of first occurance of 45

print(numbers.count(45)) #return count of 45

numbers.reverse() #reverse the list

print(numbers)