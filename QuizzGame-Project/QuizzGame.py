Title="Hello User Welcome to Quizz Game"
print(Title.center(50,'-'))
print("")

question_Array=["Brain of the computer?","Full form of CPU?","Full form of RAM?","Full form of ROM?","Device used to type letters?"]

answer_array=["CPU","Central Processing Unit","Random Access Memory","Read Only Memory","Keyboard"]
score=0
mark_fixing=round(100/int(len(question_Array)))

print(mark_fixing)
for index,question in enumerate(question_Array):
    print(f"{index+1}: {question}")
    get_ans=input("Ans: ").lower()
    if get_ans == answer_array[index].lower():
        print("Correct ANS")
        score+=mark_fixing
    else:
        print("Wrong ANS")

total_mark=f"{round((score/100)*100)}%"
print("")
print(F"Your Mark is:{total_mark}")
print("Thank You")

    





