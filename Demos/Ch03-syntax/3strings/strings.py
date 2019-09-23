
a = 'spam eggs'  # single quotes
b = 'doesn\'t'  # use \' to escape the single quote...
c = "doesn't"  # ...or use double quotes instead
d = '"Yes," they said.'
e = "\"Yes,\" they said."
f = '"Isn\'t," they said.'

print(a,b,c,d,e,f);

g,h = '''
This string is on 
multiple lines
it's quotes 
are on either side.
''', """
Your is a possessive – it means something belongs to you.
You're is short for "you are."
"""

print (g,h);

h2 = '''
here are two quotes ''
'''

print(h2)

i = 'Im \'really\' happy to be here!'
print (i)



("spam " "eggs") == "spam eggs"
("spam" "eggs") == "spameggs"


first = 'Hello'
second = 'World'
print (first + second)

character = 'BeetleJuice'
print(character*3)

verticalTab = '\vUp \vup \vaway!'
print(verticalTab)

horizontalTab = '\tUp \tup \taway!'
print(horizontalTab)

longWord = 'Supercalisfragilisticexpialadocious';
print(len(longWord))


pattern_to_match = r"\w+\s+\w+"
print(pattern_to_match)
path = r"C:\course\200Python\Demos\Ch03"
print(path)
message = r"please put a tab character (\t) for each column"
print(message)

escaped = 'abc\a'
print(escaped)

# year = 1989
# phrase = "Python was created in " + year
# print(phrase)

year = 1989
phrase = "Python was created in {} " 
print(phrase.format(year))


price = 12.95
qty = 11
id = 239
myorder = "Item {1} costs {2} and there are {0} left"
print(myorder.format(qty, id, price))


# movie_title = 'The Meaning of Life'

# movie_title.format()