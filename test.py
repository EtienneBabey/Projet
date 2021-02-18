import sqlite3

#dic1 = {"Quels sont les différents types de titres dans cette base de données ?": "SELECT DISTINCT types FROM title_akas;"}
#dic2 = {"Combien y a-t-il de titres dans cette base de données ?": "SELECT COUNT(primaryTitle) FROM title_basics;"}
#dic3 = {"En quelle année est sortie le film The Godfather ?": "SELECT startYear FROM title_basics WHERE primaryTitle = 'The Godfather' and titleType = 'movie';"}
#dic4 = {"En quelle année est sortie le premier film Superman ?": "SELECT MIN(startYear) FROM title_basics WHERE primaryTitle = 'Superman';"}

#for val in dic2.values():
    #print(val)

#conn = sqlite3.connect('imdb.db')
#c = conn.cursor()
#c.execute(val)
#for row in c:
    #print(row)
#conn.close()

#def chargerRequ():

f = open('requetes/requ_01.txt','r')
requete = f.read()
print(requete)
f.close()

