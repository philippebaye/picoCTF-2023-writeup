# Ready Gladiator 0

## Enoncé
Catégorie : [Reverse Engineering](../)

Points : 100

Tags : `CodeWars`

Description :
> Can you make a CoreWars warrior that always loses, no ties?  
> Your opponent is the Imp. The source is available here. If you wanted to pit the Imp against himself, you could download the Imp and connect to the CoreWars server like this:  
> `nc saturn.picoctf.net xxxxx` < imp.red

Hints :
1. CoreWars is a well-established game with a lot of docs and strategy
2. Experiment with input to the CoreWars handler or create a self-defeating bot


## Approche

Quelques recherches sur internet nous en apprennent plus sur Core War et le langage de propgrammation Redcode : https://fr.wikipedia.org/wiki/Core_War

On trouve également un tutotiel : https://vyznev.net/corewar/guide.html


## Solution

La soumission des instructions suivantes permet de résoudre le challenge :
```
;assert 1
mov 1, 1
end
```

Le résultat du duel est le suivant :
```
Rounds: 100
Warrior 1 wins: 0
Warrior 2 wins: 100
Ties: 0
You did it!
picoCTF{h3r0_t0_z3r0_4m1r1gh7_xxxxxxxx}
```
