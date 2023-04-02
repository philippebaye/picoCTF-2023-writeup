# useless

## Enoncé
Catégorie : [General Skills](../)

Points : 100

Tags : `man`

Description :
> There's an interesting script in the user's home directory  
> The work computer is running SSH. We've been given a script which performs some basic calculations, explore the script and find a flag.  
> Hostname: `saturn.picoctf.net`  
> Port:     `xxxxx`  
> Username: `picoplayer` 
> Password: `xxxxx`


## Approche

Les fichiers disponibles dans le HOME directory du user `picoplayer` sont les suivants :
```bash
picoplayer@challenge:~$ ls -al
total 16
drwxr-xr-x 1 picoplayer picoplayer   20 Mar 18 20:07 .
drwxr-xr-x 1 root       root         24 Mar 16 02:30 ..
-rw-r--r-- 1 picoplayer picoplayer  220 Feb 25  2020 .bash_logout
-rw-r--r-- 1 picoplayer picoplayer 3771 Feb 25  2020 .bashrc
drwx------ 2 picoplayer picoplayer   34 Mar 18 20:07 .cache
-rw-r--r-- 1 picoplayer picoplayer  807 Feb 25  2020 .profile
-rwxr-xr-x 1 root       root        517 Mar 16 01:30 useless
```

Le fichier `useless` est un script `bash` qui ne fait rien de particulier.


## Solution

A tout hasard, en exploitant le tag associé au challenge, on consulte le `man` pour ce script :
```bash
picoplayer@challenge:/etc$ man useless

useless
     useless, -- This is a simple calculator script

...

Authors
     This script was designed and developed by Cylab Africa

     picoCTF{us3l3ss_ch4ll3ng3_3xpl0it3d_xxxx}
```
