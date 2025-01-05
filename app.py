from tkinter import *


# Driver code
if __name__ == "__main__":
    root = Tk()
    
    root.title("To-Do App")
    root.geometry("500x600")
    root.configure(background="lightgreen")
    
    heading = Label(root, text="Form", bg="light green")
    heading.grid(row=0, column=1)
    root.mainloop()