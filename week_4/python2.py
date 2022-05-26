a = {}

a["이름"] = "김수연"
a["나이"] = "23살"
a["학번"] = "2018153019"
a["학과"] = "산업공학"
a["생일"] = "19991212"

print(a)
print(len(a))
print()

del a["이름"]
del a["나이"]
del a["학번"]
del a["학과"]
del a["생일"]

print(a)
print(len(a))
print()

a = dict(이름="김수연", 나이="23살", 학번="2018153019", 학과="산업공학과", 생일="19991212")

print(a)
print(len(a))
print()

a.clear()
print(a)
print(len(a))