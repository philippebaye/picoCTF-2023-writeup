# Safe Opener 2

## Enoncé
Catégorie : [Reverse Engineering](../)

Points : 100

Tags : 

Description :
> What can you do with this file?  
> I forgot the key to my safe but this file is supposed to help me with retrieving the lost key. Can you help me unlock my safe?

Hints :
1. Download and try to decompile the file.


## Approche

Le fichier `SafeOpener.class` mis à disposition correspond à du bytecode JAVA.

Le flag y est caché dedans.


## Solution

Ici, il n'est pas nécessaire de décompiler la classe. On peut juste rechercher les chaînes de caractères contenant `picoCTF`, en éditant le fichier directement ou via `strings` :
```bash
{ picoCTF_2023 }  » strings SafeOpener.class| grep picoCTF

,picoCTF{SAf3_0p3n3rr_y0u_solv3d_it_xxxxxxxx}
```
