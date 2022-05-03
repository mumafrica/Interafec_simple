from tkinter import *
import math
window = Tk () 
window.title('Salim_App - Calcul Factoriel')
# mes labels
label_Nombre = Label (window, text="entrer valeur du Nombre :",bg="red")
label_Nombre.grid (row = 1,column = 1, sticky = "E", padx = 10)
label_Factoriel = Label (window, text="Le factoriel de N est :")
label_Factoriel.grid (row = 2, column = 1, sticky = "E", padx = 10)

labelValider = Label (window, text="",bg="yellow")
labelValider.grid (row = 2, column = 2, columnspan = 2,sticky ="W",padx = 10)

Input = Entry (window)
Input.grid (row = 1, column = 2)
Input.focus_set()

def valider () :

 chn = Input.get()
 fact = math.factorial(int(chn))
 labelValider.config(text = fact)
 
def effacer ():
 labelValider.config(text = "")
 #entreeDeux.delete (0, END)

 Input.delete (0, END)

 
Bot_Quitter = Button (window, text=' Quitter ',command=window.quit)
Bot_Quitter.grid (row = 5, column = 3, pady = 10)

Bot_Valider = Button (window, text=' Valider ',command=valider)
Bot_Valider.grid (row = 5, column = 1, pady = 10)

Bot_effacer = Button (window, text=' Réinitaliser ',command=effacer)

Bot_effacer.grid (row = 5, column = 2, pady = 10)
window.mainloop()
