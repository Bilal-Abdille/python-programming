

#tasktrainees = ["John", [2, ["James","Mary"]]]

# 1. Display 2 from the list.
trainees = ["John", [2, ["James","Mary"]]]
print(trainees[1][0])


# 2. Output James  from the list.

trainees = ["John", [2, ["James","Mary"]]]
print(trainees[1][1][0])

# 3. Using a method add 56 at the end of the list.

trainees = ["John", [2, ["James","Mary"]]]
trainees.append(56)
print(trainees)

# 4. Using a method add the name Mike between James and Mary

trainees = ["John", [2, ["James","Mary"]]]
trainees[1][1].insert(1,"mike")
print(trainees)

# 5. Change the value of 2 to 8

trainees = ["John", [2, ["James","Mary"]]]
trainees[1][0]=8
print(trainees)

# 6. Remove John and Mary from the list.

trainees = ["John", [2, ["James","Mary"]]]
#remove mary

trainees[1][1].remove("Mary")
#remove john 
trainees.remove("John")
print(trainees)

# 7. Using a function, determine the length of the list

trainees = ["John", [2, ["James","Mary"]]]
print(len(trainees))


