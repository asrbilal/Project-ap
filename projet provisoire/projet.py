#Bilal Anseur

from PIL import Image


def moyennes_couleurs(colors:tuple):
    """Calcule la couleur moyenne d'une liste de pixels représentés au format RGB.

    Précondition : 
    Exemple(s) :
    $$$ pixels = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  # Rouge, vert, bleu
    $$$ moyennes_couleurs([(255, 0, 0), (0, 255, 0), (0, 0, 255)])
    $$$ (85, 85, 85)
    """
    
    num_pixels = len(colors)
    if num_pixels == 0:
        return (0, 0, 0)  # Par défaut, noir s'il n'y a pas de pixels
    r_sum, g_sum, b_sum = 0, 0, 0
    for color in colors:
        r_sum += color[0]
        g_sum += color[1]
        b_sum += color[2]
    r_avg = r_sum // num_pixels
    g_avg = g_sum // num_pixels
    b_avg = b_sum // num_pixels
    return (r_avg, g_avg, b_avg)

# Fonction pour vérifier si deux couleurs sont proches dans un certain seuil
def colors_close(color1:tuple, color2:tuple, threshold=10):
    """Vérifie si deux couleurs au format RGB sont proches l'une de l'autre.


    Précondition : 
    Exemple(s) :
    $$$ color1 = (255, 0, 0)  # Rouge
    $$$ color2 = (250, 5, 10)  # Rouge avec des nuances
    $$$ colors_close(color1, color2)
    $$$ False

    """
    
    r_diff = abs(color1[0] - color2[0])
    g_diff = abs(color1[1] - color2[1])
    b_diff = abs(color1[2] - color2[2])
    total_diff = r_diff + g_diff + b_diff
    return total_diff <= threshold

# Fonction pour charger une image à partir d'un fichier
def charge_image(file_path:str):
    """fonction pour charger une image à partir d'un fichier spécifié.

    Précondition : 
    Exemple(s) :
    $$$ image = charge_image("calbuth.png")
    $$$ image.size
    (256, 256)

    """
    
    return Image.open(file_path)

# Fonction pour enregistrer une image dans un fichier
def enregistrement_image(image:tuple, file_path:str):
    """fonction pour enregistrer une image dans un fichier spécifié.

    Précondition : 
    Exemple(s) :
    $$$ image = Image.new("RGB", (100, 100))
    $$$ enregistrement_image(image, "calbuth.png")
    $$$ image.size
    (100, 100)

    """
    
    image.save(file_path)

# Fonction pour enregistrer une image au format CSV
def enregistrement_image_csv(blocks:Block, file_path:str):
    """  Enregistre les données des blocs dans un fichier CSV spécifié.

    Cette fonction parcourt récursivement tous les blocs et écrit leurs coordonnées et leurs couleurs dans un fichier CSV.


    Précondition : 
    Exemple(s) :
    $$$ blocks = [Block((0, 0), (50, 50), (255, 0, 0)), Block((50, 0), (100, 50), (0, 255, 0)),  Block((0, 50), (50, 100), (0, 0, 255)),  Block((50, 50), (100, 100), (255, 255, 0)) ]
    $$$ enregistrement_image_csv(blocks, "output_image.csv")
    $$$ open("output_image.csv").read()

    """
    
    with open(file_path, 'w') as f:
        for block in blocks:
            csg_x, csg_y = block.csg
            cid_x, cid_y = block.cid
            color_r, color_g, color_b = block.color
            
            # Écrivez les coordonnées et la couleur du bloc dans le fichier
            f.write(f"{csg_x},{csg_y},{cid_x},{cid_y},{color_r},{color_g},{color_b}\n")
# Fonction pour diviser une image en blocs
def split_image(image:tuple, ordre:int):
    """ Divise une image en blocs de taille égale et calcule les couleurs moyennes de chaque bloc.

    Cette fonction prend une image en entrée et la divise en blocs de taille égale en fonction du nombre d'itérations spécifié par l'argument 'ordre'. Pour chaque bloc, elle calcule la couleur moyenne en prenant en compte les valeurs des pixels dans ce bloc.


    Précondition :  ordre >= 0 
    Exemple(s) :

    $$$ image = Image.new("RGB", (100, 100))
    $$$ split_image(image, 2)
    [Block((0, 0), (50, 50), (255, 0, 0)), Block((50, 0), (100, 50), (0, 255, 0)),  Block((0, 50), (50, 100), (0, 0, 255)),  Block((50, 50), (100, 100), (255, 255, 0)) ]
    

    """
    
    width, height = image.size
    block_size = max(width, height) // (2 ** ordre)
    blocks = []
    for x in range(0, width, block_size):
        for y in range(0, height, block_size):
            csg = (x, y)
            cid = (min(x + block_size, width), min(y + block_size, height))
            block_image = image.crop((x, y, cid[0], cid[1]))
            block = Block(csg, cid)
            block.color = moyennes_couleurs(list(block_image.getdata()))
            blocks.append(block)
    return blocks



# Fonction pour appliquer l'algorithme à chaque bloc de manière récursive
def algo(blocks: Block, ordre:int) -> Image:
    """ Applique un algorithme récursif sur une liste de blocs pour diviser les blocs en sous-blocs et recalculer les couleurs moyennes.

    Cette fonction prend une liste de blocs en entrée et applique un algorithme récursif pour diviser les blocs en sous-blocs. Elle permet également de recalculer les couleurs moyennes des blocs en fonction du nombre d'itérations spécifié par l'argument 'ordre'.

    Précondition : 
    Exemple(s) :
    $$$ blocks = [Block((0, 0), (50, 50), (255, 0, 0)), Block((50, 0), (100, 50), (0, 255, 0)),  Block((0, 50), (50, 100), (0, 0, 255)),  Block((50, 50), (100, 100), (255, 255, 0)) ]
    $$$ ordre=3
    $$$ algo(blocks,ordre)

    """
    
    if ordre == 0:
        return  # Pas besoin de faire de moyenne lorsque l'ordre est 0
    else:
        for block in blocks:
            if not block.is_uniform():
                sub_images = split_image(Image.new("RGB", (block.cid[0] - block.csg[0], block.cid[1] - block.csg[1]), block.color))
                algo(sub_images, ordre - 1)
                block.sousbloc = sub_images
        # Maintenant que tous les sous-blocs ont été traités, nous pouvons calculer la couleur moyenne
                block.color = moyennes_couleurs([sousbloc.color for sousbloc in block.sousbloc])

# Fonction pour visualiser les blocs
def visualisation(blocks:Block, image_size:tuple):
    """Cette fonction parcourt récursivement tous les blocs et les dessine sur une image en fonction de leurs attributs.
    Exemple(s) :
    $$$ image_size = (100, 100)
    $$$ blocks = [Block((0, 0), (50, 50), (255, 0, 0)), Block((50, 0), (100, 50), (0, 255, 0)),  Block((0, 50), (50, 100), (0, 0, 255)),  Block((50, 50), (100, 100), (255, 255, 0)) ]
    $$$ image = visualisation(blocks, image_size)
    $$$ image.enregistre("example_image.png")
    $$$ image.show()
    """
    
    image = Image.new("RGB", image_size)
    for block in blocks:
        if block.is_uniform():
            image.paste(block.color, (block.csg[0], block.csg[1], block.cid[0], block.cid[1]))
        else:
            visualisation(block.sousbloc, image_size)
    return image

# Function to process command line arguments and perform actions accordingly
def ligne_de_commande():
    input_file_path = input("Entrez le nom du fichier d'entrée (avec extension): ")
    ordre = int(input("Entrez l ordre: "))
    sortie = input("entrez 'afficher' pour afficher l'image ou 'enregistrer' pour l'enregistrer au format CSV: ")

    if sortie not in ['afficher', 'enregistrer']:
        print("Action de sortie invalide. Choisissez s'il vous plaît 'afficher' ou 'enregistrer'.")
        return

    if input_file_path.endswith('.png'):
        # Charger l'image
        image = charge_image(input_file_path)
        image = image.convert('RGB')
        
        blocks = split_image(image, ordre)
        algo(blocks, ordre)

        if sortie == 'afficher':
            output_image = visualisation(blocks, image.size)
            output_image.show()
        elif sortie == 'enregistrer':
            enregistrer_image_csv(blocks, "output_image.csv")
            print("enregistrerd ...")

    elif input_file_path.endswith('.csv'):
        print("Lecture du fichier CSV")
        # Lire CSV et créer des blocs
        blocks = []
        with open(input_file_path, 'r') as f:
            for line in f:
                data = line.strip().split(',')
                if len(data) == 7:
                    csg_x, csg_y, cid_x, cid_y = map(int, data[:4])
                    color_r, color_g, color_b = map(int, data[4:])
                    block = Block((csg_x, csg_y), (cid_x, cid_y), (color_r, color_g, color_b))
                    blocks.append(block)
                         
        print("Lecture du fichier CSV.")
        
        if sortie == 'afficher':
            print("visualisation...")
         # Si nous visualisons des blocs, nous devons considérer la taille de l'image entière
            max_x = max([block.cid[0] for block in blocks])
            max_y = max([block.cid[1] for block in blocks])
        
            output_image = visualisation(blocks, (max_x, max_y))
            output_image.show()
        elif sortie == 'enregistrer':
            enregistrer_image_csv(blocks, "output_image.csv") 
            print("enregistrerd ...")
            

    else:
        print("Type de fichier invalide. Veuillez fournir un fichier .png ou .csv.")
        return

    

#Appelez la fonction pour traiter les arguments de la ligne de commande
ligne_de_commande()


