from Insecte import Insecte
class Boite:
    def __init__(self, assaisonnements : str, poids : int, prix : float, linsecte : Insecte ):
        self.__assaisonnements = assaisonnements
        self.__poids = poids
        self.__prix = prix
        self.__linsecte = linsecte

    def getAssaisonnements(self) -> str:
        return self.__assaisonnements

    def setAssaissonnements(self):
        self.__assaisonnements = valeur

    def getPoids(self) -> int:
        return self.__poids

    def setPoids(self, valeur : int) -> None:
        self.__poids = valeur

    def getPrix(self) -> float:
        return self.__prix

    def setPrix(self, valeur : float) -> None:
        self.__prix = valeur

    def getLinsecte(self) -> str:
        return self.__linsecte

    def setLinsecte(self, valeur : Insecte) -> None:
        self.__linsecte = valeur

    def __str__(self) -> str:
        return "Boite de" + self.__linsecte.getNom() + "(" + str(self.__poids) + "g)" + " - " + "assaisonnés " + self.__assaisonnements
