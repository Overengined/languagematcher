import os,sys

#initialises vars
languages = {
    "en":"en.txt",
    "fr":"fr.txt",
    "es":"es.txt"
}

words = {
    "en":[],
    "fr":[],
    "es":[]
}

matches = [
    ["en",0],
    ["fr",0],
    ["es",0]
]

progressionstatus = 0

# read the name of the file from the argument
try:
    fileToRead = str(sys.argv[1])
    
except: #if the user specified nothing
    print("no file specified, aborting")
    exit()

def progression():
    '''
    function managing progress display
    '''
    global text
    global progressionstatus
    print(round((progressionstatus/len(text))*100,0),"% done", end="\r")


    
def matchcount():
    '''
    function allowing match count 
    '''
    global text
    global matches
    global words
    global progressionstatus
    for wordoftext in text:
        if wordoftext in words["en"]:
            matches[0][1]+=1
        if wordoftext in words["fr"]:
            matches[1][1]+=1
        if wordoftext in words["es"]:
            matches[2][1]+=1
        progression()
        progressionstatus += 1



#this piece of code allows the program to work in all possible directories, as lon a sys is present on the system
#it creates a root path wich is the global path of the program's folder
APP_FOLDER = os.path.dirname(os.path.realpath(sys.argv[0]))

#we use the root path and a loop to gather all the dictionnaries entries
print("reading dictionnaries...")
for i in languages:
    full_path = os.path.join(APP_FOLDER, languages[i])
    with open(full_path, encoding="utf-8") as file:
        for line in file:
            words[i].append(line.replace("\n","")) 

#
print("reading text...")
full_path = os.path.join(APP_FOLDER, fileToRead)
file = open(full_path, encoding="utf-8")
text = file.read().replace("\n"," ")
file.close()
text = text.split(" ")

print("counting matches...")
matchcount()

print("/!\ 100 % done")
print("en :",matches[0][1])
print("fr :",matches[1][1])
print("es :",matches[2][1])

if matches[0][1] > matches[1][1] and matches[0][1] > matches[2][1] :
    print("the text is written in English")
elif matches[1][1] > matches[0][1] and matches[1][1] > matches[2][1]:
    print("The text is written in French")
elif matches[2][1] > matches[0][1] and matches[2][1] > matches[2][1]:
    print("The text is written in Spanish")

input("")
