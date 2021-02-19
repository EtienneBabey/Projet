import sqlite3

"""
for val in dic2.values():
    print(val)

conn = sqlite3.connect('imdb.db')
c = conn.cursor()
c.execute(val)
for row in c:
    print(row)
conn.close()
"""


def chercherRequete(nbRequete):
    
    assert type(nbRequete) == int,'nbRequete doit être un entier'
    assert nbRequete > 0,'nbRequete doit être strictement supérieur à 0'
    assert nbRequete <= 2,'nbRequete doit être inférieur ou égal à 2'
    
    d1=dict()
    
    for i in range(1, nbRequete+1):
        
        d2=dict()
        question=[]
        requete=[]
    
        numRequ = str(i)
        chercheRequ = open("requetes/requ_"+numRequ+".txt", "r")
        lignes = chercheRequ.readlines()
        
        #Parcour ligne par ligne le fichier et les récupère séparément sous forme listes.
        for lignes in lignes:
            requete += [lignes]
        question.append(requete[0]), requete.remove(requete[0])

        #Transforme les listes question et requete en chaîne de caractere.
        question = ''.join(question)
        requete = ''.join(requete)

        #Ajoute les variables question et requete dans un dico d2 à l'interieur d'un autre dico d1, question étant la clé et requete étant la valeur.
        d2[question]=requete
        d1[i]=d2
        
    return d1
        
        
print(chercherRequete(2))  







