# Pychess

# Introduction

Ce document met en excergue les différentes parties du code ainsi que la structure générale de ce dernier. Il est divisé en trois grandes parties :

1. Présentation rapide du projet

   - En quoi consiste t-il
   - Les fonctionalités implémentées

2. Structure du projet

   - La représentation des structures
   - La représentation des mécaniques

3. Comment Jouer

   - Les différentes mécaniques de jeu

# Présentation du projet

## En quoi consiste t-il

Ce projet est un jeu d'échec implémenté dans un but pédagogique. L'objectif étant de montrer nos compétences en programmation Python ou C ++ en fonction du choix de technologie.

**Pychess** est codé en _python_. Dans sa version 1.O.O il implémente les bases du jeu d'échec :

- le mouvement des pièces suivant les règles de déplacement.
- la capture de pion ennemi en adéquation avec les règles de capture.
- La continuité des mouvement tant que l'un des roi n'est pas capturé.
- La promotion d'un pion en Reine.

Le roque et le "en passant" ne sont malheuresement pas disponible dans cette version du jeu d'échec.

## Les fonctionnalités implémentés

Pour lui donner un aspect plus ergonomique ainsi qu'offrir une meilleure experience de jeu, il est possible de sauvegarder une partie afin de la reprendre ultérieurement.

Il est aussi possible de modifier l'affichage des pions celon deux modes:

- Le mode visuel qui permet d'afficher les pions en format unicode
- Le mode textuel qui affiche les pions en format texte

Nous verrons plus comment changer de mode.

# Structure du projet

## Réprensation des structures

Le projet est divisé en deux grands packages :

### 1. GameEngine

Ce package contient tout les fichiers concernant le moteur de jeu.

- La classe **_Pawn.py_** représente toutes les pièces du jeu d'échec. Elle contient tout les attributs tels que le type, la couleur ainsi que la position de la pièce sur l'échiquier.

- La classe **_ChessBoard.py_** représente quand à elle l'échiquier du jeu. Elle possède un état représentant toutes les pièces sur l'échiquier ainsi que tous les attributs concernant le déroulement de la partie. c'est une classe centrale car elle permet d'effectuer les actions de déplacement ainsi que gérer les interactions entre les pièces du jeu notemment en générant les différentes positions des pièces.
- Le fichier **_Position.py_** possède quand à lui deux fonctions utilitaire permettant la conversion des représentations de la position des pièces.

### 2. FileEngine

Ce package contient tout les scripts permettant la gestion des sauvegardes ainsi que la gestion de l'historique des mouvements. Voici les différents scripts et leurs présentation :

- **_history.py_** possède toutes les fonctions permettant l'écriture de l'historique des différentes actions durant la partie dans un fichier externe. Il enregistre l'historique dans un fichier renseigné par l'utilisateur en argument de programme. Si aucun chemin n'est renseigné, un fichier par défault est crée afin.

- **_load.py_** possède toutes les fonctions permettant la gestion de sauvegarde / chargement d'une partie. Il gère le dossier **_save_** (le crée s'il n'existe pas) dans lequel sera stocké le fichier de sauvegarde. **_Pychess_** gère les sauvegarde grace à la librairie pickle qui permet de sérialiser des objets. Ainsi, il sérialise l'objet Chessboard vue précédement.

## Réprésensation des mécaniques

### Les déplacements

Les déplacements sont gérés par la classe **_ChessBoard.py_**. Quand l'utilisateur choisis un pion, elle calcul les positions possible en fonction du type de la pièce. Ce calcul prend en compte toutes les pièces sur l'échiquier.

### La capture

Outres les déplacements, les captures sont aussi gérés par la classe **_ChessBoard.py_**. Quand une capture est possible, la position de la pièce à capturer est désigné comme étant mouvement possible. Quand la pièce se déplace sur cette position **_ChessBoard.py_** s'occupe alors de supprimer la pièce de l'échiquier ainsi que de donner le point à l'équipe qui a capturé la pièce.  
Si un des rois est capturé la partie s'arrete et le vainqueur est déclaré.

# Comment jouer

## Excecuter le projet

Le projet n'utilsant que les lirairies natives de python3, l'excécution du projet ce fait en allant à la racine du projet et tapant la commande suivante :

```bash
python3 main.py
```

## Jouer

**_PyChess_** suit les règles du jeu d'échec, aisni ce sont toujours aux blancs de commencer.  
Pour selectionner une pièce il suffit d'écrire les coordonées de la case sur laquelle se situe la pièce quand le jeu vous le demande. Par exemple si je veux selectionner une pièce en a7 j'écris a7 au moment de choisir mon pion.  
Il est possible que le jeu vous demande de choisir une autre pièce que celle initialement choisis si cette dernière n'a aucune position possible pour le tour en cour ou alors que la pièce choisit n'appartient pas à votre camp.

## Sauvegarder une partie

Vous pouvez sauvegarder une partie en cours au moment de choisir de votre pièce. Pour cela vous pouvez écrire "save" quand le jeu vous demande de choisir un pion. un message vous avertit de l'enregistrement de votre partie et cette dernière s'arrete. Noter qu'il ne peut y avoir qu'une seule sauvegarde à la fois, une sauvegarde en détruit une autre.

## Charger une partie

Si vous avez sauvegardé une partie au préalable, un message s'affichera à la prochaine ouverture vous demandant de charger ou non votre denrière partie.
Noter que si aucune sauvegarde n'a été faite au préalable, ce message ne s'affichera pas.

## Voir l'historique

Par défault le fichier d'historique se situe dans la racine du projet dans le fichier **_history.txt_**. Il est cependant possible de changer ce fichier en renseigant un le chemin du fichier en argument du programme.  
Par exemple :

```bash
# Le fichier d'historique se situera au chemin suivant
# /home/user/Document/text.txt

python3 main.py /home/user/Document/text.txt
```

Noter que le fichier par défault est unique, à chaque partie ce dernier est écrasé.

## Activer le mode unicode

Il est possible d'activer / désactiver le mode unicode via le fichier de configuration **_config.cfg_**. Il suffit de changer la valeur de unicode à true.

```
unicode = true
```

Noter que ce fichier dest sensible à la case, ainsi écrire True n'activera pas le mode unicode
