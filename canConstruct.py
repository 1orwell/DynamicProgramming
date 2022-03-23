def canConstruct(target, wordBank, memo = {}):

    # if we have reached a successful base case, return True
    if target == "":
        return True

    if target in memo:
        return memo[target]

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
            if canConstruct(new_target, wordBank, memo) == True:
                memo[target] = True
                return True

    memo[target] = False
    return False
        
result = canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"])
print(result)

result = canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])
print(result)

result = canConstruct("eeeeeeeeeeeeeeeelllllll", ["e", "ee", "eeeee", "l"])
print(result)

result = canConstruct("eeeeeeeeeeeeeeeelllllllw", ["e", "ee", "eeeee", "l"])
print(result)
