capitals = {}
capitals["Netherlands"] = "Amsterdam"
capitals["Ireland"] = "Dublin"
capitals["France"] = "Paris"
print(capitals)
print(list(capitals.keys()))
print(list(capitals.values()))
del(capitals["France"])
print(list(capitals.keys()))
print(capitals.get("France","Not found"))