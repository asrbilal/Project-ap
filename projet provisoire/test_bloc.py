def __add__(self, sous_bloc):
    """ Fonction pour ajouter un sous-bloc à un bloc.

    Précondition : 
    Exemple(s) :
    >>> bloc = Bloc()
    >>> sous_bloc = SousBloc()
    >>> bloc + sous_bloc
    >>> len(bloc.sous_bloc)
    1
    >>> bloc.sous_bloc[0] is sous_bloc
    True
    """
    
    self.sous_bloc.append(sous_bloc)