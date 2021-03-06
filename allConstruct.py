#why are some lists returned twice?


def allConstruct(target, wordBank, memo = None):
    if not memo:
        memo = {}

    result = []

    if target == "":
        return([[]])

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
            suffix_ways = allConstruct(new_target, wordBank)
            for way in suffix_ways:
                print("inserting word: " + word + " at start of list: " + str(way))
                way.insert(0, word) 
                print("The result is " + str(way))
            result.extend(suffix_ways)
            memo[target] = result

    memo[target] = result
    return result

result = allConstruct("ab", ["ab", "a"])
print(result)

#result = allConstruct("abc", ["ab", "c", "cd", "abc"])
#print(result)

#result = allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"])
#print(result)
