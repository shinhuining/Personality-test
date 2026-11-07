from tkinter import *

window= Tk()
window.geometry("920x400")
window.title("Personality Test")

num=0
score=0
questions=[
     ["How do you prefer spending your weekends?",
"Going out, meeting friends.",
 "Staying home.",
 "A mixture of both sometimes."],

["During a group conversation, you usually:",
 "Actively participate.",
 "Listen more than you speak.",
 "Contribute only when something interests you."],

 ["After a long, socially exhausting day, you prefer to:",
 "Meet more people.",
 "Spend some quiet time alone.",
 "Relax with a few close friends."],

 ["When meeting someone for the first time, you tend to:",
 "initiate conversation.",
 "Wait for them to approach you.",
 "Respond warmly but rarely initiate."],

["How do you feel about public speaking?",
"I enjoy being in the spotlight.",
"I prefer avoiding attention.",
 "I'm comfortable when I know what I'm talking about."],

 ["When something exciting happens, your first instinct is to:",
 "Tell everyone immediately.",
 "Keep it to yourself.",
 "Share it with a few close friend."],

 ["Which social setting do you prefer?",
 "Large gatherings with lots of people.",
 "Quiet environments.",
 "Small gatherings with people I know well."],

 ["How do you react when plans with friends get cancelled?",
 "Feel disappointed.",
 "Feel relieved to have free time.",
 "Don't mind either way, depends on mood."],

 ["How easily do you express your emotions?",
 "Quite openly.",
 "I rarely share my feelings.",
 "It depends on the person and situation."],

 ["What happens when you spend too much time alone?",
 "I start feeling bored.",
 "I feel perfectly comfortable.",
 "I enjoy it initially but eventually miss company."],

 ["How would your friends describe you?",
 "Outgoing, talkative and energetic.",
 "Reserved, thoughtful and independent.",
 "Friendly, adaptable and somewhere in between."]
]
label=Label(window, text=questions[num][0], fg="white", bg="black")
label.pack(pady=20)
def next(choice):
    global num, score
    if choice == 1:
        score += 5
    elif choice == 2:
        score += 2.5
    elif choice == 3:
        score += 0
    num+=1
    label.config(text=questions[num][0])
    button1.config(text=questions[num][1])
    button2.config(text=questions[num][2])
    button3.config(text=questions[num][3])

    if num == len(questions)-1:
        personality=["You are an extrovert! You thrive in social situations.", "You are an introvert! You prefer solitude and find energy in quiet environments.", "You are an ambivert! You have a balance of extrovert and introvert traits."]
        pc=(score/(len(questions)*5))*100
        if pc >= 60:
            result = personality[0]
        elif pc >= 40:
            result = personality[1]
        else:
            result = personality[2]

        label1=Label(window, text=result, fg="white", bg="black")
        label1.pack(pady=20)
        label.config(text="Thank you for completing the test!")
        button1.pack_forget()
        button2.pack_forget()
        button3.pack_forget()

button1=Button(window, text=questions[0][1], command=lambda: next(1))
button1.pack(pady=10)
button2=Button(window, text=questions[0][2], command=lambda: next(2))
button2.pack(pady=10)
button3=Button(window, text=questions[0][3], command=lambda: next(3))
button3.pack(pady=10)

window.mainloop()