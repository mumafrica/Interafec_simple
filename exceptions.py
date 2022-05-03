https://docs.python.org/3/tutorial/errors.html
from statistics import mean
# try:
#     msg=int(input("enter number"))
#     print(1/msg)
# except:
#     print('Erreur rencontrée')
# finally:
#     print("fin de programme")
# print()
# #---------------------------------------Exercice 2: Cibler l’exception--------------------------
# try:
#     print(1/msg)
# except ZeroDivisionError :
#     print("Désolé,Zéro n’admet pas d’inverse")
# except:
#     print('Erreur rencontrée')
# else :
#     print('tres bien ,bloc try est ok')
# print()
# print("Exercices 2", " *"*45)
#
# while True:
#     try:
#         x=int(input("Entrer un entier :"))
#         print("L’inverse de", x ,"est:", "{:.2f}".format(1/x))
#         break
#     except ZeroDivisionError:
#         print("Zero n'admet pas d'inverse")
#
#     except :
#         print("Erreur rencontree")

# #---------------------------------------Exercice 3: La clause else-------------------------------
#while True :
    # try:
    #     msg = int(input("enter number"))
    #     print(1/msg)
    #
    # except ZeroDivisionError :
    #     print("Désolé,Zéro n’admet pas d’inverse")
    # except:
    #     print('Erreur rencontrée, Veuillez saisir un autre')
    #
    # else :
    #     print('tres bien')
    #
    # finally:
    #     print('FIIIIIIIIIIIN')
#+++++++++++++++++++++++++++++++++Exercice 4 : La clause raise

# i=0
# try:
#     for i in range(5):
#         msg = int(input("entre la note : ", i))
#         if 0<= x <=20:
#             print(i)
#
#     except:
#         raise ValueError("findEven called with bad arguments")

try:
    Tabl = []
    Note = 0

    for i in range(5) :
        Note = int(input('Entrez la note : '))
        if  Note < 0 or Note >= 20:
            raise ValueError
            Tabl.append(Note)
    Moyenne = sum(Tabl)/len(Tabl)
    print(Moyenne)

except :
    print ('Erreur dans la liste de nombres')

#Solution Ex 5
try :
 a = int(input("tapez un nombre pour afficher son inverse"))
 i = 1/a
except (ZeroDivisionError):
 print("Zero n'admet pas d'inverse")
except :
 print("Erreur rencontree")
else :
 print("l'inverse de " , a , "est : " ,'{0:3.2f}'.format(i))
finally:
 print("Au Revoir")

#Solution Ex 4
i = 1
somme = 0
while True and i <= 5 :
 try:
  n = float(input("tapez la note numero {0}  :".format(i)  ))
  if n < 0 or n > 20 :
   raise ValueError
  else:
   somme += n
   i += 1
 except ValueError:
  print("note invalide ")
print("la moyenne  est " , somme/5)
#+++++++++++++++++++++++++++++++++++++++++ examples

>>> try:
...     raise KeyboardInterrupt
... finally:
...     print('Goodbye, world!')
...
Goodbye, world!
KeyboardInterrupt
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
#++++++++++++++++++++++++++++++++++++++++
try:
...     a = int(input("Enter a positive integer: "))
...     if a <= 0:
...         raise ValueError("That is not a positive number!")
... except ValueError as ve:
...     print(ve)
...
Enter a positive integer: -2
#++++++++++++++++++++++++++++++++++++++++++++
try:
    # get input net sales
    print('Enter the net sales for')

    previous = float(input('- Prior period:'))
    current = float(input('- Current period:'))

    # calculate the change in percentage
    change = (current - previous) * 100 / previous

    # show the result
    if change > 0:
        result = f'Sales increase {abs(change)}%'
    else:
        result = f'Sales decrease {abs(change)}%'

    print(result)
except ValueError:
    print('Error! Please enter a number for net sales.')
except ZeroDivisionError:
    print('Error! The prior net sales cannot be zero.')
except Exception as error:
    print(error)
#++++++++++++++++++++++++++++++++++++++


