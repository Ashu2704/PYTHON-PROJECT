print("QUIZ ON CITIES OF INDIA")
Name = input("Enter your name:")
a1 = input("1. How many states and union territories are present in India currently? \n(a) 28 and 6 respectively \n(b) 29 and 7 respectively \n(c) 28 and 9 respectively \n")
a2 = input("2. Which Indian city is a capital of two states? \n(a) Hyderabad \n(b) Mumbai \n(c) Chandigarh \n")
a3 = input("3. Which is the smallest state in India in terms of area? \n(a) Tamilnadu \n(b) Goa \n(c) Kerala \n")
a4 = input("4. Which of the following is not a metropolitan city of India \n(a) Trivandrum \n(b) Mumbai \n(c) Chennai \n")
a5 = input("5. In which town of Nagaland was the world war 2 fought? \n(a) kohima \n(b) Dimapur \n(c) Phek \n") 
given_answer = [a1,a2,a3,a4,a5]
correct_answer= {a1:"c", a2:"c", a3:"b", a4:"a", a5:"a"}
score=0
if given_answer[0] == correct_answer[a1]:
    score += 1
if given_answer[1] == correct_answer[a2]:
    score += 1
if given_answer[2] == correct_answer[a3]:
    score += 1
if given_answer[3] == correct_answer[a4]:
    score += 1
if given_answer[4] == correct_answer[a5]:
    score += 1
print (Name + " has scored",score)
