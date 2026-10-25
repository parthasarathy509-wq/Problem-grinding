a = {"lahfla": 1, "afad": 3, "love": "lover"}
l = 1
b = next(i for i, value in a.items() if value == l)
print(b)
m = next((damm for damm, value in a.items() if value == "lover"), None)
print(m)
