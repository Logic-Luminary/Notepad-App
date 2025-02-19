from tkinter import Menu, Text, filedialog, END, Tk
import tkinter as tk



class NotepadApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Notepad")
        
        self.text_area = tk.Text(self.root)
        self.text_area.pack(expand=True, fill='both')
        
        self.create_menu()

    def create_menu(self):
        menu_bar = Menu(self.root)
        self.root.config(menu=menu_bar)

        file_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)

    def new_file(self):
        self.text_area.delete(1.0, END)

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt",
                                                filetypes=[("Text files", "*.txt"),
                                                           ("All files", "*.*")])
        if file_path:
            with open(file_path, 'r') as file:
                self.text_area.delete(1.0, END)
                self.text_area.insert(END, file.read())

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                   filetypes=[("Text files", "*.txt"),
                                                              ("All files", "*.*")])
        if file_path:
            with open(file_path, 'w') as file:
                file.write(self.text_area.get(1.0, END))

    def run(self):
        self.root.mainloop()