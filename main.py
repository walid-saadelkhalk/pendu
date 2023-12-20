import pygame
import pygame_menu
import random

pygame.init()
surface = pygame.display.set_mode((800, 600))
width, height = 800, 600

# Couleur de fond
background_color = (239, 98, 58)
# Police
custom_font = "police/PressStart2P-Regular.ttf"
menu_theme = pygame_menu.themes.THEME_BLUE.copy()  


menu = None

def difficulte(value):
    pass

def score():
    fenetre = pygame.display.set_mode((width, height))
    fenetre.fill((239, 98, 58))
    pygame.display.flip()

    # Obtenir le nom du joueur depuis le champ de saisie
    player_name = menu.get_input_data().get('JOUEUR', '')

    # Sauvegarder le nom du joueur dans le fichier "score.txt"
    with open('score.txt', 'a') as fichier_score:
        fichier_score.write(f"Joueur : {player_name}\n")

    # Image de Mario et fond
    image = pygame.image.load("images/mario.png")
    fenetre.blit(image, (550, 350))

    # Titre
    titre_font = pygame.font.Font("police/PressStart2P-Regular.ttf", 50)
    titre = titre_font.render("SCORE", True, (0, 0, 0))
    fenetre.blit(titre, (width // 2 - titre.get_width() // 2, 50))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        pygame.display.flip()




def demarrer_jeu():
    hangman()
    pass


def inserer_mot():
    insertion()
    pass


def insertion():
    fenetre = pygame.display.set_mode((width, height))
    fenetre.fill((239, 98, 58))
    pygame.display.flip()
    titre_font = pygame.font.Font("police/PressStart2P-Regular.ttf", 36)


    font = pygame.font.Font("police/PressStart2P-Regular.ttf", 25)
    mot_display_x = 50
    mot_display_y = 150
    ligne_spacing = 30

    running = True
    nouveau_mot = ""
    mots = []

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  
                    # Ajouter le mot à la liste et écrire dans le fichier
                    if nouveau_mot:
                        mots.append(nouveau_mot)
                        with open('mots.txt', 'a') as fichier_ajout:
                            fichier_ajout.write("\n" + nouveau_mot)
                    running = False
                    return

                # Gérer la suppression de caractères
                elif event.key == pygame.K_BACKSPACE:
                    nouveau_mot = nouveau_mot[:-1]
                else:
                    nouveau_mot += event.unicode

        #image mario et fond
        image = pygame.image.load("images/mario.png")
        fenetre.blit(image, (550, 350))

        #titre
        titre_font = pygame.font.Font("police/PressStart2P-Regular.ttf", 50)
        titre = titre_font.render("INSERER UN MOT", True, (0, 0, 0))
        fenetre.blit(titre, (width // 2  - titre.get_width() // 2, 50))

        # Affichage des mots
        for i, mot in enumerate(mots):
            text = font.render(mot, True, (0, 0, 0))
            fenetre.blit(text, (mot_display_x, mot_display_y + i * ligne_spacing))

        # Affichage du nouveau mot en cours de saisie
        text_nouveau_mot = font.render("Nouveau mot : " + nouveau_mot, True, (0, 0, 0))
        fenetre.blit(text_nouveau_mot, (10, 200))

        pygame.display.flip()


status_pendu = 0

def hangman():
    global status_pendu, mot, devine
    fenetre = pygame.display.set_mode((width, height))
    fenetre.fill((239, 98, 58))
    pygame.display.flip()
    titre_font = pygame.font.Font("police/PressStart2P-Regular.ttf", 36)
    titre_jeu = titre_font.render("HANGMAN", True, (0, 0, 0))
    fenetre.blit(titre_jeu, (width // 2  - titre_jeu.get_width() // 2, 30))

    #boutons
    radius = 20
    gap = 15
    lettres = []
    startx = round((width - (radius * 2 + gap) * 13) / 2)
    starty = 400
    a= 65

    for i in range(26):
        x = startx + gap * 2 + ((radius * 2 + gap) * (i % 13))
        y = starty + ((i // 13) * (gap + radius * 2))
        lettres.append([x, y, chr(a + i), True])



    #font
    lettre_font = pygame.font.SysFont("police/PressStart2P-Regular.ttf" , 25)
    mot_font = pygame.font.SysFont("police/PressStart2P-Regular.ttf" , 50)
    titre_font = pygame.font.SysFont("police/PressStart2P-Regular.ttf" , 60)  




    #images
    images = []
    for i in range(7):
        image = pygame.image.load("images/attaque"+str(i)+".png")
        images.append(image)
    print(images)



    #variables du jeu
    #choix du mot
    with open('mots.txt', 'r') as fichier:
        liste_mots = fichier.readlines()
    mots = list(liste_mots)
    mots = [mot.strip().lower() for mot in liste_mots]
    mot = random.choice(mots)
    devine = []



    def dessin():
        #image mario et fond
        image_mario = pygame.image.load("images/mario_hangman.png")
        fenetre.fill((239, 98, 58))
        fenetre.blit(image_mario, (610, 470))

        #hangman
        titre_font_hangman = pygame.font.Font("police/PressStart2P-Regular.ttf", 80)
        titre_hangman = titre_font_hangman.render("HANGMAN", True, (0, 0, 0))
        fenetre.blit(titre_hangman, (100, 500))

        #mots
        display_mot = ""
        for lettre in mot:
            if lettre in devine:
                display_mot += lettre 
            else:
                if i < len(mot):
                    display_mot += " _ "
                else:
                    display_mot += " _ "
        text = mot_font.render(display_mot, 1, (0, 0, 0))
        fenetre.blit(text, (width/2 - text.get_width()/2, height/7))

        # Boutons
        for lettre in lettres:
            x, y, ltr, visible = lettre
            if visible:
                pygame.draw.circle(fenetre, (0, 0, 0), (x, y), radius, 3)
                text = lettre_font.render(ltr, 1, (0, 0, 0))
                fenetre.blit(text, (x - text.get_width()/2, y - text.get_height()/2))
        fenetre.blit(images[status_pendu], (100, 50))
       


    #message de victoire/défaite
  
    def affichage_message(message, mot_perdu="", running=True):
        
        fenetre.fill((239, 98, 58))
        text = mot_font.render(message, 1, (0, 0, 0))
        fenetre.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2))

                    
        if mot_perdu:
            text_mot_perdu = mot_font.render(f"Le mot était : {mot_perdu}", 1, (0, 0, 0))
            fenetre.blit(text_mot_perdu, (width/2 - text_mot_perdu.get_width()/2, height/2 + 30))
        
        pygame.display.update()
        pygame.time.delay(3000)
        return False
        


    # Actions sur la fenêtrel

    def main():
        global status_pendu

        status_pendu = 0
        running = True
        while running:
   

            text = titre_font.render("Jeu du pendu" , 1, (0, 0, 0))
            fenetre.blit(text, (400,10))

            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    print("Touche enfoncée :", event.key)
                    if event.key in [pygame.K_a, pygame.K_b, pygame.K_c, pygame.K_d, pygame.K_e, pygame.K_f, pygame.K_g,
                                    pygame.K_h, pygame.K_i, pygame.K_j, pygame.K_k, pygame.K_l, pygame.K_m, pygame.K_n,
                                    pygame.K_o, pygame.K_p, pygame.K_q, pygame.K_r, pygame.K_s, pygame.K_t, pygame.K_u,
                                    pygame.K_v, pygame.K_w, pygame.K_x, pygame.K_y, pygame.K_z]:
                        lettre_pressee = chr(event.key).lower()
                        for lettre in lettres:
                            x, y, ltr, visible = lettre
                            if visible and ltr.lower() == lettre_pressee:
                                lettre[3] = False
                                devine.append(lettre_pressee)
                                if lettre_pressee not in mot:
                                    status_pendu += 1

            dessin()
            victoire = True
            for lettre in lettres: 
                if lettre not in devine:
                    victoire = False
                    break
                    

            victoire = all(lettre in devine for lettre in mot)
        
            
            if victoire:
                affichage_message("Vous avez gagné!")
                pygame.time.delay(30)
                break
                
                
            if status_pendu == 6:
                affichage_message("Vous avez perdu!", mot)
                pygame.time.delay(10)
                break
    

            pygame.display.update() 
        
    main() 
    
    pygame.display.flip()



# Titre
menu_theme.title_offset = (290, 40) 
menu_theme.title_font_color = (0, 0, 0)  
menu_theme.title_font_size = 60 
menu_theme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_NONE  

# Boutons
menu_theme.background_color = background_color  
menu_theme.title_font = custom_font
menu_theme.widget_font = custom_font
menu_theme.widget_font_size = 20 
menu_theme.widget_font_color = (0, 0, 0) 
menu_theme.widget_padding = 20  
menu_theme.selection_color = (255, 255, 255)  

# Menu général
menu = pygame_menu.Menu('MENU', 800, 600, theme=menu_theme)

# Ajouter une image au menu
image_path = "images/mario.png"
menu.add.image(image_path, scale=(0.5, 0.5), angle=0)

# Ajouter un bouton au menu
menu.add.selector('NIVEAU :', [('FACILE', 1), ('MOYEN', 2), ('DIFFICILE', 3)], onchange=difficulte)
menu.add.button('HANGMAN', demarrer_jeu())
menu.add.button('INSERER', inserer_mot)
menu.add.button('SCORE', score)
menu.add.button('QUITTER', pygame_menu.events.EXIT)

menu.mainloop(surface)
