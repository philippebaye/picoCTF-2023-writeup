# repetitions

## Enoncé
Catégorie : [General Skills](../)

Points : 100

Tags : `base64`

Description :
> Can you make sense of this file?  
> Download the file here.

Hints :
1. Multiple decoding is always good.


## Approche

Le fichier `enc_flag` fourni est un fichier texte, dont le contenu semble encodé en base64.


## Solution

Comme indiqué dans les indices, le contenu est encodé plusieurs fois. On effectue donc séquentiellement plusieurs décodages (en l'occurrence 6 fois) jusqu'à obtenir un texte en clair.
```bash
$ base64 -d <<< VmpGU1EyRXlUWGxTYmxKVVYwZFNWbGxyV21GV1JteDBUbFpPYWxKdFVsaFpWVlUxWVZaS1ZWWnVhRmRXZWtab1dWWmtSMk5yTlZWWApiVVpUVm10d1VWZFdVa2RpYlZaWFZtNVdVZ3BpU0VKeldWUkNkMlZXVlhoWGJYQk9VbFJXU0ZkcVRuTldaM0JZVWpGS2VWWkdaSGRXCk1sWnpWV3hhVm1KRk5XOVVWVkpEVGxaYVdFMVhSbWxSV0VKVlZXcEthbVF4WkhOV2JUbHBDazFFVmtsV2JYUnpZVVpLU0dWRlZsaGkKYlRrelZERldUMkpzUWxWTlJYTkxDZz09Cg== | base64 -d |  base64 -d | base64 -d | base64 -d | base64 -d

picoCTF{base64_n3st3d_dic0d!n8_d0wnl04d3d_xxxxxxxx}
```
