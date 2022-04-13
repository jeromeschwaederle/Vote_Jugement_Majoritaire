##### APPLICATION EN CLI POUR LE VOTE PAR JUGEMENT MAJORITAIRE #####
import os

# Nombre maximum de candidats
CANDIDATS = 10

# Nombre maximum d'électeurs
ELECTEURS = 100

# Mentions
MENTIONS_COURTES = ["A", "B", "C", "D", "E", "F", "G"]

MENTIONS_LONGUES = {
    "A": "TRÈS BIEN",
    "B": "BIEN",
    "C": "PLUTÔT BIEN",
    "D": "PLUTÔT MAUVAIS",
    "E": "MAUVAIS",
    "F": "TRÈS MAUVAIS",
    "G": "À REJETER"
}

# Liste des candidats
liste = []

# Scrutin
urne = {}


def main():

    global nature_candidats 
    global nb_cand
    global nb_elec
    global objet_du_vote
    global urne
    global liste

    # Définie l'objet du vote
    objet_du_vote = objet_vote()

    # Définie la nature des candidats / propositions
    nature_candidats = nature()
    
    # Définie le nombre de candidat / propositions en appelant la fonction nb_candidats
    nb_cand = nb_candidats()
    
    # Demande les noms des candidats qui ne peuvent pas être identiques
    noms_candidats()

    # Demande le nombre d'électeurs
    nb_elec = nb_electeurs()

    # Procède au vote
    scrutin()

    # Ordonne l'intérieur des profiles des candidats
    ordonne_profile()

    # Définie la mention majoritaire de chaque candidat
    mention_majoritaire()

    # Donne le classement des résultats
    results()

    # Affiche les résultats
    affichage_classement()


# Formatte l'affichage des questions
def affichage(*a_afficher):
    os.system("clear")
    y = "\n"
    z = "{:*^80}"
    b = z.format("")
    print(b)
    for phrase in a_afficher:
        a = z.format(f"  {phrase}  ")
        print(a)
    print(b, y)


# Formatte l'affichage sans "clear"
def affichage_no_clear(*a_afficher):
    z = "{:*^80}"
    b = z.format("")
    print(b)
    for phrase in a_afficher:
        a = z.format(f"  {phrase}  ")
        print(a)
    print(b)


# Affiche juste une ligne
def affichage_ligne(a_afficher):
    z = "{:*^80}"
    b = z.format("")
    a = z.format(f"  {a_afficher}  ")
    print(a)


# Définie l'objet du vote
def objet_vote():

    while True:

        a = " QUEL EST L'OBJET DU VOTE ? "
        b = " (Exemple : Choisir où on part pour les prochaines vacances) "

        affichage(a, b)

        vote = input("")

        if len(vote) > 0 and vote.isprintable() and not vote.isspace():
            vote = vote.lstrip()
            vote = vote.rstrip()
            break

    return vote


# Définie la nature du/des candidats
def nature():

    while True:

        a = " QUEL EST LA NATURE DES CANDIDATS ? "
        affichage(a)

        nat = input("")

        if len(nat) > 0 and nat.isprintable() and not nat.isspace():
            nat = nat.lstrip()
            nat = nat.rstrip()
            break

    return nat  


# Définie le nombre de candidats / propositions
def nb_candidats():

    global nb_cand

    while True:

        # Demande à l'utilisateur le nombre de candidats
        a = f" Quel est le nombre de {nature_candidats} ? "
        b = f" Merci de donner un entier positif entre 1 et {CANDIDATS}. "
        affichage(a,b)

        nb_cand = input("")

        # Si c'est un entier positif
        if nb_cand.isdigit():

            # Parse en integer
            nb_cand = int(nb_cand)

            # check que c'est pas supérieur à la constante CANDIDATS
            if nb_cand <= CANDIDATS and nb_cand > 0:
                break

    # Rends la valeur donnée par l'utilisateur
    return int(nb_cand)


# Demande les nom des candidats
def noms_candidats():

    # Demande à l'utilisateur le nom des candidats
    a = f" Quels sont les noms des {nature_candidats} ? "
    affichage(a)

    # Pour chaque candidats
    for i in range(nb_cand):
        # Oblige l'utilisateur à donner des noms
        while True: 
            reponse = input(f"{nature_candidats} n°{i + 1}: ")
            reponse = reponse.lstrip()
            reponse = reponse.rstrip()
            if reponse in liste:
                print("Chaque candidat doit avoir un nom différent")
            if len(reponse) > 0 and reponse not in liste:
                liste.append(reponse)
                break


# Définie le nombre d'électeurs
def nb_electeurs():

    while True:

        # Demande à l'utilisateur le nombre d'électeurs
        a = " Quel est le nombre d'électeur ? "
        b = f" Merci de donner un entier positif entre 1 et {ELECTEURS}. "
        affichage(a, b)

        nb_elec = input()

        # Si c'est un entier positif
        if nb_elec.isdigit():

            # Parse en integer
            nb_elec = int(nb_elec)

            # check que c'est inférieur ou égal à la constante CANDIDATS et supérieur à 0
            if nb_elec <= ELECTEURS and nb_elec > 0:
                break

    return int(nb_elec)


# Le scrutin
def scrutin():
    
    # Met le nom des candidats dans l'urne
    for candidat in liste:
        urne[candidat] = ""

    # Pour chaque électeur
    for electeur in range(nb_elec):

        # Phrase de présentation
        a = f" Pour {objet_du_vote}, "
        b = " ayant pris tous les éléments en considération, "
        c = f" je juge en conscience que ces {nature_candidats} sont : "
        d = f" A = {MENTIONS_LONGUES['A']} | B = {MENTIONS_LONGUES['B']} | C = {MENTIONS_LONGUES['C']} | D = {MENTIONS_LONGUES['D']}"
        e = f" E = {MENTIONS_LONGUES['E']} | F = {MENTIONS_LONGUES['F']} | G = {MENTIONS_LONGUES['G']} "
        z = f"Électeur n°{electeur + 1}/{nb_elec}"
        affichage(a, b, c, d, e)
        affichage_no_clear(z)
        for candidat in liste:
            affichage_ligne(candidat)
        print("{:*^80}".format(""))            

        # Pour chaque candidat
        for candidat in liste:
            while True:
                mention = input(f"---> {candidat}: ")
                if mention in MENTIONS_COURTES:
                    urne[candidat] += mention
                    break
                f = " Merci de noter avec une seule lettre majuscule entre A et G "
                affichage_no_clear(f, d, e)
   

# Ordonne le "Merit Profile" des candidats dans l'urne
def ordonne_profile():
    for candidat in liste:
        profile = urne[candidat]
        sorted_profile = sorted(profile)
        profile = "".join(sorted_profile)
        urne[candidat] = profile


def mention_majoritaire():

    global mentionMaj
    mentionMaj = {}

    # Si le nombre d'électeur est impair
    if nb_elec % 2 == 1:
        # Définie le charactère du milieu (x)
        x = int(round((nb_elec - 1)/ 2)) 
        for candidat in liste:
            mentionMaj[candidat] = urne[candidat][x]

    # Si le nombre d'électeur est pair
    if nb_elec % 2  == 0:
        # Trouve les deux charactères du milieu (x, y)
        for candidat in liste:
            x = int(round((nb_elec/2)) - 1)
            y = int(round(nb_elec / 2))
            mentionMaj[candidat] = urne[candidat][x]
            mentionMaj[candidat] += urne[candidat][y]


          
# Calcule et donne le classement des résultats
def results():

    global classement
    global mentionMaj

    # Pour les résultats définitifs
    classement = {}    

    # Initialise à zéro les défaites des candidats
    départagés = {}
    for candidat in liste:
        départagés[candidat] = 0
    
    # Si le nombre d'électeur est impair
    if nb_elec % 2 == 1:
        # Définie le charactère du milieu (x)
        x = int(round((nb_elec - 1)/ 2))   

    # Pour faire tous les duels entre toutes les paires de candidats
    for _ in range(len(liste)):

        # Pour indexer dans la liste des candidats
        a = 1
        b = len(liste)
        
        while (b - a > _):

            # Si le nombre d'électeur est pair
            if nb_elec % 2  == 0:
                # Trouve les deux charactères du milieu (x, y)
                x = int(round((nb_elec/2)) - 1)
                y = int(round(nb_elec / 2))
            else:
                compteur = 0

            while True:

                # Traite le cas de l'égalité parfaite
                if urne[liste[_]] == urne[liste[b - a]]:
                    break

                # Élargie la mention d'un vote des deux côtés de la médiane à chaque tour
                # Si c'est impair
                if nb_elec % 2 == 1:
                    mentionAComparer1 = urne[liste[_]][x - compteur]
                    mentionAComparer11 = urne[liste[_]][x + compteur]
                    mentionAComparer2 = urne[liste[b - a]][x - compteur]
                    mentionAComparer22 = urne[liste[b - a]][x + compteur]
      
                # Si c'est pair
                else:
                    mentionAComparer1 = urne[liste[_]][x]
                    mentionAComparer11 = urne[liste[_]][y]
                    mentionAComparer2 = urne[liste[b - a]][x]
                    mentionAComparer22 = urne[liste[b - a]][y]
                
                # Si les mentions diffères
                if mentionAComparer1 != mentionAComparer2 or mentionAComparer11 != mentionAComparer22:
                    # Arrête d'élargir
                    break

                # Sinon, élargi plus et recommence
                # Si le nombre d'électeur est impair
                if nb_elec % 2 == 1:
                    compteur += 1
                # Si le nombre d'électeur est pair
                else:
                    x -= 1
                    y += 1

            # En cas d'égalité
            if urne[liste[_]] == urne[liste[b - a]]:
                pass
        
            # Gère tous les cas particuliers du consensus et de la domination
            elif (mentionAComparer1 > mentionAComparer2 and mentionAComparer11 < mentionAComparer22)\
            or (mentionAComparer1 < mentionAComparer2 and mentionAComparer11 < mentionAComparer22)\
            or (mentionAComparer1 <= mentionAComparer2 and mentionAComparer11 < mentionAComparer22)\
            or (mentionAComparer1 < mentionAComparer2 and mentionAComparer11 <= mentionAComparer22):

                # Ajoute une défaite au dict "départagé"
                départagés[liste[b - a]] += 1        

            else:
                départagés[liste[_]] += 1

            a += 1

    # Inverse le dictionnaire "départagés" et classe les candidats dans le dict "classement"
    global rang_sorted
    rang_sorted = []
    rang = départagés.values()
    for element in sorted(rang):
        if element not in rang_sorted:
            rang_sorted.append(element) 

    for key, value in départagés.items():
        if value not in classement:
            classement[value] = [key]
        else:
            classement[value] += [key]



# Formatte l'affichage du classement
def affichage_classement():

    a = "RÉSULTATS"
    affichage(a)

    # Retient la longueur du nom du candidat le plus long
    taille_nom = 0
    for value in classement.values():
        for _ in range(len(value)):
            if len(value[_]) > taille_nom:
                taille_nom = len(value[_])


    # Retient la longueur de la mention la plus longue
    taille_mention = 0
    for candidat in liste:
        if int(round(nb_elec % 2)) == 1:
            if len(MENTIONS_LONGUES[mentionMaj[candidat]]) > taille_mention:
                taille_mention = len(MENTIONS_LONGUES[mentionMaj[candidat]])
        else:
            if len(MENTIONS_LONGUES[mentionMaj[candidat][0]]) > taille_mention:
                    taille_mention = len(MENTIONS_LONGUES[mentionMaj[candidat][0]])
            if len(MENTIONS_LONGUES[mentionMaj[candidat][1]]) > taille_mention:
                    taille_mention = len(MENTIONS_LONGUES[mentionMaj[candidat][1]])

    # Affiche le résultat ligne par ligne
    for rang in rang_sorted:
        for _ in range(len(classement[rang])):
            if int(round(nb_elec % 2)) == 1:
                print(f"[{rang + 1}] {classement[rang][_].ljust(taille_nom + 3)}{MENTIONS_LONGUES[mentionMaj[classement[rang][_]]].ljust(taille_mention + 3)}[{urne[classement[rang][_]]}]\n")
            # Prend en compte les difficultés pour l'affichage des résultats quand il y a un nombre pair d'électeurs
            else:
                if MENTIONS_LONGUES[mentionMaj[classement[rang][_]][0]] != MENTIONS_LONGUES[mentionMaj[classement[rang][_]][1]]:
                    print(f"[{rang + 1}] {classement[rang][_].center(taille_nom + 3)}{MENTIONS_LONGUES[mentionMaj[classement[rang][_]][0]].rjust(taille_mention + 2)} - {MENTIONS_LONGUES[mentionMaj[classement[rang][_]][1]].ljust(taille_mention + 2)}[{urne[classement[rang][_]]}]\n")
                else:
                    print(f"[{rang + 1}] {classement[rang][_].center(taille_nom + 3)}{MENTIONS_LONGUES[mentionMaj[classement[rang][_]][0]].center(taille_mention * 2 + 7)}[{urne[classement[rang][_]]}]\n")

    z = "{:*^80}"
    b = z.format("")
    print(b)
    print(b)
    print(b)
    
    while True:
        enter = input("")
        if enter == "":
            break


main()