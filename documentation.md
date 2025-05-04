# Star Battle Projet 2algo

## 1. Introduction

Présentation du projet Star Battle

## 2. Contraintes du problème

Les règles du Star Battle sont les suivantes :

- Chaque ligne comporte exactement 2 étoiles.
- Chaque colonne comporte exactement 2 étoiles.
- Chaque région comporte exactement 2 étoiles.
- Deux étoiles ne peuvent être adjacentes (horizontalement, verticalement et diagonalement).

## 2. Résolution avec différents domaines et algorithmes


### 2.2 Les domaines sont les colonnes de la grille

#### Backtracking
 -Logique :
    -Choix d'une case de départ par exemple (row=0, col=0)
    -On place une étoile en fonction des contraintes (méthode is_valid)
    -Si k étoiles a été placé sur la colonne on passe à la suivante
    -sinon on revient à la première colonne en incrémentant la case de départ (row+=1, col=0)  

 -temps moyen de résolution : 30 secondes

#### Forward checking
 -Logique :
    -Choix d'une case de départ par exemple (row=0, col=0)
    -On place une étoile en fonction des contraintes (méthode is_valid)
    -on place des "X" pour indiquer la cases interdites par les constraintes
    -Si k étoiles a été placé sur la colonne on passe à la suivante
    -sinon on revient à la première colonne en incrémentant la case de départ (row+=1, col=0) en supprimant les "X"  

 -temps moyen de résolution : 5 minutes

#### Forward checking with minimum remaining values
    #todo 

### 2.3 Les domaines sont les régions de la grille

#### Backtracking
 -Logique :
    -Lors de la première itération on trie les régions en fonction du nombre de cases
    -On prend la région la plus petite dans la liste de regions trié établi
    -On place une étoile en fonction des contraintes (méthode is_valid)
    -Si k étoiles a été placé sur la région on passe à la suivante
    -Sinon on reste sur la même région pour placer les étoiles

 -temps moyen de résolution : 

#### Forward checking
 -Logique :
    -Lors de la première itération on trie les régions en fonction du nombre de cases
    -On prend la région la plus petite dans la liste de regions trié établi
    -On place une étoile en fonction des contraintes (méthode is_valid)
    -on place des "X" pour indiquer la cases interdites par les constraintes
    -Si k étoiles a été placé sur la région on passe à la suivante
    -Sinon on reste sur la même région pour placer les étoiles

 -temps moyen de résolution : 

#### Forward checking with minimum remaining values
- Explication de l'implémentation
- Analyse de l'impact du MRV
- Comparaison complète des approches

## 3. Résultats et analyse

Comparaison globale des différentes approches:
- Temps d'exécution
- Nombre de noeuds explorés
- Efficacité selon la taille des grilles

## 4. Conclusion

Synthèse des résultats et pistes d'amélioration possibles.

## 5. Annexes

Grilles de test utilisées, captures d'écran, etc.