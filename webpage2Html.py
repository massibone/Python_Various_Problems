'''
Get a URL from the user. If the user doesn’t
include the http:// part of the URL, the program adds the prefix.
Ask the user for a query string if blank program add
URL from the user .html
The contents can be downloaded if user choose "y"
'''

import requests
from urllib.parse import urlparse
url = input('Web url to fetch:')
urlparts = urlparse(url)
if urlparts[0] == '':
    url = ''.join(('http://', url))
qstring = input('Enter query string:')
if len(qstring) > 0:
    url = '?'.join((url, qstring))
save = input('Save downloaded page to disk [y/n]?')
print('Requesting', url)
try:
    response = requests.get(url)
    if save.lower() == 'y':
        geturl = response.url
        urlparts = urlparse(geturl)
        netloc = urlparts[1]
        if len(netloc) == 0:
            fname = 'save.html'
        else:
            fname = '.'.join((netloc, 'html'))
        print('saving to', fname, '...')
        fp = open(fname, 'w')
        fp.write(response.text)
        fp.close()
    else:
        print(response.text)
except Exception as e:
    print(e.__class__.__name__, e)
