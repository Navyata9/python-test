student= {"Sara":90, "Lily":95, "John":80, "Jenny":85, "Mike":100}

for value in student.values():
    avg= sum(student.values())/len(student)
print("Average score:", avg)

maxscore= max(student.values())
minscore= min(student.values())
print("highest score:", maxscore)
print("lowest score:",minscore)

student_search= input("What student do you want to search up?")
print(student.get(student_search))