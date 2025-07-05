import os
import tkinter as tk
import tkinter.font as tkfont
from tkinter import ttk

from main import compare_modes, generate_chord
from modes import SCALES, find_compatible_scale


def main() -> None:
    min_width = 900
    min_height = 556
    app = CagedTrainer(min_width, min_height)
    app.mainloop()


class AnswerSet(ttk.Labelframe):
    """A custom ttk.Labelframe widget for displaying a set of checkable options.

    The AnswerSet widget presents a labeled frame containing a number of checkbuttons,
    each corresponding to an option provided at initialization. It manages the state
    of each option using tkinter BooleanVar instances, allowing for easy retrieval
    of selected options and programmatic deselection.

    Parameters
    ----------
        parent : ttk.Widget
                The parent widget to which this labelframe will be attached
        title : str
                The title displayed on the labelframe.
        options : list[str]
                The list of option strings to display as checkbuttons.

    Attributes
    ----------
        title : str
                The title displayed on the labelframe.
        options : list[str]
                The list of option strings to display as checkbuttons.
        vars : dict[str, tk.BooleanVar]
                Mapping of option strings to their associated BooleanVar.

    Methods
    -------
        create_widgets()
            Creates and places checkbuttons for each option.
        get_selected() -> list[str]
            Returns a list of currently selected options.
        deselect_all()
            Deselects all options.

    """

    def __init__(self, parent: ttk.Widget, title: str, options: list[str]) -> None:
        """Initialize the custom widget with a title and a list of options."""
        super().__init__(parent, text=title, labelanchor="nw")
        self.title = title
        self.options = options
        self.vars: dict[str, tk.BooleanVar] = {}
        self.checkbuttons: list[ttk.Checkbutton] = []

        self.create_widgets()

    def create_widgets(self) -> None:
        """Create and place a checkbutton widget for each option in self.options.

        For each option, a BooleanVar is created and associated with a ttk.Checkbutton.
        The checkbuttons are arranged in a single column with padding, and the
        BooleanVar for each option is stored in self.vars for later access.
        """
        for i, option in enumerate(self.options):
            var = tk.BooleanVar()
            chk = ttk.Checkbutton(self, text=option, variable=var)
            chk.grid(column=0, row=i, padx=10, sticky="w")
            self.vars[option] = var
            self.checkbuttons.append(chk)

            self.rowconfigure(i, weight=1)

        self.columnconfigure(0, weight=1)

    def focus_first_child(self, _event: tk.Event | None = None) -> None:
        """Set focus to the first checkbutton in the answer set."""
        if self.checkbuttons:
            self.checkbuttons[0].focus_set()

    def get_selected(self) -> list[str]:
        """Return a list of selected options based on the state of associated variables.

        Returns:
            A list of answers that are currently selected.

        """
        selected: list[str] = []
        for option, var in self.vars.items():
            if var.get():
                selected.append(option)
        return selected

    def deselect_all(self) -> None:
        """Deselect all items by setting each variable in self.vars to False.

        This method iterates over all variables stored in the self.vars dictionary and
        sets their value to False, effectively deselecting any associated UI elements.
        """
        for var in self.vars.values():
            var.set(False)


class CagedTrainer(tk.Tk):
    """A GUI application for practicing the CAGED system and mode harmonization.

    This class creates a window where users are presented with random chord questions
    and must select compatible modes/scales from multiple options. It provides
    interactive widgets for answering, checking results, and generating new questions.
    The interface is dynamically laid out and supports keyboard shortcuts for user
    convenience.

    Attributes
    ----------
    answer_sets : list[AnswerSet]
        List of answer set widgets for user input.
    question : tk.StringVar
        The current question displayed to the user.
    results : tk.StringVar
        The result or feedback message displayed to the user.
    chord_degrees : list[Degree]
        The degrees of the current chord (set by new_question).

    Methods
    -------
    create_widgets()
        Initializes and arranges all GUI widgets.
    reset_interface()
        Resets the interface for a new question.
    new_question(_event=None)
        Generates a new chord question.
    check_answer(_event=None)
        Checks the user's selected answers against compatible modes.

    """

    def __init__(self, min_width: int, min_height: int) -> None:
        """Initialize the main application window with specified minimum dimensions.

        Initializes window title, style, variables, event bindings, and widgets,
        then generates a new question for the user.
        """
        super().__init__()
        self.title("CAGED Trainer")
        if os.name == "nt":
            self.iconbitmap("_internal/icon.ico")

        self._init_window(min_width, min_height)
        self._init_variables()
        self._init_bindings()

        self._init_style()
        self.create_widgets()

        self.new_question()

    def _init_style(self) -> None:
        """Initialize and configure custom ttk styles and fonts for the GUI."""
        style = ttk.Style()

        default_font = tkfont.nametofont(style.lookup("TLabel", "font"))
        self.title_font = default_font.copy()
        self.title_font.configure(size=22, weight="bold")
        style.configure("Title.TLabel", font=self.title_font)
        self.subtitle_font = default_font.copy()
        self.subtitle_font.configure(size=14, weight="bold")
        style.configure("TLabelframe.Label", font=self.subtitle_font)
        self.body_font = default_font.copy()
        self.body_font.configure(size=14, weight="normal")
        style.configure("TCheckbutton.Label", font=self.body_font)
        self.results_font = default_font.copy()
        self.results_font.configure(size=16, weight="normal")
        style.configure("Results.TLabel", font=self.results_font)

    def _init_window(self, min_width: int, min_height: int) -> None:
        """Initialize the main window with specified minimum width and height."""
        self.geometry(f"{min_width}x{min_height}")
        self.minsize(min_width, min_height)
        self.configure(padx=16, pady=16)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

    def _init_variables(self) -> None:
        """Initialize instance variables for question, answer sets, and results."""
        self.question = tk.StringVar()
        self.answer_sets: list[AnswerSet] = []
        self.results = tk.StringVar()

    def _init_bindings(self) -> None:
        """Initialize key bindings for the GUI."""
        self.bind("<Return>", self.check_answer)
        self.bind("<n>", self.new_question)

    def create_widgets(self) -> None:
        """Create and configure all widgets for the application's main GUI.

        Widgets created:
            - Question label (displays the current question)
            - Multiple AnswerSet widgets (one for each scale in SCALES)
            - Button frame with "Check" and "New chord" buttons
            - Results frame to display feedback or results
        """
        content = ttk.Frame(self)
        content.grid(column=0, row=0, sticky="nsew")
        self._configure_content_grid(content)

        self._create_question_label(content)
        self._create_answer_sets(content)
        self._create_buttons(content)
        self._create_results_frame(content)

    def _configure_content_grid(self, content: ttk.Frame) -> None:
        """Configure the grid layout for the given ttk.Frame `content`."""
        content.columnconfigure(0, weight=1)
        content.rowconfigure(0, weight=2)
        for row in range(1, 3):
            content.rowconfigure(row, weight=1)
        content.rowconfigure(3, weight=1, minsize=125)

    def _create_question_label(self, parent: ttk.Frame) -> None:
        """Create and place a question label widget inside the given ttk.Frame."""
        lbl_question = ttk.Label(
            parent,
            textvariable=self.question,
            anchor="center",
            style="Title.TLabel",
        )
        lbl_question.grid(column=0, row=0)

    def _create_answer_sets(self, parent: ttk.Frame) -> None:
        """Create a set of AnswerSet widgets as children of the given parent frame.

        This method iterates over the predefined SCALES dictionary, creating an
        AnswerSet for each scale. The AnswerSets are arranged in a grid layout within
        the parent frame. Keybindings are set up to allow quick access to each AnswerSet
        using the number keys (1 through N).
        """
        frm_answers = ttk.Frame(parent)
        frm_answers.grid(column=0, row=1, sticky="nsew")

        for i, (name, scale) in enumerate(SCALES.items()):
            answer_set = AnswerSet(frm_answers, title=name, options=scale.keys())
            answer_set.grid(column=i, row=0, sticky="nsew", padx=10, pady=10)
            self.answer_sets.append(answer_set)
            self.bind_all(f"<Key-{i + 1}>", answer_set.focus_first_child)

        for i in range(len(self.answer_sets)):
            frm_answers.columnconfigure(i, weight=1, minsize=200)
        frm_answers.rowconfigure(0, weight=1)

    def _create_buttons(self, parent: ttk.Frame) -> None:
        """Create and configure the button widgets for the parent frame."""
        frm_buttons = ttk.Frame(parent)
        frm_buttons.grid(column=0, row=2, sticky="nsew")
        btn_check = ttk.Button(
            frm_buttons,
            text="Check",
            command=self.check_answer,
            default="active",
        )
        btn_new = ttk.Button(
            frm_buttons,
            text="New chord",
            command=self.new_question,
        )
        btn_check.grid(column=0, row=0)
        btn_new.grid(column=1, row=0)

        frm_buttons.columnconfigure(0, weight=1)
        frm_buttons.columnconfigure(1, weight=1)
        frm_buttons.rowconfigure(0, weight=1)

    def _create_results_frame(self, parent: ttk.Frame) -> None:
        """Create and configure the results frame within the given parent frame."""
        frm_results = ttk.Frame(parent, borderwidth=2, relief="raised")
        frm_results.grid(column=0, row=3, sticky="nsew")
        lbl_result = ttk.Label(
            frm_results,
            textvariable=self.results,
            wraplength=800,
            style="Results.TLabel",
        )
        lbl_result.grid(column=0, row=0)

        frm_results.columnconfigure(0, weight=1)
        frm_results.rowconfigure(0, weight=1)

    def reset_interface(self) -> None:
        """Reset the user interface to its initial state."""
        for answer_set in self.answer_sets:
            answer_set.deselect_all()
        self.results.set("")

    def new_question(self, _event: tk.Event | None = None) -> None:
        """Generate a new chord question."""
        self.reset_interface()

        note, chord_name, self.chord_degrees, shape = generate_chord()
        self.question.set(f"{note}{chord_name} in {shape} shape")

    def check_answer(self, _event: tk.Event | None = None) -> None:
        """Handle the answer checking process when triggered by a user event.

        Collects the user's selected answers from all answer sets, determines the set of
        compatible modes based on the current chord degrees, and generates the results
        for display.
        """
        user_modes: set[str] = set()
        for answer_set in self.answer_sets:
            for answer in answer_set.get_selected():
                user_modes.add(answer)

        compatible_modes = find_compatible_scale(self.chord_degrees)

        output = compare_modes(user_modes, compatible_modes)
        self.results.set(output)


if __name__ == "__main__":
    main()
