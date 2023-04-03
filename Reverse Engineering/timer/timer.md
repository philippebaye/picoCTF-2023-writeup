# timer

## Enoncé
Catégorie : [Reverse Engineering](../)

Points : 100

Tags : `android`

Description :
> You will find the flag after analysing this apk  
> Download here.

Hints :
1. Decompile
2. mobsf or jadx


## Approche

On dispose d'une archive Android `timer.apk`.

Le flag est caché parmi les fichiers constituant l'archive.


## Solution

Le flag est présent dans différents fichiers :
* AndroidManifest.xml
* classes3.dex
* ...
