# Special

## Enoncé
Catégorie : [General Skills](../)

Points : 300

Tags : `bash` `ssh`

Description :
> Don't power users get tired of making spelling mistakes in the shell? Not anymore! Enter Special, the Spell Checked Interface for Affecting Linux. Now, every word is properly spelled and capitalized... automatically and behind-the-scenes! Be the first to test Special in beta, and feel free to tell us all about how Special streamlines every development process that you face. When your co-workers see your amazing shell interface, just tell them: That's Special (TM)  
> Start your instance to see connection details.  
> `ssh -p xxxxx ctf-player@saturn.picoctf.net`  
> The password is `xxxxx`

Hints :
1. Experiment with different shell syntax


## Approche

Une fois connecté au serveur on essaie diverses commandes, mais celles-ci sont modifiées avant leurs interprétations.

Il faut trouver un moyen d'éviter ce comportement.

## Solution

En SHELL, classiquement `\` est utilisé comme caractère d'échappement.

On essaie de faire appel à `ls` en échappant chaque caractère, sans succès :
```bash
Special$ \l\s
Plus
sh: 1: Plus: not found
```

Que se passe-t-il si on utilise le chemin absolu à savoir `/usr/bin/ls` :
```bash
Special$ /usr/bin/ls
Absolutely not paths like that, please!
```

Et en combinant les 2 techniques (chemin absolu + échappement) :
```bash
Special$ \/u\s\r/\b\i\n\/l\s
\/u\s\r/\b\i\n\/l\s
blargh
```

Cela semble fonctionner. On renouvelle l'expérience avec `/usr/bin/sh` :
```bash
Special$ \/u\s\r/\b\i\n/\s\h
\/u\s\r/\b\i\n/\s\h
$
```

Maintenant qu'on a réussi à s'échapper, on peut utiliser les commandes normales :
```
$ ls -al
total 0
drwxr-xr-x 1 ctf-player ctf-player 20 Mar 18 21:56 .
drwxr-xr-x 1 root       root       24 Mar 16 02:10 ..
drwx------ 2 ctf-player ctf-player 34 Mar 18 21:56 .cache
drwxr-xr-x 2 ctf-player ctf-player 22 Mar 16 02:10 blargh

$ cd blargh

$ ls
flag.txt

$ cat flag.txt
picoCTF{5p311ch3ck_15_7h3_w0r57_xxxxxxxx}
```
