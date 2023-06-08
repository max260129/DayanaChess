from os import system, name

# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def draw_chess_board():
    # Numérotation des colonnes
    print("    a   b   c   d   e   f   g   h")

    # Liste des pièces de départ pour chaque colonne
    pieces = ['♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜']
    pawns = ['♟', '♟', '♟', '♟', '♟', '♟', '♟', '♟']

    # Dessiner les lignes de l'échiquier
    for row in range(8):
        # Dessiner une ligne avec les cases et les barres verticales
        print("  +" + "---+" * 8)

        # Afficher le numéro de ligne
        print(row + 1, end=" ")

        for col in range(8):
            # Afficher la barre verticale
            print("|", end="")

            # Afficher la pièce correspondante
            if row == 0:
                piece = pieces[col]
            elif row == 1:
                piece = pawns[col]
            elif row == 6:
                piece = pawns[col].lower()
            elif row == 7:
                piece = pieces[col].lower()
            else:
                piece = " "

            print(f" {piece} ", end="")

        # Afficher la dernière barre verticale de la ligne
        print("|")

    # Afficher la dernière ligne horizontale
    print("  +" + "---+" * 8)


def is_valid_move(move, player):
    # Vérifier la syntaxe du coup
    if len(move) != 4:
        print("Le coup doit être entré sous la forme de_case_à_case (par exemple, a2a4).")
        return False



# Fonction pour demander au joueur d'entrer un coup
def get_player_move(player):
    move = input(f"Joueur {player}, entrez votre coup (par exemple, a2a4) : ")
    return move

# Appeler la fonction pour dessiner l'échiquier
draw_chess_board()

# Boucle de jeu
player = 1
while True:
    # Demander au joueur d'entrer son coup
    move = get_player_move(player)

    # Vérifier si le coup est valide
    valid = is_valid_move(move, player)

        

    # Effectuer le coup (mettre à jour l'état de l'échiquier)


    # Dessiner l'échiquier mis à jour
    clear()   
    draw_chess_board()

    # Passer au joueur suivant
    player = 3 - player  # Alterner entre les joueurs 1 et 2 (par exemple)


    # Répéter le processus jusqu'à la fin du jeu
