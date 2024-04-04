class Bloc:
    def __init__(self, coord_haut_gauche, coord_bas_droite, color):
        """ Fonction pour initialiser un bloc.

        Précondition : 
        Exemple(s) :
        $$$ bloc1 = Bloc((0, 0), (50, 50), (255, 0, 0))
        $$$ bloc = Bloc((50, 0), (100, 50), (0, 255, 0))
        $$$ bloc
        Bloc((50, 0), (100, 50), (0, 255, 0))

        """
        
        
        self.coord_haut_gauche = coord_haut_gauche
        self.coord_bas_droite = coord_bas_droite
        self.color = color
        self.uniforme = False
        self.sous_bloc = []

    def __add__(self, sous_bloc):
        """ Fonction pour ajouter un sous-bloc à un bloc.

        Précondition : 
        Exemple(s) :

        """
        
        self.sous_bloc.append(sous_bloc)

    def est_uniforme(self):
        """ Fonction pour vérifier si un bloc est uniforme.

        Précondition : 
        Exemple(s) :
        $$$ Bloc((0, 0), (50, 50), (255, 0, 0)).est_uniforme()
        True

        """
        
        return self.color is not None
    
    def __repr__(self):
        """ Fonction pour afficher les informations d'un bloc.

        Précondition : 
        Exemple(s) :
        $$$ Bloc((0, 0), (50, 50), (255, 0, 0))
        Bloc((0, 0), (50, 50), (255, 0, 0))

        """
        
        return f"Bloc({self.coord_haut_gauche}, {self.coord_bas_droite}, color={self.color})"
    
    def __eq__(self, other) :
        """ Fonction pour vérifier si deux blocs sont égaux.

        Précondition : 
        Exemple(s) :
        $$$ Bloc((0, 0), (50, 50), (255, 0, 0)) == Bloc((0, 0), (50, 50), (255, 0, 0))
        True
        $$$ Bloc((0, 0), (50, 50), (255, 0, 0)) == Bloc((0, 0), (50, 50), (0, 255, 0))
        False

        """
        
        if not isinstance(other, Bloc):
            return False
        return (self.coord_haut_gauche == other.coord_haut_gauche and
                self.coord_bas_droite == other.coord_bas_droite and
                self.color == other.color)