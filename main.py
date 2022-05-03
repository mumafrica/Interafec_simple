# he try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The else block lets you execute code when there is no error.
# The finally block lets you execute code, regardless of the result of the try- and except blocks.
# try:
#   print(uu)
# except:
#   print("An exception occurred")
#
# #++++++++++++++++++++++++++++++++++++++++++++++++++++
# nombre = input("Entrez un nombre : ")
# try:
#  nombre = int(nombre)
# except ValueError:
#     print("Désolé la valeur saisie n'est pas un nombre.")
# #++++++++++++++++++++++++++ Traiter une exception ++++++++++++++++++++++++++
#
# try:
#  numerateur = int(input("Entrez un numérateur : "))
#  denominateur = int(input("Entrez un dénominateur : "))
#  resultat = numerateur / denominateur
#  print("Le resultat de la division est", resultat)
# except ValueError:
#  print("Désolé, les valeurs saisies ne sont pas des nombres.")
# except ZeroDivisionError:
#  print("Désolé, la division par zéro n'est pas permise.")
#
# # #+++++++++++++++++++  Traiter exceptions de types différents+++++++++++++++++++++++++++++++++
# try:
#  numerateur = int(input("Entrez un numérateur : "))
#  denominateur = int(input("Entrez un dénominateur : "))
#  resultat = numerateur / denominateur
#  print("Le resultat de la division est", resultat)
# except (ValueError, ZeroDivisionError):
#  print("Désolé, quelque chose ne s'est pas bien passé.")

 # #+++++++++++++++++++  Récupérer le message d’une exception +++++++++++++++++++++++++++++++++
# nombre = input("Entrez nombre : ")
# try:
#  nombre = int(nombre)
# except ValueError as e:
#  print(e)
#++++++++++++++++++  Clause else  +++++++++++++++++++++++++++++++++

# Le bloc else est exécuté uniquement si le bloc try se termine normalement,
# c’est-à-dire sans qu’une exception ne survienne.
#
# try:
#  numerateur = int(input("Entrez un numérateur : "))
#  denominateur = int(input("Entrez un dénominateur : "))
#  resultat = numerateur / denominateur
# except (ValueError, ZeroDivisionError):
#  print("Désolé, quelque chose ne s'est pas bien passé.")
# else:
#  print("Le resultat de la division est", resultat)

 # ++++++++++++++++++  Post-traitement  +++++++++++++++++++++++++++++++++
 # Un bloc finally est systématique appelé même si le bloc
 # try est interrompu par une instruction return.

try:
  numerateur = int(input("Entrez un numérateur : "))
  denominateur = int(input("Entrez un dénominateur : "))
  resultat = numerateur / denominateur
  print("Le resultat de la division est", resultat)
except (ValueError, ZeroDivisionError):
  print("Désolé, quelque chose ne s'est pas bien passé.")
finally:
  print("afficher ceci quel que soit le résultat")