def is_isogram(string):
    #creating a set of letters in the string
    letters = set()
    string = string.lower()
    
    #iterate over character in word
    for character in string:
        
        if not character.isalpha():
            continue
        #if find character already remembered return false
        if character in letters:
            return False
        #remeber each letter we iterate over
        letters.add(character)
    
