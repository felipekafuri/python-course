# why sets are useful

local = {"Rolf"}
abroad = {"Bob", "Jen"}

total_friends = local.union(abroad)

print(total_friends)



art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}

both = art.intersection(science)

print(both)