#Works successfully

# Fonction nblist() permet de lister les multiples communs à deux entiers, dans l'interval [0 : limite]
def commonMultiplesList(limit, multiple1, multiple2):
  # Déclaration de la liste (vide)
  listInt = []
  #Déclaration du nombre de référence à incrémenter à chaque tour de boucle
  currentNb = 0
  
  #boucle tourne tant que nombre de référence strictement inférieur à la limite
  while currentNb < limit:
    #Ajout du nombre de référence à la liste, si est seulement si, il est multiple commun aux deux entiers spécifiés en valeur d'entrée 
    if currentNb % multiple1 == 0 or currentNb % multiple2 == 0:
      listInt.append(currentNb)
    #incrémentation du nombre de référence
    currentNb += 1
  #La fonction est arrivée au terme de sa tâche. Retourne la liste de multiples communs. 
  return listInt

#Fonction sumListElements() addition les éléments d'une liste d'entiers
def sumListElements(intList):
  result = 0
  for i in intList:
    result += i
  
  return result


# Varibles en entrée
maxLimit = 1000
firstMultiple = 3
secondMultiple = 5

total = sumListElements(commonMultiplesList(maxLimit, firstMultiple, secondMultiple))
print(total)





  