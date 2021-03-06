#listeRequ
def liste():
    
    d1 = dict()
    
    for i in range(1, 3):
        
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
        
        d2[question]=requete
        d1[i]=d2
    
    for v in d1.values():
        print(v)