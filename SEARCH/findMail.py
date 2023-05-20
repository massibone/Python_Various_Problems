import re
# The RegEx library
#
# our regular expression (to find e-mails)
# and text to search
#
regex = '\s[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}[\s]'
text = """This is example of text with x@y.z embedded e-mails
that we'll use as@gmail.com
line with no addresses
others@insail.two valid email@addresses.com
The re module is awonderful@thing."""
print('** Search text ***\n'+text)
print('** Regex ***\n'+regex+'\n***')
#
#

utext = text.upper()
#
#
# perform a search (any emails found?)
s = re.search(regex, utext)
if s:
    print('*** At least one email found "'+s.group()+'"')
#
# now, find all matches
#
m = re.findall(regex, utext)
if m:
    for match in m:
        print('Match found', match.strip())
