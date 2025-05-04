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

#### Backtracking colonnes
 -Logique :
    -Choix d'une case de départ par exemple (row=0, col=0)
    -On place une étoile en fonction des contraintes (méthode is_valid)
    -Si k étoiles a été placé sur la colonne on passe à la suivante
    -sinon on revient à la première colonne en incrémentant la case de départ (row+=1, col=0)  


#### Forward checking colonnes
 -Logique :
    -Choix d'une case de départ par exemple (row=0, col=0)
    -On place une étoile en fonction des contraintes (méthode is_valid)
    -on place des "X" pour indiquer la cases interdites par les constraintes
    -Si k étoiles a été placé sur la colonne on passe à la suivante
    -sinon on revient à la première colonne en incrémentant la case de départ (row+=1, col=0) en supprimant les "X"  


#### Forward checking with minimum remaining values colonnes
 -Logique :
   -On trie les colonnes en fonction du nombre de case valide 
   -On place les étoiles en des contraintes (méthode is_valid, valid_cells)
   -On place les "X" en fonction des étoiles placé
   -Si le placement n'est pas valide on vient alors retirer les étoiles et les "X" placés
   -On passe à la colonne suivante si on trouve 2 étoiles dans la colonne


### 2.3 Les domaines sont les régions de la grille

#### Backtracking regions
 -Logique :
    -Lors de la première itération on trie les régions en fonction du nombre de cases
    -On prend la région la plus petite dans la liste de regions trié établi
    -On place une étoile en fonction des contraintes (méthode is_valid)
    -Si k étoiles a été placé sur la région on passe à la suivante
    -Sinon on reste sur la même région pour placer les étoiles


#### Forward checking regions
 -Logique :
    -Lors de la première itération on trie les régions en fonction du nombre de cases
    -On prend la région la plus petite dans la liste de regions trié établi
    -On place une étoile en fonction des contraintes (méthode is_valid)
    -on place des "X" pour indiquer la cases interdites par les constraintes
    -Si k étoiles a été placé sur la région on passe à la suivante
    -Sinon on reste sur la même région pour placer les étoiles


#### Forward checking with minimum remaining values regions
 -Logique :
   -On trie les regions en fonction du nombre de case valide 
   -On place les étoiles en des contraintes (méthode is_valid)
   -On place les "X" en fonction des étoiles placé
   -Si le placement n'est pas valide on vient alors retirer les étoiles et les "X" placés
   -On passe à la regions suivante si on trouve 2 étoiles dans la région




#### temps d'éxection

-solve_backtracking_cols:
   solve_backtracking_cols Solution trouvée et affichée
   Temps d'exécution: 26.0825 secondes

-solve_forward_checking_cols:
   solve_forward_checking_cols Solution trouvée et affichée
   Temps d'exécution: 169.5353 secondes

-solve_forward_checking_MRV_cols:
   Temps d'exécution: trop long (plus de 1h)

-solve_backtracking_regions:
   solve_backtracking_regions Solution trouvée et affichée
   Temps d'exécution: 11.6562 secondes

-solve_forward_checking_regions:
   solve_forward_checking_regions Solution trouvée et affichée
   Temps d'exécution: 74.1793 secondes

-solve_forward_checking_MRV_regions:
   solve_forward_checking_MRV_regions Solution trouvée et affichée
   Temps d'exécution: 7.0370 secondes

