"""
Programme Jimini's : manger des insectes comestibles
Salés, sucrés ou naturés, les insectes de chez Jimini's suraont vous régaler tout au long de la journée
"""
from Insecte import Insecte
from boite import Boite

# Programme principal

def afficherB(lesAssaisonnements) -> None :

    for assaissonements in lesAssaisonnements :
        print(assaissonements)

def afficher(lesInsectes) -> None:

    for insecte in lesInsectes:
        print(insecte)


def rnjMoyen(lesInsectes) -> int:
    rnjInsecte = 0
    for i in range(len(lesInsectes)):
        insecte = lesInsectes[i]
        rnjInsecte += insecte.getRnj()

    moyRnj = rnjInsecte / len(lesInsectes)
    return moyRnj


#liste des insectes

i1 = Insecte("le criquet",28)
i2 = Insecte("le grillon",25)
i3 = Insecte("le molitor",28)
lesInsectes = [i1,i2,i3]

afficher(lesInsectes)
print(rnjMoyen(lesInsectes))
lesAssaisonnements = [Boite("mangue douce", 14,5.0,i2),Boite("oignon fumé", 14,5.0,i2),Boite("paprika", 10,5.0,i1),Boite("poivre & tomates séchées", 10,5.0,i1),Boite("curry fruité", 10,5.0,i1),Boite("à la grecque", 10,5.0,i1),Boite("sésame & cumin", 18,2.0,i3),Boite("ail & fines herbes", 18,2.0,i3),Boite("soja impérial", 18,2.0,i3)]
afficherB(lesAssaisonnements)






# création des insectes
# TODO 2 : instancier 3 insectes : le criquet (rnj : 28), le grillon (rnj : 25), le molitor (rnj : 28)
# TODO 3 : ajouter les insectes à la liste d'insectes
# TODO 6 : afficher l'ensemble des insectes (nom)
# TODO 7 : rédiger une fonction rnjMoyen retournant le rnj moyen pour une liste d'insectes fournies en paramètres.
# TODO 8 : tester la fonction rnjMoyen sur la liste d'insecte
