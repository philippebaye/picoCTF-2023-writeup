# Ready Gladiator 1

## Enoncé
Catégorie : [Reverse Engineering](../)

Points : 200

Tags : `CodeWars`

Description :
> Can you make a CoreWars warrior that wins?  
> Your opponent is the Imp. The source is available here. If you wanted to pit the Imp against himself, you could download the Imp and connect to the CoreWars server like this:  
> `nc saturn.picoctf.net xxxxx < imp.red`  
> To get the flag, you must beat the Imp at least once out of the many rounds.

Hints :
1. You may be able to find a viable warrior in beginner docs


## Approche

Le guide https://vyznev.net/corewar/guide.html fournit des exemples intéressants de Warriors.


## Solution

On s'appuie sur celles du Nain : https://vyznev.net/corewar/guide.html#start_dwarf

La soumission des instructions suivantes permet de résoudre le challenge :
```
;assert 1
add #4, 3
mov 2, @2
jmp -2
dat #0, #0
end
```

Le résultat du duel est le suivant :
```
Rounds: 100
Warrior 1 wins: 30
Warrior 2 wins: 0
Ties: 70
You did it!
picoCTF{1mp_1n_7h3_cr055h41r5_xxxxxxxx}
```
