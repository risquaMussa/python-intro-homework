#Warmup 3: Set Operations

languages1 = ["Python", "Java", "JavaScript", "SQL", "C++"]
languages2 = ["Python", "Java", "C#", "Ruby", "PHP"]

set1 = set(languages1)
set2 = set(languages2)

#both without duplicate
print("Union:", set1.union(set2))

#print both sets have in common
print("Intersection:", set1.intersection(set2))
#print the differnce 
print("Difference:", set1.difference(set2))