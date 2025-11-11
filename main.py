"""Lecture et manipulation de listes numériques stockées dans un CSV.

Ce module fournit des utilitaires pour lire le fichier `listes.csv`
et effectuer des opérations simples sur les listes (premier, dernier,
min, max, somme, etc.).
"""

#### Imports et définition des variables globales

FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    l = []
    # ouvrir le fichier et lire toutes les lignes
    with open(filename, mode="r", encoding="utf8") as fh:
        lines = fh.readlines()

    # chaque ligne contient des entiers séparés par ';'
    # on nettoie la ligne, on split et on convertit en int
    for line in lines:
        s = line.strip()
        if not s:
            continue
        parts = s.split(";")
        row = [int(x) for x in parts if x != ""]
        l.append(row)

    return l

def get_list_k(data, k):
    """Retourne la k-ième liste dans ``data``.

    Args:
        data (list[list[int]]): liste de listes d'entiers.
        k (int): indice (0-based) de la liste à retourner.

    Returns:
        list[int]: la liste à l'indice ``k``.

    Note:
        Une ``IndexError`` est levée si ``k`` est hors bornes (comportement
        attendu pour les tests de cet exercice).
    """
    return data[k]

def get_first(l):
    """Retourne le premier élément de la liste ``l`` ou ``None`` si vide."""
    if not l:
        return None
    return l[0]

def get_last(l):
    """Retourne le dernier élément de la liste ``l`` ou ``None`` si vide."""
    if not l:
        return None
    return l[-1]

def get_max(l):
    """Retourne la valeur maximale de ``l`` ou ``None`` si la liste est vide."""
    if not l:
        return None
    return max(l)

def get_min(l):
    """Retourne la valeur minimale de ``l`` ou ``None`` si la liste est vide."""
    if not l:
        return None
    return min(l)

def get_sum(l):
    """Retourne la somme des éléments de ``l``. Renvoie 0 si ``l`` est vide."""
    if not l:
        return 0
    return sum(l)


#### Fonction principale


def main():
    """Point d'entrée principal utilisé pour de courts tests manuels.

    Le bloc de test original est laissé en commentaire pour référence.
    """
    data = read_data(FILENAME)
    k = 37
    lst = get_list_k(data, k)
    print(k, lst)
    print(get_first(lst), get_last(lst), get_sum(lst))


if __name__ == "__main__":
    main()
