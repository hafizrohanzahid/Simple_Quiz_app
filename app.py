import tkinter as tk

# ------------ QUIZ DATA ------------

Quiz = {
    "What is the capital city of Pakistan": {
        "options": ["Lahore", "Islamabad", "Karachi", "Peshawar"],
        "answer": "Islamabad"
    },

    "Which planet is known as the Red Planet": {
        "options": ["Earth", "Jupiter", "Mars", "Venus"],
        "answer": "Mars"
    },

    "What is the largest continent in the world": {
        "options": ["Africa", "Europe", "Asia", "Australia"],
        "answer": "Asia"
    },

    "How many continents are there in the world": {
        "options": ["5", "6", "7", "8"],
        "answer": "7"
    },

    "Which language is mainly used for web page structure": {
        "options": ["Python", "HTML", "C++", "Java"],
        "answer": "HTML"
    },

    "Which data type is used to store True or False in Python": {
        "options": ["String", "Integer", "Boolean", "Float"],
        "answer": "Boolean"
    },

    "Which symbol is used for comments in Python": {
        "options": ["//", "#", "/*", "$"],
        "answer": "#"
    },

    "What is the output of 10 % 3 in Python": {
        "options": ["0", "1", "2", "3"],
        "answer": "1"
    },

    "Which keyword is used to define a function in Python": {
        "options": ["function", "define", "def", "fun"],
        "answer": "def"
    },

    "Which collection stores data in key-value pairs in Python": {
        "options": ["List", "Tuple", "Set", "Dictionary"],
        "answer": "Dictionary"
    }
}

# making quetsions list
questions=list(Quiz.keys())

# abhi konsa question chal raha hai
current_question=0

# user's score
score=0

# ------------ MAIN WINDOW ------------
# creating main window
window = tk.Tk()
window.title("Quiz App")
window.geometry("600x600")
window.configure(bg="#0B1220")

# ---------- WELCOME SCREEN ------------

# Quiz app heading
card = tk.Frame(
    window,
    bg="#111C2E",
    width=450,
    height=400
)

card.pack(pady=80)
card.pack_propagate(False)


heading=tk.Label(
    card,
    text="Quiz App",
    font=("Arial", 32, "bold"),
    bg="#111C2E",
    fg="#F8FAFC"
)

# showing heading to main window
heading.pack(pady=35)

# welocome mesaage
welcome=tk.Label(
    card,
    text="Test your knowledge!",
    font=("Arial",17),
    bg="#111C2E",
    fg="#94A3B8"
)

welcome.pack(pady=5)

# ------------- QUIZ SCREEN -------------

# question
question=tk.Label(
    window,
    text="",
    font=("Arial",17,"bold"),
    bg="#111827",
    fg="white",
    wraplength=500
)

# option 1
option1=tk.Button(
    window,
    text="",
    font=("Arial",14),
    width=25,
    bg="#1E293B",
    fg="#F8FAFC",
    activebackground="#2563EB",
    activeforeground="white",
    relief="flat",
    cursor="hand2"
)

# option 2
option2=tk.Button(
    window,
    text="",
    font=("Arial",14),
    width=25,
    bg="#1E293B",
    fg="#F8FAFC",
    activebackground="#2563EB",
    activeforeground="white",
    relief="flat",
    cursor="hand2"
)

# option 3
option3=tk.Button(
    window,
    text="",
    font=("Arial",14),
    width=25,
    bg="#1E293B",
    fg="#F8FAFC",
    activebackground="#2563EB",
    activeforeground="white",
    relief="flat",
    cursor="hand2"
)

# option 4
option4=tk.Button(
    window,
    text="",
    font=("Arial",14),
    width=25,
    bg="#1E293B",
    fg="#F8FAFC",
    activebackground="#2563EB",
    activeforeground="white",
    relief="flat",
    cursor="hand2"
)

# result label
result=tk.Label(
    window,
    text="",
    font=("Arial",16,"bold"),
    bg="#0B1220",
    fg="white"
)

# ------------ FINAL SCREEN ------------

# final heading
final_heading=tk.Label(
    window,
    text="",
    font=("Arial",28,"bold"),
    bg="#0B1220",
    fg="#60A5FA"
)

# final score
final_score=tk.Label(
    window,
    text="",
    font=("Arial",22),
    bg="#0B1220",
    fg="#F8FAFC"
)

# ------------ FUNCTION ------------

# function of showing quiz screen
def show_quiz():

    # hiding welcome screen
    card.pack_forget()

    # showing current question
    question_text=questions[current_question]

    # showing question on screen
    question.config(text=question_text)

    # taking current questions options
    options=Quiz[question_text]["options"]

    # setting text of buttons 
    option1.config(
        text=options[0],
        command=lambda:check_answer(options[0])
)
    option2.config(
        text=options[1],
        command=lambda:check_answer(options[1])
    )
    option3.config(
        text=options[2],
        command=lambda:check_answer(options[2])
    )
    option4.config(
        text=options[3],
        command=lambda:check_answer(options[3])
    ) 

    # showing question
    question.pack(pady=30)

    # Showing Options
    option1.pack(pady=5)
    option2.pack(pady=5)
    option3.pack(pady=5)
    option4.pack(pady=5)

# ----------- CHECKING ANSWER -----------
def check_answer(selected_answer):

    global score

    # taking current question
    question_text=questions[current_question]

    # taking correct answer
    correct_answer=Quiz[question_text]["answer"]

    # checking answer
    if selected_answer==correct_answer:
        # adding 1 in score
        score+=1

        # Correct message
        result.config(
            text="Correct Answer ✅",
            fg="#22C55E"
        )

    else:
        # wrong message
        result.config(
            text=f"Wrong Answer ❌\nCorrect Answer: {correct_answer}",
            fg="#EF4444"
        )

    # showing result
    result.pack(pady=15)

    # disabling the options
    option1.config(state="disabled")
    option2.config(state="disabled")
    option3.config(state="disabled")
    option4.config(state="disabled") 

    # showing next question button 
    next_question_button.pack(pady=10)

# function of showing next question
def next_question():

    global current_question

    # checking is there any more questions left
    if current_question<len(questions)-1:
        # going to next question
        current_question+=1

        # hiding result
        result.pack_forget()

        # hiding next question button
        next_question_button.pack_forget()
        result.config(fg="white")
        # enabling options again 
        option1.config(state="normal")
        option2.config(state="normal")
        option3.config(state="normal")
        option4.config(state="normal")

        # showing next question
        show_quiz()

    else:
        # if all questions are completed
        show_final_result()

# showing final result function
def show_final_result():

    # hiding things of quiz screen
    question.pack_forget()

    option1.pack_forget()
    option2.pack_forget()
    option3.pack_forget()
    option4.pack_forget()

    result.pack_forget()
    next_question_button.pack_forget()
    quit_button.pack_forget()

    # final result heading
    final_heading.config(
        text="Quiz Completed 🎉"
    )

    final_heading.pack(pady=80)

    # showing score
    final_score.config(
        text=f"Your Score: {score}/{len(questions)}"
    )

    final_score.pack(pady=20)

    # showing Restart buttton 
    restart_button.pack(pady=20)
    quit_button2.pack(pady=10)

# function of restarting quiz
def restart_quiz():
    global current_question
    global score

    # reseting variable
    current_question=0
    score=0

    option1.config(state="normal")
    option2.config(state="normal")
    option3.config(state="normal")
    option4.config(state="normal")

    # hiding final screen
    final_heading.pack_forget()
    final_score.pack_forget()
    restart_button.pack_forget()
    quit_button.pack_forget()

    # starting quiz again
    show_quiz()

# ============ BUTTONS ============

# exiting button
quit_button=tk.Button(
    card,
    text="QUIT",
    font=("Arial",12,"bold"),
    width=18,
    bg="#1E293B",
    fg="#CBD5E1",
    activebackground="#334155",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=window.destroy
)


# start/next button
start_button=tk.Button(
    card,
    text="START QUIZ  ➡",
    font=("Arial",15,"bold"),
    width=15,
    bg="#3B82F6",
    fg="white",
    activebackground="#2563EB",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=show_quiz
)

start_button.pack(pady=25)
quit_button.pack(pady=10)

# Next question button
next_question_button=tk.Button(
    window,
    text="NEXT QUESTION ➡️",
    font=("Arial",14,"bold"),
    width=20,
    bg="#3B82F6",
    fg="white",
    activebackground="#2563EB",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=next_question
)

# Restart button 
restart_button=tk.Button(
    window,
    text="RESTART QUIZ",
    font=("Arial",14,"bold"),
    width=18,
     bg="#2563EB",
    fg="white",
    activebackground="#1D4ED8",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=restart_quiz
)
# exiting button
quit_button2=tk.Button(
    window,
    text="QUIT",
    font=("Arial",12,"bold"),
    width=18,
    bg="#1E293B",
    fg="#CBD5E1",
    activebackground="#334155",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=window.destroy
)

# ================= START APP =================

# running app
window.mainloop()