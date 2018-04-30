import tkinter as tk

#create function for the bind , event = event handler 
def halo(event):
    print("Halo is downloading")

def wake(event):
    print("Wake up is downloading")

window = tk.Tk()
window.geometry("600x600")

#create and name the lables
alabel = tk.Label(text="Halo 1gb")
alabel.grid(column=0, row=0)

blabel = tk.Label(text="wake up 1gb")
blabel.grid(column=4, row=0)



#create the buttons
button = tk.Button(text="download")
button.grid(column=0)

button2 = tk.Button(text="download")
button2.grid(column = 4 , row =1)  
                    
button.bind("<Button-1>", halo)
button2.bind("<Button-1>", wake)


window.mainloop()
