friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

local_friends = friends.difference(abroad)

print(local_friends)

#alternatively...

local2 = {"Rolf"}
abroad2 = {"Bob",  "Anne"}

friends2 = local2.union(abroad2)

print(friends2)

#New ex

art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}

both = art.intersection(science)
print(both)