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

progressionhelper = 0
progressionstatus = 0

def progression():
    '''
    fonction gérant l'affichage de la progression
    '''
    global text
    global progressionhelper
    global progressionstatus
    if progressionhelper >= len(text)/10 :
        progressionhelper = 0
        print(round((progressionstatus/len(text))*100,0),"% done", end="\r")

    
def matchcount():
    '''
    fonctions permettant de dénombrer  
    '''
    global matches
    global words
    global progressionhelper, progressionstatus
    for wordoftext in text:
        if wordoftext in words["en"]:
            matches[0][1]+=1
        if wordoftext in words["fr"]:
            matches[1][1]+=1
        progression()
        progressionhelper += 1
        progressionstatus += 1



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
text = file.read().replace("\n"," ")
file.close()
text = text.split(" ")

print("counting matches...")
matchcount()

print("")
print("en :",matches[0][1])
print("fr :",matches[1][1])

if matches[0][1] > matches[1][1] :
    print("votre texte est écrit en Anglais, la langue de Shakespeare !")
else:
    print("votre texte est écrit en Francais, la langue de Molière !")

input("")
