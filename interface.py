import tkinter as tk
window=tk.Tk()
#window.mainloop()
#Changer le titre de la fenêtre
window.title("Salamoalikom")

#Changer le taille de la fenêtre
#window.geometry("300 * 300")
#Spécifier une taille minimum de fenêtre
window.minsize(480, 360)
## place a label on the root window
message = tk.Label(window, text="Application Salem!")
message.pack()
#Changer le logo de la fenêtre
window.iconbitmap("ramadan.ico")
#Changer la couleur de fond
window.config(background='green')
#Ajouter un texte dans la fenêtre
label_title=tk.Label(window,text="Bienvenue mois de Ramadan")
label_title.pack(side='bottom')
#Changer la police du label

label_title=tk.Label(window,text="Bienvenue mois de Ramadan",font=("Courrier",40))
label_title.pack(expand='YES') #centre
#Changer la clouleur du label
label_title=tk.Label(window,text="Bienvenue mois de Ramadan",bg="red",fg="white")
label_title.pack(side='left')
#Changer la position du label
label_title=tk.Label(window,text="Bienvenue mois de Ramadan")
label_title.pack(side='right')

#Ajouter un autre texte “Bonjour à TOUS”
print("Pratique")
label_title=tk.Label(window,text="Bonjour à TOUS",font=("Courrier",25))
label_title.pack(expand='YES') #centre


s = Spinbox(fenetre, from_=0, to=10)
s.pack()
#Afficher ecran
window.mainloop()
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# button = tk.Button(
#     text="Click me!",
#     width=25,
#     height=5,
#     bg="blue",
#     fg="yellow",
# )
# button.pack()
# button.mainloop()
#
# entry = tk.Entry(fg="yellow", bg="blue", width=50)
# entry.pack()
# entry.mainloop()
# name = entry.get()
# print(name)
#Interface graphique Tkinter python
# bouton de sortie
fenetre=tk.Tk()
# label =tk.Label(fenetre, text="Hello World")
# label.pack()
# fenetre.mainloop()
# label
label = tk.Label(fenetre, text="Texte par défaut", bg="yellow")
label.pack()


# Frames
# Les frames (cadres) sont des conteneurs qui permettent de séparer des
# éléments.
