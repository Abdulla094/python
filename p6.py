print("Enter the marks of p,c,m")

p = int(input("Enter the marks of p :"))
c = int(input("Enter the marks of c :"))
m = int(input("Enter the marks of m :"))

avg = p+c+m/3
print("Avg marks is: ",avg)

if avg >= 75:
    print("A grade")
elif avg >= 65:
    print("B grade")
elif avg >= 45:
    print("C grade")
elif avg >= 35:
    print("D grade")
else:
    print("Fail")
  


