# #!/bin/env python
# # -*-coding: utf-8 -*-

# def aff_menu1():
#     print("\033[H\033[J")
#     print("\n\033[31mBienvenue sur le Shell interactif ! \033[0m\n")
#     print("====================================================\n")
#     print("1 : Informations generales \n")
#     print("2 : Reseaux \n")
#     print("3 : Processus \n")
#     print("====================================================\n")
#     print("Tapez sur 'quit' pour quitter :")


def aff_menu2(princip_window):
   # princip_window.addstr(16, 0,"0 : Retour en arriere")
    # print("\033[H\033[J")
    # print("\n\033[31mBienvenue sur le Shell interactif ! \033[0m\n")
    princip_window.addstr(1, 0,"============================================================================")
    # print("0 : Retour au menu principal \n")
    princip_window.addstr(3, 20,"1 : Version du systeme d'exploitation ")
    princip_window.addstr(5, 20,"2 : Uptime ")
    princip_window.addstr(7, 20,"3 : Version du kernel ")
    princip_window.addstr(9, 20,"4 : Informations du hardware")
    princip_window.addstr(11, 20,"5 : Limite de fichiers ouverts")
    princip_window.addstr(13, 20,"6 : Limite de processus ouverts")
    princip_window.addstr(15, 20,"7 : Paquets installes ")
    #princip_window.addstr(17, 10,"====================================================")
    princip_window.addstr(17, 0,"===========================================================================")
    princip_window.refresh()
    # print("Tapez sur 'quit' pour quitter :\n")

def aff_menu3(princip_window):
    princip_window.clear()
    princip_window.addstr(1, 0,"============================================================================")
    princip_window.addstr(3,20,"1 : Adresse IP ")
    princip_window.addstr(5,20,"2 : Interfaces existantes ")
    princip_window.addstr(7,20,"3 : Nombre de paquets transmis/recu ")
    princip_window.addstr(9,20,"4 : Routes")
    princip_window.addstr(11,20,"5 : Etat forward de paquet")
    princip_window.addstr(13,20,"a : Autre")
    princip_window.addstr(15,0,"============================================================================")
    #princip_window.addstr(15,0,"====================================================")
    princip_window.addstr(17, 0,"0 : Retour en arriere")

def aff_menu3bonus(princip_window):
    princip_window.clear()
    princip_window.addstr(2,0,"============================================================================")
    princip_window.addstr(4,20,"6 : Desactiver l'Interfaces Ethernet")
    princip_window.addstr(6,20,"7 : Activer l'Interfaces Ethernet")
    princip_window.addstr(8,20,"8 : Afficher le ping")
    princip_window.addstr(10,20,"9 : Activer ou Desactiver l'IP forward")
    princip_window.addstr(12,20,"a : Debut")
    princip_window.addstr(14,0,"============================================================================")

def aff_menu4(princip_window):
    princip_window.clear()
    princip_window.addstr(4,0,"============================================================================")
    princip_window.addstr(6,20,"0 : Retour au menu principal \n")
    princip_window.addstr(8,20,"2 : Afficher les details d'un processus \n")
    princip_window.addstr(10,20,"3 : Lancer un processus\n")
    princip_window.addstr(12,0,"============================================================================")


# def aff_menu4():
#     print("\033[H\033[J")
#     print("\n\033[31mBienvenue sur le Shell interactif ! \033[0m\n")
#     print("====================================================\n")
#     print("0 : Retour au menu principal \n")
#     print("1 : Afficher tous les processus \n")
#     print("2 : Afficher les details d'un processus \n")
#     print("3 : Lancer un processus\n")
#     print("====================================================\n")
#     print("Tapez sur 'quit' pour quitter :\n")
