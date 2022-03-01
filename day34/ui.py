from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz Game")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text=f"test",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )

        self.score_text = Label(
            text="Score: 0",
            fg="white",
            bg=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.score_text.grid(column=1, row=0)

        true_png = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_png, highlightthickness=0, command=self.answer_true)
        self.true_button.grid(column=0, row=2)

        false_png = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_png, highlightthickness=0, command=self.answer_false)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_text.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def answer_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def answer_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
