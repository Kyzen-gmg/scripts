#!/usr/bin/env python3
'''
1st way:
1. Regex/wildcard registries

Issue:
1. Not allowed or restricted.....


2nd way:
1. PRINT all chars of valid domain string (^[0-9A-Za-z._-]+$) onto a list   
2. Iterate over the list of char while inserting KEYWORD into the string while simultaenously subtracting the len(KEYWORD) from the string to keep it valid

Problem:
1. Bruteforcing whois/dns servers is not a great idea......... to be continued...
'''







'''
3rd way:
curl, wget, python request websites to get results back.

Issue:
1. <h1>Forbidden Access</h1>
<p>Oops, something went wrong with your request! Please only submit content through the web forms with a current browser.</p>

```
└─# curl -i -s -k -X $'GET' \
    -H $'Host: www.namedroppers.com' -H $'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0' -H $'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H $'Accept-Language: en-US,en;q=0.5' -H $'Accept-Encoding: gzip, deflate' -H $'Upgrade-Insecure-Requests: 1' -H $'Sec-Fetch-Dest: document' -H $'Sec-Fetch-Mode: navigate' -H $'Sec-Fetch-Site: none' -H $'Sec-Fetch-User: ?1' -H $'Cache-Control: max-age=0' -H $'Te: trailers' -H $'Connection: close' \
    -b $'tlds=255' \
    $'https://www.namedroppers.com/b/q?adv=1&k=covid&x=23&y=25&exclude=&order=0&min=1&max=63&org=1'
```

```
import requests

# This is in case a site requires an api key
#api_key = os.environ.get('API_KEY')
#api_url = 'https://rhost/page?api_key={}'.format(api_key)

key = input("Enter keyword you'd like to search DNS registries: ")
list_urls = [
"https://www.namedroppers.com/b/q?adv=1&k="+key+"&x=23&y=25&exclude=&order=0&min=1&max=63&org=1"
]

def use_requests(url):

    response = requests.get(url)
    print(response.text)

for url in list_urls:
    use_requests(url)
```
'''