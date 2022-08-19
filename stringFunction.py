myString = "Shahid knows many programming languages"
myStr = "shahid"
print(len(myString))
print(type(myString))
print(myString.isalnum())
print(myStr.isalnum())
print(myString.isalpha())
print(myStr.isalpha())

print(myString.endswith("languages"))
print(myString.endswith("mylanguages"))

print(myString.find("many"))
print(myString.count("a"))

print(myString.lower())
print(myString.islower())
myString2 = myString.lower()
print(myString2.islower())

print(myString.upper())

print(myStr.capitalize())

print(myStr.replace("shahid", "Shahid Raza"))

