listy = [1, 2, 3, 34, 145454, 'gh']

listy.append("this junk here")
print(listy)

listy.extend(["this too", 124])
print(listy)

listy.insert(2, 'added by insert')
print(listy)
