# HideToSee

## Enoncé
Catégorie : [Cryptography](../)

Points : 100

Tags : 

Description :
> How about some hide and seek heh?  
> Look at this image here.

Hints :
1. Download the image and try to extract it.


## Approche

Le fichier `atbash.jpg` mis à disposition représente un disque associé à la méthode de chiffrement Atbash.  
Pour réaliser le chiffrement et le déchiffrement avec cet algorithme, on peut s'aider d'un outil en ligne : 
* dCode : https://www.dcode.fr/chiffre-atbash
* CyberChef : https://gchq.github.io/CyberChef/#recipe=Atbash_Cipher()

Reste à trouver le texte à déchiffrer !!!

Le fichier fourni étant une image, on pense alors au fait que le texte y est surement caché quelque part.

## Solution

### Piste 1 : Utilisation du couteau Suisse Aperi'Solve 

Le site [Aperi'Solve](https://www.aperisolve.com/) permet de tester rapidement différentes techniques de stéganogaphie.  
Malheureusement rien de probant.

### Piste 2 : Délires ...

Plusieurs tentatives réalisées en manipulant l'image (miroir, retournement, inversion des couleurs, ...) avant de la soumettre à Aperi'Solve.  
Pas mieux.

### Piste 3 : Retour aux sources

Le site Aperi'Solve propose également une [cheatsheet](https://www.aperisolve.com/cheatsheet) intéressante listant différents outils de stéganographie, dont ceux utilisés par le solver en ligne.  
Parmi ceux-ci :
* Steghide qui sait cacher dans une image / extraire d'une image des données associées à un "mot de passe".
* StegCracker et StegBrute qui comme Steghide peuvent extraire les données, en brutant forçant le "mot de passe" à partir d'un dictionnaire.

Personnellement j'ai utilisé [Stegseek](https://github.com/RickdeJager/stegseek), qui fait la même chose, associé à [Rockyou](https://gitlab.com/kalilinux/packages/wordlists) comme dictionnaire.  

Par soucis de simplicité, on peut utiliser la version containerisée.
Il suffit de déposer le fichier image (i.e. `atbash.jpg`) et le dictionnaire (i.e. `rockyou.txt`) dans un répertoire (exemple : /picoCTF_2023) qui sera monté en tant que volume /steg dans le container :

```txt
docker run -it --rm -v /picoCTF_2023:/steg rickdejager/stegseek atbash.jpg rockyou.txt
```

Le résultat ne se fait pas attendre :

```txt
StegSeek 0.6 - https://github.com/RickdeJager/StegSeek

[i] Found passphrase: ""
[i] Original filename: "encrypted.txt".
[i] Extracting to "atbash.jpg.out".
```

Le contenu du fichier extrait `atbash.jpg.out` est le suivant : 

```txt
krxlXGU{zgyzhs_xizxp_cccccccc}
```

En y appliquant l'algorithme Atbash pour le déchiffrer (https://gchq.github.io/CyberChef/#recipe=Atbash_Cipher()&input=a3J4bFhHVXt6Z3l6aHNfeGl6eHBfY2NjY2NjY2N9), on obtient le texte en clair :

```txt
picoCTF{atbash_crack_xxxxxxxx}
```
