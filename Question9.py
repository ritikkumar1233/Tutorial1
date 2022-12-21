s= {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53,
         'july': 54, 'Aug': 44, 'Sept': 54}

sl = list()

for val in s.values():
    if val not in sl:
        sl.append(val)
print(sl)
