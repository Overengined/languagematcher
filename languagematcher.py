import os,sys

#initialises vars
languages = {
    "en":"en.txt",
    "fr":"fr.txt"
}

words = {
    "en":[],
    "fr":[]
}

matches = [
    ["en",0],
    ["fr",0]
]

#this piece of code allows the program to work in all possible directories, as lon a sys is present on the system
#it creates a root path wich is the global path of the program's folder
APP_FOLDER = os.path.dirname(os.path.realpath(sys.argv[0]))

#we use the root path and a loop to gather all the dictionnaries entries
print("reading dictionnaries...")
for i in languages:
    full_path = os.path.join(APP_FOLDER, languages[i])
    with open(full_path) as f:
        for line in f:
            words[i].append(line.replace("\n","")) 

#
print("reading text...")
full_path = os.path.join(APP_FOLDER, "echantillon.txt")
file = open(full_path)
text = file.read().replace("\n", " ")
file.close()

#
# for lang in range(len(matches)):
#     for word in words[i]:
#         if word in text :
#             print(word)
#             matches[lang][1] += 1
print("counting matches...")
for testedlang in range(len(matches)):
    for wordoftext in text:
        if wordoftext in words[i]:
            matches[testedlang][1]+=1

for i in range(len(matches)):
    print(matches[i][1])
input("")
