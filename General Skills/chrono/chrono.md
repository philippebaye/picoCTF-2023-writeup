# chrono

## Enoncé
Catégorie : [General Skills](../)

Points : 100

Tags : `linux`

Description :
> How to automate tasks to run at intervals on linux servers?  
> Use `ssh` to connect to this server:  
> Server: `saturn.picoctf.net`  
> Port: `xxxxx`  
> Username: `picoplayer`  
> Password: `xxxxx`


## Approche

Sous linux, l'outil pour automatiser des tâches est `cron`.


## Solution

On consulte donc le fichier par défaut `/etc/crontab` et on y trouve le flag :
```bash
picoplayer@challenge:~$ cat /etc/crontab
# picoCTF{Sch3DUL7NG_T45K3_L1NUX_xxxxxxxx}
```
