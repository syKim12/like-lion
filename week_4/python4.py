a = {}

while True:
    fruit_type = input("Enter a fruit type (q to quit): ")
    if fruit_type == "q":
        print(a)
        break
    weight = input("Enter the weight in kg: ")
    a[fruit_type] = weight