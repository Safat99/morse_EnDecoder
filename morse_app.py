from morse_endecoder import encode, decode
import tkinter as tk

gui = tk.Tk()
gui.title('Morse Code EnDeCoder APP')
gui.geometry('640x480')
gui.resizable(None,None)

headline = tk.Label(gui,text='Enter normal text for encoding: ')
headline.grid(row=0,column=2,padx=10,pady=10)

# blank =tk.Label(gui,text="")
# blank.grid(row=1,column=0)

entry = tk.Entry(gui,width=30)
entry.grid(row=1, column=2, padx=10, pady=10)

lbl1 = tk.Label(gui,text="")
lbl1.grid(row=2, column=2, pady=10, padx=10)

def btn_1():
    encoded = encode(entry.get())
    lbl1.configure(text=encoded)

btn = tk.Button(gui,text="Encode", fg="red", bg="white", command=btn_1)
btn.grid(row=1,column=3)

headline = tk.Label(gui,text='Decode the Morse Code: ')
headline.grid(row=3,column=2,padx=10,pady=10)


entry2 = tk.Entry(gui,width=30)
entry2.grid(row=4, column=2, padx=10, pady=10)

lbl2 = tk.Label(gui,text="")
lbl2.grid(row=5, column=2, pady=10, padx=10)

def btn_2():
    decoded = decode(entry2.get())
    lbl2.configure(text=decoded)

btn2 = tk.Button(gui,text="DECODE", fg="white", bg="black", command=btn_2)
btn2.grid(row=4,column=3)



gui.mainloop()