import json
from difflib import get_close_matches
data=json.load(open("data.json"))
word=input("enter word,you want to search")
w=word.lower()
def dictnary(w):
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys()))>0:
        print("did u mean %s instead" %get_close_matches(w,data.keys())[0])
        decide=input("press y for yes or n for no")
        if decide=="y":
            return data[get_close_matches(w,data.keys())[0]]
        elif decide=="n":
            return("the word did not exist")
        else:
            return("you have enter wrong input ")
    else:
        print("please check the spelling")

output=dictnary(w)
if type(output)==list:
    for item in output:
        print(item)
else:
    print(output)