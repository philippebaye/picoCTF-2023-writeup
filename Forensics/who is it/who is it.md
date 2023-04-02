# who is it

## Enoncé
Catégorie : [Forensics](../)

Points : 100

Tags : `email`

Description :
> Someone just sent you an email claiming to be Google's co-founder Larry Page but you suspect a scam.  
> Can you help us identify whose mail server the email actually originated from?  
> Download the email file here. Flag: picoCTF{FirstnameLastname}

Hints :
1. whois can be helpful on IP addresses also, not only domain names.


## Approche

Le fichier `email-export.eml` à disposition contient notamment les informations relatives aux différents intermédaires d'expédition :
```txt
...
Received: by 2002:ab0:638a:0:0:0:0:0 with SMTP id y10csp123720uao;
        Thu, 7 Jul 2022 23:19:48 -0700 (PDT)
...
Received: from mail.onionmail.org (mail.onionmail.org. [173.249.33.206])
        by mx.google.com with ESMTPS id f16-20020a05600c4e9000b003a1947873d6si1882702wmq.224.2022.07.07.23.19.47
        for <francismanzi@gmail.com>
        (version=TLS1_3 cipher=TLS_AES_256_GCM_SHA384 bits=256/256);
        Thu, 07 Jul 2022 23:19:47 -0700 (PDT)
...
Received: from localhost
 by mail.onionmail.org (ZoneMTA) with API id 181dc76dff2000ccee.001
 for <francismanzi@gmail.com>;
 Fri, 08 Jul 2022 06:19:47 +0000
...
```

## Solution

Parmi les intermédiaires, une IP apparaît : `173.249.33.206`

Pour savoir à qui elle correspond, plusieurs possibilités :
* utiliser un outil en ligne (exemple : https://www.whatismyip.com/ip-whois-lookup/)
* utiliser `whois` (comme suggéré dans les Hints)

```bash
whois 173.249.33.206 | grep person
person:         Wilhelm Zwalina
```
