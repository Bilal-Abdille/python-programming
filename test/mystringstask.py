#Clean up the following variable to give the clean version in lower case. Using inbuilt methods in the str class
name = " JOHn  ."
print(name.lower().strip("."))

#2nd task-Slice the below string to get you the resulting sentence:
#sentence_one = “The Dog Breed is German Shepherd” only display “Breed is German”


sentence="The Dog Breed is German Shepherd"
print(sentence[8:23])

#3rd task-sentence_two = “Defeats for the Clinton forces, this was her moment of triumph” 
# only display “Clinton forces”

sentencetwo="Defeats for the Clinton forces, this was her moment of triumph"
print(sentencetwo[16:30])

#4th task-Split the below sentence using a semicolon i.e ; And display length of the result. 
# “The lazy dog; ran so fast; it hit the wall.” 

third="The lazy dog; ran so fast; it hit the wall."
split_third=third.split(";")
length_third=len(split_third)
print("split sentence",split_third)
print("length of the result",length_third)
#print(len(third.split(";")))

#5th task-first_name="  Joh.n"  last_name="   Do,e" Clean up and display Full name i.e John Doe
first_name="joh.n"
last_name="Do,e"
clean_first_name=first_name.replace('.','').capitalize()
clean_last_name=last_name.replace(",",'').capitalize()
full_name=f'{clean_first_name} {clean_last_name}'
print("full name:",full_name)


#6th task

mylast=["E","W","C"]
result_string=''.join(mylast)
print(result_string)

