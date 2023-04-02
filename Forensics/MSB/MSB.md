# MSB

## Enoncé
Catégorie : [Forensics](../)

Points : 200

Tags : `steganography`

Description :
> This image passes LSB statistical analysis, but we can't help but think there must be something to the visual artifacts present in this image...  
> Download the image here

Hints :
1. What's causing the 'corruption' of the image?


## Approche

L'image `Ninja-and-Prince-Genji-Ukiyoe-Utagawa-Kunisada.flag.png` fournie représente une estampe Japonaise.
Ce même fichier est utilisé en référence d'un article Wikipedia sur les [Ninja](https://en.wikipedia.org/wiki/Ninja).

A la différence près que la copie dont on dispose est altérée sur la majeure partie haute.

Les 2 acronymes LSB et MSB font référence à :
* LSB : Least Significant Bit
* MSB : Most Significant Bit


## Solution

En stéganographie, LSB fait aussi référence à une technique consistant à manipuler les bits de poids faible d'un fichier afin d'y dissimuler une information.

Lorsque cette technique est appliquée sur une image, l'altération des bits de poids faible n'est pas perceptible à l'oeil nu, même en ayant l'image originale à proximité.

Par contre, il en va tout autrement lorsque l'altération est réalisée sur les bits de poids fort (MSB).

Pour extraire ces bits de poids fort et reconstituer les informations dissimulées, on peut utiliser un simple script (qui est l'option que j'ai choisi) ou un outil en ligne (exemple : https://stegonline.georgeom.net/upload).

Voici le script utilisé : [`msb.py`](msb.py) qui extrait les données dans un fichier `Ninja.extraction`.

Le fichier ainsi obtenu est un fichier texte. Une simple recherche de `picoCTF` permet d'y retrouver le flag.
