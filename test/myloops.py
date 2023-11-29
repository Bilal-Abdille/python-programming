n = "10"
for i in n:
    print(i)

y = range(0, 10)
for i in y:
    print(i)

nov_intake = ["antony","tosh","cornellius","herman","ropy","bilal","ian","abigal"]
for i in nov_intake:
    print(i)

# looping through a control statement
for i in range(10):
    if i =="ropy":
        break
    print(i)


for i in range(20):
    if i==5:
        continue
    print(i)

# looping through dictionaries
person = {"name": "Bilal","age": 20, "location":"Nairobi","email":"bilalmaalim57@gmail.com"}

for key,value in person.items():
    print(key,value)