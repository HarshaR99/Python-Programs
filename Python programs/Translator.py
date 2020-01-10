# Random translator
# In this language all vowels are replaced by 'g'

def translate(phrase) :
    traslation = ""
    for letter in phrase :
       # this check if any one letter in "AEIOUaeiou" is
        if letter in "AEIOUaeiou":
            if letter.isupper() :
                traslation += 'G'
            else :
                traslation += 'g'
        else :
            traslation += letter
    return traslation

phrase = input("Enter a phrase : ")

print(translate(phrase))