s1 = {23, 42, 65, 57, 78, 83, 29}
s2 = {57, 83, 29, 67, 73, 43, 48}
intersection = s1.intersection(s2)
print("Intersection is ", intersection)
for item in intersection:
    set1.remove(item)

print("First Set after removing common element ", s1)
