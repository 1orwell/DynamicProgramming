#why are some lists returned twice?
result = []

def allConstruct(target, wordBank):
    if target == "":
        return([[]])

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
            suffix_ways = allConstruct(new_target, wordBank)
            #target_ways = map(lambda x: x.insert(0, word), suffix_ways)
            # the above line didn't work as insert does not return a value
            for way in suffix_ways:
                way.insert(0, word) 
            print("target ways are: ")
            for way in suffix_ways:
                print(way)
            # "spread out" the suffix_ways so we keep a 2D array
            result.append(*suffix_ways)

    return result


#result = allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"])
#print(result)
result = allConstruct("abc", ["ab", "c", "cd", "abc"])
print(result)