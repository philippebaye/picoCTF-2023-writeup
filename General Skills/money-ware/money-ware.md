# money-ware

## Enoncé
Catégorie : [General Skills](../)

Points : 100

Tags : `osint`

Description :
> Flag format: picoCTF{Malwarename}  
> The first letter of the malware name should be capitalized and the rest lowercase.  
> Your friend just got hacked and has been asked to pay some bitcoins to `1Mz7153HMuxXTuR2R1t78mGSdzaAtNbBWX`. He doesn’t seem to understand what is going on and asks you for advice. Can you identify what malware he’s being a victim of?

Hints :
1. Some crypto-currencies abuse databases exist; check them out!
2. Maybe Google might help.


## Approche

On fait appel à un moteur de recherche sur `1Mz7153HMuxXTuR2R1t78mGSdzaAtNbBWX`


## Solution

Plusieurs articles (exemple : https://bitcoin.fr/alerte-au-ransomware/) indiquent qu'il s'agit de l'adresse d'un compte en Bitcoin qui a été utilisé pour du ransomware, dont le virus était basé sur la souche Petya.
