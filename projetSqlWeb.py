#BABEY Etienne
#01/04

import sqlite3
import listeRequ



def chercherRequete(nbRequete):
    
    assert type(nbRequete) == int,'nbRequete doit être un entier'
    assert nbRequete > 0,'nbRequete doit être strictement supérieur à 0'
    
    
    d1=dict()
    
    for i in range(1, nbRequete+1):
        
        d2=dict()
        question=[]
        requete=[]
    
        numRequ = str(i)
        chercheRequ = open("requetes/requ_"+numRequ+".txt", "r")
        lignes = chercheRequ.readlines()
        
        #Parcour ligne par ligne le fichier et les récupère séparément sous forme de listes.
        for lignes in lignes:
            requete += [lignes]
        question.append(requete[0]), requete.remove(requete[0])

        #Transforme les listes question et requete en chaîne de caractere.
        question = ''.join(question)
        requete = ''.join(requete)

        #Ajoute les variables question et requete dans un dico d2 à l'interieur d'un autre dico d1, question étant la clé et requete étant la valeur.
        d2[question]=requete
        d1[i]=d2
      
    return d2

    
def listeRequete():
    return listeRequ.liste()

def executerRequ(requ,n):

    dic = chercherRequete(n)
    dic2 = dic.values() 
    requete = ''.join(dic2)
    result=[]      

    conn = sqlite3.connect('imdb.db')
    c = conn.cursor()
    c.execute(requete)
    for row in c:
        result.append(row)
    conn.close()
    
    return result



def afficher(numRequ):
    x = chercherRequete(numRequ).keys()
    x = ''.join(x)
    return x
    #print(chercherRequete(numRequ).values())
    #L1=executerRequ(chercherRequete(numRequ),numRequ)
    
    #for i in range(len(L1)):
        #print(L1[i])
    






