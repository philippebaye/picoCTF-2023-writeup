# rotation

## Enoncé
Catégorie : [Cryptography](../)

Points : 100

Tags : 

Description :
> You will find the flag after decrypting this file  
> Download the encrypted flag here.

Hints :
1. Sometimes rotation is right


## Approche

Le fichier `encrypted.txt` mis à disposition contient un message de la forme :
```txt
xqkwKBN{z0bib1wv_l3kzgxb3l_ffffffff}
```

D'après la forme du contenu, appuyée par le nom du challenge, on pense à un chiffrement de type César.  
Il ne reste plus qu'à trouver le bon décalage pour obtenir le texte en clair.  
Pour cela on peut s'appuyer sur des outils en ligne, par exemple :
* dCode : https://www.dcode.fr/chiffre-cesar
* CyberChef : https://gchq.github.io/CyberChef/


## Solution

On teste tous les décalages possibles.  
CyberChef propose l'opération "ROT13 Brute Force" pour cela : https://gchq.github.io/CyberChef/#recipe=ROT13_Brute_Force(true,true,false,100,0,true,'')&input=eHFrd0tCTnt6MGJpYjF3dl9sM2t6Z3hiM2xfZmZmZmZmZmZ9  
NB : dCode propose le même type de fonctionnalité.  
Le décalage de 18 caractères permet d'obtenir le texte en clair :
```txt
picoCTF{r0tat1on_d3crypt3d_xxxxxxxx}
```
