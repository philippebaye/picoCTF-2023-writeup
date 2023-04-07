# PowerAnalysis: Warmup

## Enoncé
Catégorie : [Cryptography](../)

Points : 200

Tags : 

Description :
> This encryption algorithm leaks a "bit" of data every time it does a computation. Use this to figure out the encryption key.  
> Download the encryption program here `encrypt.py`. Access the running server with `nc saturn.picoctf.net xxxxx`.  
> The flag will be of the format picoCTF{`<encryption key>`} where <encryption key> is 32 lowercase hex characters comprising the 16-byte encryption key being used by the program.

Hints :
1. The "encryption" algorithm is simple and the correlation between the leakage and the key can be very easily modeled.


## Approche

Le script python `encrypt.py` fourni prend en entrée un message de 16 bytes au format hexadécimal. Donc celui-ci doit être compris entre les 2 valeurs suivantes incluses :
```
00000000000000000000000000000000
FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
```

Pour chacun des 16 bytes du message (valeur comprise donc entre 00 et FF) on applique un XOR avec le byte correspondant de la clé de chiffrement :

$$message[i]\ \oplus \ key[i]$$

Le résultat est ensuite substitué par la valeur correspondante dans le tableau `Sbox`

On stocke le LSB (i.e. bit de poids faible) de la substitution (obtenu via l'opération `& 0x01`) dans le tableau `leak_buf`.

Une fois tous les bytes traités, ce tableau contient 16 éléments qui chaucun peuvent avoir uniquement l'une des 2 valeurs 0 ou 1.

En retour, le script nous indique le nombre de 1 présent dans le tableau `leak_buf`.

En appelant successivement le script et en consolidant les résultats ainsi obtenus, on doit pouvoir en déduire la clé de chiffrement utilisée.


## Solution

### Etape 1 : prise d'empreintes

Cette étape consiste à identifier pour chaque valeur possible d'un byte de la clé de chiffrement (valeur comprise entre 00 et FF, soit entre 0 et 255 exprimé en décimal), le résultat obtenu quand on le soumet aux différentes opérations permettant de constituer un élément du tableau `leak_buf` (XOR, puis substitution via `Sbox`, puis extraction du LSB) en le combinant avec les différentes valeurs possibles d'un byte de message (lui aussi compris entre 00 et FF)

On obtient alors pour chaque valeur possible de la clé de chiffrement, une suite de 256 éléments composées de 0 et 1. Ces suites sont toutes différentes et peuvent alors servir de signature pour identifier, en retour, la valeur du byte qui en est à l'origine.

### Etape 2 : collecte des empreintes

Pour déterminer la signature de chaque byte de la clé de chiffrement, on va interroger le script avec chacune des 256 possibilités.

Ainsi pour le 1er byte, on va soumettre tous les messages compris entre :
```
00000000000000000000000000000000
FF000000000000000000000000000000
```

On collecte les différentes valeurs ainsi obtenues.
Elles sont toutes comprises entre 0 et 16, puisque chacun des 16 éléments du tableau `leak_buf` vaut 0 ou 1.

Afin de supprimer les valeurs parasites liées aux 15 autres bytes, on détermine la valeur minimale ainsi obtenue. Cette valeur sera utilisée comme 0 de référence. En prenant cette nouvelle référence, on obtient alors une suite de 0 et 1, qui n'est autre que la signature du 1er byte de la clé de chiffrement.

Grâce à la prise d'empreintes réalisée lors de la 1ère étape, on peut donc déterminer la valeur correspondante du 1er byte de la clé de chiffrement.

On procède de la même façon pour retrouver le 2ème byte de la clé de chiffrement, on soumettant les messages compris entre :
```
00000000000000000000000000000000
00FF0000000000000000000000000000
```

Et ainsi de suite pour les 14 bytes suivants.

Cette solution est implémentée dans le script [`encrypt-reverse-v1.py`](encrypt-reverse-v1.py)

```bash
# Lancement en local
./encrypt-reverse-v1.py

# Lancement en distant
./encrypt-reverse-v1.py REMOTE
```

### Etape 3 : parallélisation de la collecte

Si la solution fonctionne en local, il s'avère qu'en distant, avec la latence réseau induite, le décodage ne peut aboutir avant les 15 minutes imparties (et donc la génération d'un nouveau secret)

J'ai donc bricolé une 2ème version, ne traitant que 4 bytes. Au lancement on précise juste l'indice du 1er byte à traiter.

Cette solution est implémentée dans le script [`encrypt-reverse-v2.py`](encrypt-reverse-v2.py)

Il suffit ensuite de lancer 4 instances en //, et de concaténer les 4 morceaux pour obtenir la clé complète :
```bash
# Pour en lancement en local
./encrypt-reverse-v2.py START=0
./encrypt-reverse-v2.py START=4
./encrypt-reverse-v2.py START=8
./encrypt-reverse-v2.py START=12

# Pour en lancement en distant
./encrypt-reverse-v2.py REMOTE START=0
./encrypt-reverse-v2.py REMOTE START=4
./encrypt-reverse-v2.py REMOTE START=8
./encrypt-reverse-v2.py REMOTE START=12
```
