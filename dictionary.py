names = {1:"abdullah",2:"John",3:"george",4:"ringo"}

print(names)

names[1] = "Talha"
names[5] = "Ansari"

print(names)

del names[5]
print(names)

for k,v in names.items():
    print(k,v)
