import os,sys

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

APP_FOLDER = os.path.dirname(os.path.realpath(sys.argv[0]))

for i in languages:
    full_path = os.path.join(APP_FOLDER, languages[i])
    with open(full_path) as f:
        for line in f:
            words[i].append(line.replace("\n","")) 

full_path = os.path.join(APP_FOLDER, "echantillon.txt")
file = open(full_path)
text = file.read().replace("\n", " ")
file.close()

for lang in range(len(matches)):
    for word in words[i]:
        if word in text :
            matches[lang][1] += 1
        
for i in range(len(matches)):
    print(matches[i][1])