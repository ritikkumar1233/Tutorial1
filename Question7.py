s1 = {57, 83, 29}
s2 = {57, 83, 29, 67, 73, 43, 48}
print("First set is subset of second set -", s1.issubset(s2))
print("Second set is subset of First set - ", s2.issubset(s1))
print("First set is Super set of second set - ", s1.issuperset(s2))
print("Second set is Super set of First set - ", s2.issuperset(s1))
if s1.issubset(s2):
    s1.clear()
elif s2.issubset(s1):
    s2.clear()
print("First Set ", s1)
print("Second Set ",s2)
