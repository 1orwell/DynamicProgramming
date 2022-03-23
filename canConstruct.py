#work in progress
#returning False when should return True

def canConstruct(target, wordBank):

    # if we have reached a successful base case, return True
    if target == "":
        possible = True
        return possible

    """
    first_letter_check = False

    #check the first letter of each word in the word bank
    #if none of these match the first letter of the target
    #return False
    for word in wordBank:
        first_letter = word[0]
        if first_letter == target[0]:
            first_letter_check = True
    if first_letter_check == False:
        possible = False
        return possible
    """

    for word in wordBank:
        match = True
        target_len = len(target)
        word_len = len(word)
        #if the word in the word bank is longer than the target
        # move onto the next word
        if word_len > target_len:
            continue
        #iterate through each character in the word from the word bank
        for index in range(0, word_len):
            #if the corresponding characters do no match
            #set match to False
            if target[index] != word[index]:
                match = False
        # if match never gets set to False, that means word is a subset of target
        if match == True:
            #remove word from beginning of target
            new_target = target[word_len:]
            if canConstruct(new_target, wordBank) == True:
                return True

    return False
        
    
        
    
result = canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"])
print(result)

result = canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])
print(result)