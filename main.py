import tkinter as tk

def main():
    window = tk.Tk()
    window.title("To Do List")
    window.geometry("300x200")

    label = tk.Label(window, text="Label")
    label.pack()

    entry = tk.Entry(window)
    entry.pack()

    window.mainloop()

main()