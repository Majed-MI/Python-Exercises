# matching word from the string(long)

# function detecting matching word and taking two values sentence1 and sentence2
# so it will try to match with two individual sentence and check all
def matchingWords(sentence1,sentence2):
    # words will be splitted by a space and strip means it will ignore extra spaces
    words1 = sentence1.strip().split(" ")
    words2 = sentence2.strip().split(" ")
    # declaring score as 0 when match occurs it will increment
    score = 0
    # for individual word matching with two sentences condition checking and also lowering the case
    for word1 in words1:
        for word2 in words2:
            # print(f"Matching {word1} with {word2}")
            # case sensitivity ignoring
            if word1.lower() == word2.lower():
                # incrementing score when matches found
                score += 1
    # returning the score from the function
    return score

# only applicable when under these function
if __name__ == '__main__':
    # matchingWords("This is good","Python is good")
    sentences = ["Python is a good language","It can run snake game","I am a good Programmer in Python",
                 "Subscribe to Python Channel","Thank you for being with Python"]

    queryString = input("Enter the Query String:\n")
    # declaring scores which will call the matchingWords() and will match with the input query and
    # serially check sentence one by one
    scores = [matchingWords(queryString,sentence) for sentence in sentences]
    # print(scores)
    # declaring sortedSentScore which will make sorting in scores and sentences in decreasing format
    # but reverse=true will do the increasing format and if sentscore does not match with the sentences
    # then it will result 0 otherwise printing the result matched in sorted format
    sortedSentScore = [sentScore for sentScore in sorted(zip(scores,sentences) ,reverse=True)
                       if sentScore[0] != 0]
    # print(sortedSentScore)

    # sortedSentScore length is the found result number
    print(f"{len(sortedSentScore)} results found")
    # for individual item which means matched sentence will be printed
    #and alse how many times it matched will show too
    for score,item in sortedSentScore:
        print(f"\"{item}\" with a score of {score}")