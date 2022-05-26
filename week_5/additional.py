#1
from datetime import date

my_mon = int(input("You : Enter month born (1-12): "))
my_day = int(input("You : Enter day born (1-31: "))
my_year = int(input("You : Enter year born (4-digit) : "))
my_date = date(my_year, my_mon, my_day)

today_month = int(input("Enter month (1-12): "))
today_day = int(input("Enter day (1-31: "))
today_year = int(input("Enter year (4-digit) : "))
today_date = date(today_year, today_month, today_day)

delta = today_date - my_date
print("Number of days you lived:",delta.days)

#2
word = input('Enter a sentence: ')
x= word.lower()
vowel = ['a','e','i','o','u']

n=0
for i in vowel:
    n += x.count(i)
       
if(n==1):
    print('Your sentence contains', n, 'vowel')
else:
    print('Your sentence contains', n, 'vowels')


#3
name_list = []

while True:
    name = input("Enter a name (q to quit): ")
    if name == "q":
        break
    else:
        if " " in name:
            split_name = name.split()
            for i in split_name:
                name_list.append(i)
        else:
            name_list.append(name)

num_a = 0
for i in name_list:
    num_a += i.count("a")

print("Number of names and letter 'a': ", len(name_list), ",", num_a)

#3
names = []
num_letter = 0

while True:
    name = input('Enter a name (q to quit): ').lower().split()
    if 'q' in name:
        break
    names += name

num_names = len(names)

for name in names:
    num_letter += str(name).count('a')

print('Number of names and letter ''a'':',num_names,num_letter)


#4
num_list = []
while True:
    num = int(input("Enter a number: "))
    if num <= 0:
        break
    else:
        num_list.append(num)

print("The largest number entered was", float(max(num_list)))
result = float(max(num_list))
print(f"The largest number entered was {result: .2f}")