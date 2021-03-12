import sqlite3
import listeRequ
"""
conn = sqlite3.connect('imdb.db')
c = conn.cursor()
c.execute("select * from name_basics limit 10")
for row in c:
    print(row)
conn.close()
"""

class database:
#https://docs.python.org/3/library/sqlite3.html
    def __init__(self, base):
        self.base = ""
        
    def connexion(self):
        self.conn = sqlite3.connect(self.base)
        self.cur = self.conn.cursor()
        
    def deconnexion(self):
        self.conn.close()
        
    def fetch(self, sql):
        self.connexion()
        self.cur.execute(sql)
        result = self.cur.fetchall()
        self.deconnexion()
        return result
    
    def execute(self, sql):
        self.connexion()
        self.cur.execute(sql)
        self.deconnexion()
        
    def chargersql(self, numRequete):
    
        for i in range(1, numRequete+1):
            dic=dict()
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
            dic[question]=requete
            
        return dic
    
    def afficher_table():
        pass
    
    def listedesrequetes():
        return listeRequ.liste()
    
    def infotable():
        pass
    
    def informations_base():
        pass


