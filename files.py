import os
#print(os.path.basename("C:\Users\Sahra\PycharmProjects\pythonProject"))
#dir_path = os.path.dirname(os.path.realpath(__salim.txt__))
#os.chdir('C:\Users\Sahra\PycharmProjects\pythonProject')

# fichier = open("salim.txt", "r")
# contenu = fichier.read()
# print(contenu)
# fichier.close()
# print()
#
# with open('salim.txt',"r") as f :
#     print(f.mode)
#     print(f.name)
#     print()
#     txt=f.readline()
# print(txt)
#os.chdir('c:/Users/Sahra/PycharmProjects/pythonProject')
# os.getcwd()
# with open('salim.txt',"r") as f :
#     txt=f.readlines()
#     for linge in txt :
#         x=linge.strip()
# print(x)
# # print(f.mode)
# # print(f.name)
# print()

def dire_bonjour_a(nom):
 """Cette fonction doit produire une exception lorsque
 nom n'est pas une chaîne de caractères ou bien si nom
 correspond à la chaîne vide."""
 # TODO

#+++++++++++++++++++++++Exercice 1 :
def Bonjour(nm):
    try:
         if nm=='' or any(chr.isdigit() for chr in nm):
             raise ValueError
         print("Bonjour", nm)
    except ValueError:
         print('Erreur rencontrée, Veuillez saisir un nom valid')

nom = input("svp, enter number votre nom? : ")
Bonjour(nom)
# #+++++++++++++++++++++++++++ 2 eme exerc++++++++++++++++
# print("\n"*2)
# mafich="chanson.txt"
# try:
#     with open ("chanson.txt") as f:
#         for l in f:
#             l=l.capitalize()
#             print(l)
# except FileNotFoundError:
#     msg= mafich + "fichier exist pas!"
#     print(msg)
# #+++++++++++++++++++++++++++3  eme exerc++++++++++++++++
# print("\n"*2)
# mafich="chanson.txt"
# #newfile="chanson1.txt"
# try:
#     with open ("chanson.txt") as f:
#         with open("newfile.txt", "a+") as g:
#             for l in f:
#                 l=l.capitalize()
#                 g.writelines(l)
# except FileNotFoundError:
#     msg= mafich + "fichier exist pas!"
#     print(msg)