#name="john   ."
#print(name.split())
#print(name.startswith("h"))
# print(name.strip(""))

# slice is wen we want multiple chracters 
# first part is the index whre we want to strt
# second part is the count where we want to stop


# name="james mwangi"
# print(name[2:4])

#Create a new python file stringtask.py and attempt the 3 questions below:
# Clean up the following variable to give the clean version in lower case. Using inbuilt methods in the str class
# name = “  JOHn  .“ to “john”
first_name = " JOHn  ."
print(first_name.lower().strip("."))
# Slice the below string to get you the resulting sentence:
# sentence_one = “The Dog Breed is German Shepherd” only display “Breed is German”
one= "the dog breed is german shepherd"
two = one[8:23]
print(two)
# sentence_two = “Defeats for the Clinton forces, this was her moment of triumph” only display “Clinton forces”
sentence = "Defeats for the clinton forces, this was her moment of triumph"
sentence= sentence[16:30]
print(sentence)
# Split the below sentence using a semicolon i.e ; And display length of the result. 
# “The lazy dog; ran so fast; it hit the wall.” 
# first_name="  Joh.n"  last_name="   Do,e" Clean up and display Full name i.e John Doe
# Attempt questions in the link below. Whether you get the right answer or not, still read the solution explanation.
# https://realpython.com/quizzes/python-strings/
