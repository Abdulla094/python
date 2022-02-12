# tuple is immutable

t = (1,2,3,4,5)
print(t)

print(t[0])
print(t[1])
print(t[2:])

u = (100,200) + t[2:]

print(u)
v = (t,u)
print(v)

names = ["Abdullah","Talha","Savez"]

z = (t,names)
print(z)

z[1][1] = "Abdul"

print(z)

