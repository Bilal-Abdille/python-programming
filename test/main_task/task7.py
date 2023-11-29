# Write that prompts the user to input student marks. The input should be between 0 and 100.Then output the correct grade: 
# A > 79 , B - 60 to 79, C -  59 to 49, D - 40 to 49, E - less 40
grade= int(input("Enter your marks: "))
if grade > 79:
    print("A")
elif grade <=79 and grade >60:
    print("B")
elif grade <=60 and grade >49:
    print("C")
elif grade <=49 and grade >40:
    print("D")
else:
    print("E")