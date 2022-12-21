sl = [87, 52, 44, 53, 54, 87, 52, 53]
sl = list(set(sl))
print("unique items", sl)

t = tuple(sl)
print("tuple ", t)

print("Min: ", min(t))
print("Max: ", max(t))
