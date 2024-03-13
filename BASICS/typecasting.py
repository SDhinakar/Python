length=len("Dhinakar shanmugam")
print(type(length)) # Integer can't be concatenated with string
print(type(str(length))) #So typecasting is required
print("Your name has "+ str(length) +" characters")

# print(len(12344))     TypeError: object of type 'int' has no len()

print(int("1234"))
print(type(int("1234")))

print(str(1234))
print(type(str(1234)))

print(float(1234))
print(type(float(1234)))

print(bool(1234))
print(type(bool(1234)))

print(int("123")+int("456"))
print(int("123")+float("456"))
