import tkinter as tk

class BoardConfig:
    def __init__(self, parent):
        self.board_selected = None
        self.parent = parent

    def board_selection_gui(self, parent):
        parent.create_window()
        label = tk.Label(master=parent.mainframe, relief=parent.border_effects.get("ridge"),
                         text="Select the board to configure for:", height=10, fg="white", bg="black")
        label.pack()
        options = ["Recore A5", "Recore A6", "Recore A7"]
        board_selected = tk.StringVar(parent.mainframe)
        board_selected.set(options[0])
        board_selection = tk.OptionMenu(parent.mainframe, board_selected, *options)
        board_selection.pack()
        board_confirm_button = tk.Button(master=parent.mainframe, relief=parent.border_effects.get("groove"), text="Ok",
                                         width=5, height=5, bg="black", fg="white")
        board_confirm_button['command'] = lambda board=board_selected: \
            self.set_board(board_selected, parent)
        board_confirm_button.pack()
        parent.window.mainloop()

    def set_board(self, board, parent):
        self.board_selected = board.get()
        print("board selected:", self.board_selected)
        parent.destroy_window()
        # call the PrinterConfig settings
        parent.printer_config.create_printer_section(parent, board)

    def get_board(self):
        return self.board_selected
