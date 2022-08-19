# Dictionary is nothing but a key value pairs.

d = {} #dictionary
print(type(d))

d = () #tuple
print(type(d))

d = [] #list
print(type(d))

d1 = {"shahid":"Developer", "Company":"Freelancer"} #syntax dict = {"key":"value" ,"key":"value" }
print(d1["shahid"])
print(d1["Company"])

#Dictionary inside the dictionary
d2 = {"shahid":"Developer", "Company":"Freelancer", "Qualification": {"BscInCA":"XavierRanchi", "MCA":"SVSU"}}
print("\n dictionary inside the dictionary")
print(d2)
print(d2["Qualification"])
print(d2["Qualification"]["BscInCA"])

#add key and value to dictionary

d2["imran"] = "Developer" # dict[key] = value
print(d2)
d2[6] = "Zeeshan" #key can be number or string
print(d2)

#to delete
del d2[6]
print(d2)
del d2["imran"]
print(d2)

#copy function

d3 = d2.copy()
print(d3)

d4=d3 #This isn't copying, this is pointing to original dictionary and if you delete something will
      #be deleted from original dict#)

del d4["shahid"]
print(d4) #deleted from d4 and
print(d3) #deleted from d3 also

print(d3.get("Company"))
d3.update({"Shahid":"Developer"})
print(d3)
print(d2.keys())
print(d2.items()) #it prints key value pairs.