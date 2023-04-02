# hideme

## Enoncé
Catégorie : [Forensics](../)

Points : 100

Tags : `steganography`

Description :
> Every file gets a flag.  
> The SOC analyst saw one image been sent back and forth between two people. They decided to investigate and found out that there was more than what meets the eye here.


## Approche

On cherche quelque chose de caché dans le fichier `flag.png` fourni.


## Solution

L'utilisation de `binwalk` montre qu'un fichier `secret/flag.png` y est caché :
```txt
$ binwalk flag.png

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 512 x 504, 8-bit/color RGBA, non-interlaced
41            0x29            Zlib compressed data, compressed
39739         0x9B3B          Zip archive data, at least v1.0 to extract, name: secret/
39804         0x9B7C          Zip archive data, at least v2.0 to extract, compressed size: 2997, uncompressed size: 3152, name: secret/flag.png
43036         0xA81C          End of Zip archive, footer length: 22
```

Une fois extrait, il suffit d'ouvrir l'image pour lire le flag.
