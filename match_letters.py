#A character class is indicated by square brackets and matches one character among those specified between the brackets. For example, ma[dnt] matches either mad, man, or mat.
#Modify your pattern to match a w followed by either h or a.

import re
pattern = 'w[ha]'
quote = 'Not all those who wander are lost.'
print(re.findall(pattern, quote))

'''
output
['wh', 'wa']
'''

pattern = 'l+'
quote = 'Not all those who wander are lost.'
print(re.search(pattern, quote))

'''output
<re.Match object; span=(5, 7), match='ll'>

se metto findall al posto di search mi dà ['ll', 'l']
'''
