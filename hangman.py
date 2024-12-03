import random
movies = ['OOPENHEIMER', 'BARBIE','IRON MAN','THE AVENGERS','THE MATRIX','GLADIATOR','TENET','INCEPTION','INTERSTELLAR']
x = len(movies)
y = random.randint(0,x)
k = movies[y]
question = list(k)
length_of_movie = len(k)
chances_left = 8
final_answer = question
print("\nNumber of letters:",length_of_movie)
print()
for i in range(length_of_movie):
    if question[i] == ' ':
        print(" ",end='')
    else:
        print("_",end=' ')
        final_answer[i] = "_"
print("\n")
correct = 0
while chances_left > 0 and correct == 0:
    print("\nChances left:",chances_left)
    print("\nChoose how to enter your answer: \n  A)As whole(Single Attempt)\n  B)Letter by letter")
    choice = input("\nEnter your choice:")
    if choice == 'A' or choice == 'a':
        answer = input("\nEnter your answer:")
        if (answer == k.upper())or(answer == k.lower()):
            correct = 1
        else:
            print("\nWrong Answer")
            print("\nCorrect Answer:",k)
            break
    elif choice == 'b' or choice == 'B':
        letter = input("\nEnter your choice of letter:")
        if letter.upper() not in k:
            print("\nWrong Choice")
            chances_left -= 1
        else:
            print("Right Choice")
        letter = letter.upper()
        for i in range (length_of_movie):
            if k[i] ==  letter:
                final_answer[i] = letter
        for i in range(length_of_movie):
            if str(final_answer[i]) == " ":
                print(" ",end='')
            else:
                print(final_answer[i],end=' ')
        if str(final_answer) == k:
            correct = 1
    else:
        print("Invalid Input")
    print()
if(correct == 1):
    print("\nCorrect Answer")
if(chances_left == 0 and correct == 0):
    print("\nChances are Over")
print("\n")
