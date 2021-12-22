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
            words[i].append(line) 

full_path = os.path.join(APP_FOLDER, "echantillon.txt")
file = open(full_path)
inputedtext = file.read().replace("\n", " ")
file.close()

