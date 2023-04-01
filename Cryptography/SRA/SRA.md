# SRA

## Enoncé
Catégorie : [Cryptography](../)

Points : 400

Tags : `rsa`

Description :
> I just recently learnt about the SRA public key cryptosystem... or wait, was it supposed to be RSA? Hmmm, I should probably check...  
> Connect to the program on our server: `nc saturn.picoctf.net xxxxx`  
> Download the program: `chal.py`


## Approche

L'analyse du fichier `chal.py` fourni montre que celui-ci met en oeuvre l'algorithme RSA.  
Voici la correspondance entre les 2 algorithmes :

| Etape | Algorithme `chal.py` | Algorithme RSA 
| :-: | - | - 
| 1 | Génération d'une chaine aléatoire `pride` composée de 16 caractères alphanumériques. Il s'agit du message secret en clair à trouver. | Message en clair `M`
| 2 | Obtention de 2 nombres premiers aléatoires de 128 bits `gluttony` et `greed` | On choisit 2 nombres premiers `p` et `q`
| 3 | On calcule `lust` : $lust = gluttony \cdot greed$ | On détermine le module de chiffrement `n` : $n = p \cdot q$
| 4 |  | On détermine l'indicatrice d'Euleur `phi(n)` : $\phi(n) = (p-1)\cdot(q-1)$
| 5 | On prend 65537 comme valeur pour `sloth` | On choisit l'exposant de chiffremet `e` premier avec `phi(n)`. Classiquement on prend $e = 65537 = 2^{16} + 1$ (qui est le Nombre de Fermat $F_4$).
| 6 | On détermine `envy` comme inverse modulaire de `sloth` vis à vis de $(gluttony - 1) \cdot (greed - 1)$ | On détermine l'exposant de déchiffrement `d` en tant qu'inverse modulaire de `e` vis-à-vis de `phi(n)` : $d \cdot e \equiv 1\ [\phi(n)]$
| 7 | On calcule `anger` par exponentiaton modulaire de `pride` (puissance `sloth`,  modulo `lust`) | Le message chiffré `C` est déterminé par : $C \equiv M^{e} (modulo\ n)$


2 informations sont fournies : `anger` (i.e. le secret chiffré) et `envy` (i.e. l'exposant de déchiffrement)  
Pour obtenir le flag il faut retrouver le secret `pride`


## Solution

### Etape 1 : décomposition en facteurs premiers

Par rapport à l'algorithme RSA, on dispose donc des 3 informations suivantes :
- l'exposant de chiffrement `e` qui est fixe : $e = 65537$
- l'exposant de déchiffrement `d`
- le message chiffré `C`

`d` étant l'inverse modulaire de `e` vis-à-vis de `phi(n)` (i.e. $\ d \cdot e \equiv 1\ [\phi(n)]$ ), on a donc : 

$$ \exists\ k\ |\ d \cdot e = 1 + k \cdot \phi(n) <=> \ d \cdot e -1 =k \cdot (p-1) \cdot (q-1) $$

Connaissant `d` et `e`, on connait donc $k \cdot (p-1) \cdot (q-1)$

Les valeurs n'étant pas trop grande, il est possible de décomposer celui-ci en produit de facteurs premiers, en un temps raisonnablement rapide sans nécessiter une puissance de calcul démesurée.

$$d \cdot e - 1 = \prod_{i=0}^{m} P_{i} \ => \ prime\\_factors = \{P_{0}, P_{1}, ..., P_{m}\}$$

NB : La liste des facteurs premiers ainsi obtenues peut contenir des doublons.

On a donc pour `p` :
$$(p-1) = \prod P_{j} \ => \ p = 1 + \prod P_{j} $$

Et de façon identique pour `q` :
$$q = 1 + \prod P_{k} $$

---

### Etape 2 : identification des combinaisons de facteurs premiers permettant de retrouver des `p` et `q` potentiels

On cherche donc les combinaisons des facteurs premiers qui multipliés entre eux + 1 donnent un nombre premier. En complément :
- on retient la combinaison uniquement si le nombre premier est un nombre de 128 bits (cf. étape 2 de l'algorithme).
- on prend uniquement les combinaisons d'au moins 2 facteurs et au plus (taille de la liste des facteurs -2).

Pourquoi au moins 2 facteurs ? Les facteurs étant premiers, ils sont :
- soit imper. Lorsqu'on ajoute 1 la somme devient paire, et ne peut donc pas être un nombre premier
- soit égal à 2. Lorsqu'on ajoute 1 la somme (i.e. 3) est un nombre < 128 bits.

Contrainte supplémentaire, un facteur ne peut pas à la fois servir pour définir `p` et `q`.  
Donc si :  

$$prime\\_factors\\_p = \{P_{j_0}, P_{j_1}, ..., P_{j_{p}}\}$$

$$prime\\_factors\\_q = \{P_{k_0}, P_{k_1}, ..., P_{k_{q}}\}$$

Alors :
$$prime\\_factors\\_p + prime\\_factors\\_q \subset prime\\_factors$$

Comme `prime_factors_p` est composé d'au moins 2 éléments, `prime_factors_q` contient au plus (nombre d'éléments de `prime_factors` - 2). Et inversement.  
Donc :
$$2 \le count(prime\\_factors\\_p) \le count(prime\\_factors) - 2$$
$$2 \le count(prime\\_factors\\_q) \le count(prime\\_factors) - 2$$

Si on définit : 
* `min_count` comme étant le nombre d'éléments de la plus petite combinaison des facteurs premiers trouvée `prime_factors_p`,

$$min\\_count = min(prime\\_factors\\_p_{0}, prime\\_factors\\_p_{1}, prime\\_factors\\_p_{x})$$

* `max_count` comme étant le nombre d'éléments de la plus grande combinaison possible des facteurs premiers `prime_factors_q`

$$max\\_count = max(prime\\_factors\\_q_{0}, prime\\_factors\\_q_{1}, prime\\_factors\\_q_{y})$$

On a la relation :
$$max\\_count \le count(prime\\_factors) - min\\_count$$

Donc chaque combinaison des facteurs premiers doit valider la contrainte :
$$min\\_count \le count(prime\\_factors\\_p) \le count(prime\\_factors) - min\\_count$$
$$min\\_count \le count(prime\\_factors\\_q) \le count(prime\\_factors) - min\\_count$$

---

### Etape 3 : identification des couples (`p`, `q`) candidats

Maintenant que l'on a écarté un certain nombre de combinaison de facteurs premiers, on   doit trouver des couples de combinaisons qui associées permettent d'avoir un `p` et `q`.

On essaie les différentes associations possibles, sachant qu'elles doivent répondre (pour rappel) à la contrainte suivante :
$$prime\\_factors\\_p + prime\\_factors\\_q \subset prime\\_factors$$

A partir des couples (`p`, `q`) identifiés, on essaie de déchiffrer le message chiffré `C` et de retrouver le message en clair `M`.  
Pour rappel de l'algorithme RSA, on a :
$$M \equiv C^{d}\ (modulo\ n) \ avec \ n = p \cdot q$$

`C` et `d` étant fournis, on teste donc tous les couples (`p`, `q`) trouvés précédemment.

Parmi les messages déchiffrés obtenus, on ne retient que ceux contenant uniquement des caractères alphanumériques. Pour rappel, le secret `pride` a été généré à partir d'une suite aléatoire de caractères alphanumériques.

Reste plus qu'à soumettre le secret ainsi obtenu pour obtenir le flag.

---

### Etape 4 : implémentation de l'algorithme correspondant

Voici l'implémentation réalisée : [chall-reverse.py](./chall-reverse.py)

---

### Etape 5 : exécution 

1. Connexion au serveur et récupération de `C` et `d` :
```bash
{ picoCTF_2023 }  » nc saturn.picoctf.net xxxxx
anger = 53669793913171408732196856528742384141562153068446118765052227063373349441805
envy = 54195268562551666854582277080820475168115232074416582313302921028869342214929
vainglory?
> 
```

2. Utilisation de `C` et `d` pour retrouver `M` :
```bash
{ picoCTF_2023 }  » python3 chall-reverse.py
anger ? > 53669793913171408732196856528742384141562153068446118765052227063373349441805
envy ? > 54195268562551666854582277080820475168115232074416582313302921028869342214929
prime_factors = [2, 2, 2, 2, 3, 3, 29, 31, 71, 71, 89, 2437, 49875181, 905936487457, 9425132741803, 58924214417773777974784486741974049]
possible vainglory : Gl3LEpGNmsBbhL9E
possible vainglory : Gl3LEpGNmsBbhL9E
```

3. Soumission du secret `M` et obtention du flag
```bash
vainglory?
> Gl3LEpGNmsBbhL9E
Gl3LEpGNmsBbhL9E
Conquered!
picoCTF{7h053_51n5_4r3_n0_m0r3_xxxxxxxx}
```
