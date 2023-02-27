import nltk
from nltk.corpus import wordnet
nltk.download('wordnet')

def  find_synonyms(word):
        synonyms=[]
        for syn in wordnet.synsets(word):
            for l in syn.lemmas():
                synonyms.append(l.name())
            if synonyms:
                return synonyms[0]
            else:
                return word

def findsynonyms(input):
    tagslist=input["tags"]
    needlist=input["need"]
    endtagslist=[]
    endneedlist=[]

    
    for i in tagslist:
        endtagslist.append(find_synonyms(word=i))
    for i in needlist:
        endneedlist.append(find_synonyms(word=i))

    print(endtagslist)
    print(endneedlist)
    return {"tags":endtagslist, "need":endneedlist}

