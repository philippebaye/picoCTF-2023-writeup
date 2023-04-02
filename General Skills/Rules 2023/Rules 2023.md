# Rules 2023

## Enoncé
Catégorie : [General Skills](../)

Points : 100

Tags : 

Description :
> Read the rules of the competition and get a little bonus!  
> Rules (https://picoctf.org/competitions/2023-spring-rules.html)

Hints :
1. Ctrl-F will not work


## Approche

Comme indiqué, on se rend sur la page expliquant les règles de l'épreuve.


## Solution

Au milieu du texte, une image avec le flag est présente.

Si on ouvre le DOM de la page, on retrouve également le flag, en tant qu'attribut `alt` de cette même image :
```html
<img src="/img/rules_fl23.png" alt="picoCTF{h34rd_und3r5700d_4ck_xxxxxxxx}">
```
