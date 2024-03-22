phone_number={
    'Ram':1234,
    'Shyam':5678,
    'Hari':9101,
    'Ram':1234455 # Duplicate key will be overwritten
}

# phone_number=dict({'Ram':1234,'Shyam':5678,'Hari':9101})
# print(phone_number) # different declaration of dictionary

# print(phone_number)
# phone_number["Shyam"]=2004  # Update value

# phone_number['Gita']={1234,5678,9101} # Add new key value pair and value is set

# phone_number['Sita']={'Sita_home':1234,'Sita office':5678} # Add new key value pair and value is dictionary
# print(phone_number)

# print(phone_number['Sita']['Sita_home']) # Accessing nested dictionary

# print(phone_number.get('Sita')) # Accessing value of key Sita

# del phone_number['Ram'] # does not return anything
# print(phone_number.pop('Shyam')) # Returns a deleted value
# print(phone_number)

# print(phone_number.popitem()) # delets the last item and returns value and key

# phone_number.clear()
# print(phone_number) # Clears the dictionary

# print(phone_number.keys())
# print(phone_number.values())
# print(phone_number.items()) # Returns key value pair in the form of tuples

# for i in phone_number:
#     print(i)          # Returns only keys
#     print(phone_number[i])        # Returns only values

# for i in phone_number.items():
#     print(i)      # Returns key value pair in the form of tuples

phone_number_2=phone_number.copy()
print(phone_number_2)
print(len(phone_number_2))