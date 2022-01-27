class Insecte:
    """Classe Insecte
    Permet de créer une instance d'Insecte
    Attributs d'instance
    --------------------
    nom : str
        nom de l'animal
    rnj : int
        repère nutritionnel journalier (rnj) correspondant à la teneur en énergie et en macro-nutriments.
    """

    def __init__(self, unNom: str, valRnj : int):
        """Constructeur de la classe Insecte
        """
        self.__nom = unNom
        self.__valRnj = valRnj
        #TODO 1: implémenter le constructeur de la classe

    def getNom(self) -> str:
        """Getter sur l'attribut nom
        :return: str, le nom de l'insecte
        """
        return self.__nom

    def setNom(self, valeur : str) -> None :
        """Setter sur l'attribut nom
        :param valeur : valeur pour le nom
        """
        self.__nom = valeur
        
    
    def setRnj(self, valeur : str):
        self.__valRnj = valeur

    def getRnj(self) -> int:
        return self.__valRnj

    def __str__(self) -> str:
        result = self.__nom +"(rnj :" + str(self.__valRnj) + ")"
        return result

    #TODO 4 : implémenter les méthodes get et set pour l'attribut rnj

    #TODO 5: définir la méthode permettant de générer l'affichage d'une instance d'Insecte au format str
