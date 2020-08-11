l = ["Bob", "Rolf", "Anne"]
t = ("Bob", "Rolf", "Anne")
s = {"Bob", "Rolf", "Anne"}

print(l[0])
print(t[0])
#print(s[0])won't work

l[0] = "Smith"
[print(l)]
#t[0] = "Smith" Won't work

l.append("Smith")
print(l)
#t.append("Smith") Won't work

l.remove("Rolf")
print(l)

s.add("Smith")
print(s)
s.add("Smith")
print(s) #sets can't contain any duplicates