import tkinter as tk
from tkinter import ttk


def main() -> None:
    app = CagedTrainerGUI()
    app.mainloop()


class CagedTrainerGUI(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("CAGED Trainer")
        self.geometry("800x450")
        self.configure(padx=16, pady=16)
        self.create_widgets()
        self.new_question()

    def create_widgets(self) -> None:
        # Question
        self.question_var = tk.StringVar(value="Question will appear here")
        question_frame = ttk.Frame(self, padding=10)
        question_frame.grid(row=1, column=0, columnspan=2, sticky="ew")
        question_label = ttk.Label(
            question_frame,
            textvariable=self.question_var,
            font=("Arial", 16),
        )
        question_label.pack(fill="x")

        # Answer set 1
        self.answer_vars1 = [tk.BooleanVar() for _ in range(5)]
        answer_frame1 = ttk.LabelFrame(self, text="Answer Set 1", padding=10)
        answer_frame1.grid(row=2, column=0, columnspan=2, sticky="ew", pady=5)
        for i, var in enumerate(self.answer_vars1):
            cb = ttk.Checkbutton(answer_frame1, text=f"Option {i + 1}", variable=var)
            cb.pack(side="left", padx=5)

        # Answer set 2
        self.answer_vars2 = [tk.BooleanVar() for _ in range(5)]
        answer_frame2 = ttk.LabelFrame(self, text="Answer Set 2", padding=10)
        answer_frame2.grid(row=3, column=0, columnspan=2, sticky="ew", pady=5)
        for i, var in enumerate(self.answer_vars2):
            cb = ttk.Checkbutton(answer_frame2, text=f"Option {i + 1}", variable=var)
            cb.pack(side="left", padx=10)

        # Buttons
        btn_new = ttk.Button(self, text="New Question", command=self.new_question)
        btn_new.grid(row=4, column=0, sticky="ew", pady=10, padx=(0, 5))
        btn_check = ttk.Button(self, text="Check Answers", command=self.check_answer)
        btn_check.grid(row=4, column=1, sticky="ew", pady=10, padx=(5, 0))

        # Results
        self.result_var = tk.StringVar(value="Results")
        result_frame = ttk.Frame(self, padding=10)
        result_frame.grid(row=5, column=0, columnspan=2, sticky="nsew")
        result_label = ttk.Label(
            result_frame,
            textvariable=self.result_var,
            font=("Arial", 16),
        )
        result_label.pack(fill="both")

        # Make the result area expand
        self.grid_rowconfigure(5, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

    def new_question(self) -> None:
        pass

    def check_answer(self) -> None:
        pass


if __name__ == "__main__":
    main()
