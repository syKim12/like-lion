lst = []

while True:
    k = input("Enter anything: ")
    if k == "q":
        print(lst)
        break
    lst.append(k)
