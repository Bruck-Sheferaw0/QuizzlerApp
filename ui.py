THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain


class QuizUI:

    def __init__(self, quizbrain: QuizBrain):
        self.quiz = quizbrain
        self.score = 0

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(row=2, column=2, columnspan=2, pady=50,padx=20)


        # Add text to the canvas
        self.text = Label(self.window, text=f"Score: {self.score}/15", font=("Arial", 15, "italic"), bg=THEME_COLOR,fg="white")
        self.text.grid(row=1, column=3, columnspan=2,pady=20)

        # main text
        self.questiontext = self.canvas.create_text(
            150, 125,  # Position in the canvas
            text="Sample",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR,
            width=260,  # Wrap text to fit within the canvas
            anchor="center"  # Center the text in the canvas
        )



        self.falseimage = PhotoImage(file="images/false.png")  # Replace with your image file path
        self.trueimage = PhotoImage(file="images/true.png")

        self.image_label1 = Button(image=self.falseimage,highlightthickness=0,command=self.falsepressed)
        self.image_label1.grid(row=3, column=3, columnspan=2, pady=20)

        self.image_label = Button(image=self.trueimage,highlightthickness=0,command=self.truepressed)
        self.image_label.grid(row=3, column=1, columnspan=2, pady=20)
        self.getnextquestion()
        self.window.mainloop()

    def getnextquestion(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.canvas.itemconfig(self.questiontext, text=self.quiz.next_question())
        else:
            self.canvas.itemconfig(self.questiontext,text="FINISHED")
            self.image_label1.config(state='disabled')
            self.image_label.config(state='disabled')

    def truepressed(self):
        self.givefeedback(self.quiz.check_answer("True"))
    def falsepressed(self):
        self.givefeedback(self.quiz.check_answer("False"))

    def givefeedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg='green')
            self.score += 1
            self.text.config(text=f"Score: {self.score}/15")
        else:
            self.canvas.config(bg='red')
        self.window.after(500,self.getnextquestion)


