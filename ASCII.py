from tkinter import *

root=Tk()

root.title("ASCII")
root.geometry("400x400")
root.configure(background = 'snow')

entered_word = Entry(root)
entered_word.place(relx = 0.5, rely = 0.4, anchor = CENTER)

label = Label(root, text = "ASCII number: ", bg = 'light yellow', fg = 'black')

def turnintoascii():
    label["text"] = "ASCII number: "
    iw = entered_word.get()
    
    for letter in iw :
        label["text"] += str(ord(letter)) + " "
btn = Button(root, text = 'Show ASCII number', command=turnintoascii, bg='gold', fg = 'black')
btn.place(relx = 0.5, rely = 0.5, anchor = CENTER)

label.place(relx = 0.5, rely = 0.6, anchor = CENTER)

root.mainloop()