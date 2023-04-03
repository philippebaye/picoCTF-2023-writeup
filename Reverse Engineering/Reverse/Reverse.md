# Reverse

## Enoncé
Catégorie : [Reverse Engineering](../)

Points : 100

Tags : 

Description :
> Try reversing this file? Can ya?  
> I forgot the password to this file. Please find it for me?


## Approche

Le fichier `ret` mis à disposition est un exécutable binaire :
```bash
{ picoCTF_2023 }  » file ret

ret: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=d19709b8777cf6b55ef3d1321b36009454db6920, for GNU/Linux 3.2.0, not stripped
```

Le mot de passe doit être caché dedans.


## Solution

En cherchant les chaines de caractère présentes dans le fichier, on y trouve le flag :
```bash
{ picoCTF_2023 }  » strings ret
/lib64/ld-linux-x86-64.so.2
...
picoCTF{H
3lf_r3v3H
r5ing_suH
cce55fulH
_xxxxxxxH
[]A\A]A^A_
Enter the password to unlock this file:
You entered: %s
Password correct, please see flag: picoCTF{3lf_r3v3r5ing_succe55ful_xxxxxxxx}
Access denied
:*3$"
...
```
