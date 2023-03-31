# ReadMyCert

## Enoncé
Catégorie : [Cryptography](../)

Points : 100

Tags : 

Description :
> How about we take you on an adventure on exploring certificate signing requests  
> Take a look at this CSR file here.

Hints :
1. Download the certificate signing request and try to read it.


## Approche

Le fichier `readmycert.csr` mis à disposition est un CSR (Certificate Signature Request). 
Un CSR est un fichier contenant les informations d'identification du demandeur et sa clé publique.
Il est transmis à une autorité de certification, qui après vérification appose sa signature, permettant ainsi d'obtenir en retour un certificat signé (CRT).

Pour lire le contenu d'un CSR on peut utiliser :
* OpenSSL
* un outil en ligne


## Solution

La lecture du CSR avec OpenSSL peut s'effectuer comme suit :
```txt
openssl req -in readmycert.csr -noout -text
```
Le flag apparaît alors au niveau du Subject :
```
Certificate Request:
    Data:
        Version: 1 (0x0)
        Subject: CN = picoCTF{read_mycert_xxxxxxxx}, name = ctfPlayer
        Subject Public Key Info: rsaEncryption
        ...
```
