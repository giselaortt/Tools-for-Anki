import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://www.verbformen.pt/declinacao/substantivos/?w=studium"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('p')
for tag in tags:
    #if("vStm rCntr" in tag):
    print(tag)


'''
<p class="vStm rCntr">
<b><i></i>Studium<i>s</i></b>
·
<b><i></i>Studi<u>en</u><i></i></b>⁰


<p class="vStm rCntr">
<b><i></i>Kenntnis<i></i></b>
·
<b><i></i>Kenntnis<i>se</i></b>
'''