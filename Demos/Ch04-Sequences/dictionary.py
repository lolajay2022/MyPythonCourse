
spanish_english = {
  "uno": "one",
  "dos": "two",
  "tres": "three"
}
print(spanish_english)
print(spanish_english["dos"])

spanish_english["quatro"]="four"
print(spanish_english)

for word in spanish_english:
    print(word, "means", spanish_english[word])

for x in spanish_english.values():
  print(x)

for x, y in spanish_english.items():
  print(x, y)

if "tres" in spanish_english:
    print("Tres is in this dictionary")

print(len(spanish_english)) 

spanish_english["gatto"]="cat"
spanish_english["hola"]="hello"
print(spanish_english)

#copy dictionaries
espanol = spanish_english.copy()
espanol_ingles = dict(spanish_english)
print ('espanol', espanol == spanish_english)
print ('espanol_ingles', espanol_ingles)

#remove specified item by key
spanish_english.pop("uno") 
#removes last added item before 3.7 was random
spanish_english.popitem() 
del spanish_english["dos"]
print(spanish_english)

spanish_english.clear()
print(spanish_english)

del spanish_english
del spanish_english #throws an error


