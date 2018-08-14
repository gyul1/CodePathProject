# CodePath Project
import heapq
import random
import getWords


WORDS = getWords.getWords()

def getTotalNumberOfWords():
    return len(WORDS)

def getTotalUniqueWords():
    return len(set(WORDS))

def get20MostFrequentWords():
    frequency_dict = dict()
    for word in WORDS:
        if word.lower() in frequency_dict:
            frequency_dict[word.lower()] += 1
        else:
            frequency_dict[word.lower()] = 1

    frequency_list = []
    for k in frequency_dict:
        frequency_list.append([frequency_dict[k], k])

    heapq._heapify_max(frequency_list)
    return_list = []
    for i in range(20):
        return_list.append(heapq._heappop_max(frequency_list))
        
    return return_list

def get20MostInterestingFrequentWords():
    filter = open("most-common-EnglishWords-100.txt","r")
    filter_words = filter.readlines()

    for i in range(len(filter_words)):
        filter_words[i] = filter_words[i].strip("\n")

    frequency_dict = dict()
    for word in WORDS:
        if word.lower() not in filter_words:
            if word.lower() in frequency_dict:
                frequency_dict[word.lower()] += 1
            else:
                frequency_dict[word.lower()] = 1

    frequency_list = []
    for k in frequency_dict:
        frequency_list.append([frequency_dict[k], k])

    heapq._heapify_max(frequency_list)
    return_list = []
    for i in range(20):
        return_list.append(heapq._heappop_max(frequency_list))

    return return_list



def get20LeastFrequentWords():
    frequency_dict = dict()
    for word in WORDS:
        if word.lower() in frequency_dict:
            frequency_dict[word.lower()] += 1
        else:
            frequency_dict[word.lower()] = 1

    frequency_list = []
    for k in frequency_dict:
        frequency_list.append([frequency_dict[k], k])

    heapq.heapify(frequency_list)

    return_list = []

    while len(return_list) < 20:
        val = heapq.heappop(frequency_list)

        if len(val[1]) >= 5:
            return_list.append([val])


    return return_list



def getFrequencyOfWord(searchWord):

    index = 0
    result = []
    count = 0
    while index < len(WORDS):
        if WORDS[index] == "chapter":
            if index + 1 < len(WORDS):
                index += 1
                try:
                    num = int(WORDS[index])
                    result.append(count)
                    count = 0

                except:

                    index += 1

        if WORDS[index] == searchWord:
            count += 1

        index += 1

    return result[1:]


def getChapterQuoteAppears(q):
    if q == "":
        return "string is empty"
    q = q.split()
    quote = []

    for word in q:
        word = word.replace(".", "")
        word = word.replace(";", "")
        word = word.replace(",", "")
        word = word.replace("_", "")
        word = word.replace("?", "")
        word = word.replace("\"", "")
        word = word.replace("!", "")
        word = word.replace("(", "")
        word = word.replace(")", "")
        word = word.replace(":", "")
        word = word.rstrip("'")
        word = word.lstrip("'")


        quote.append(word.lower())

    index = 0

    while index < len(WORDS):
        if WORDS[index] == "chapter":
            if index + 1 < len(WORDS):
                index += 1
                try:
                    num = int(WORDS[index])
                except:
                    index += 1

        if WORDS[index] == quote[0]:
            q_index = 1
            index += 1
            the_same = True
            while index < len(WORDS) and q_index < len(quote):
                if WORDS[index] != quote[q_index]:
                    the_same = False
                    break

                index += 1
                q_index += 1

            if the_same:
                return num

        index += 1



    return -1



def generateSentence():

    res = ["The"]

    while len(res) < 20:
        value = res[-1].lower()

        possible_words = []

        index = 0

        while index < len(WORDS):
            if WORDS[index] == value and index + 1 < len(WORDS):
                index += 1
                possible_words.append(WORDS[index])
            index += 1

        num = random.randrange(0, len(possible_words))

        res.append(possible_words[num])


    sentence = ""

    for i in range(len(res)):
        sentence += " " + res[i]


    sentence = sentence.lstrip(" ")
    sentence += "."

    return sentence






if __name__ == '__main__':
    print("The total amount of words:")
    print(getTotalNumberOfWords())
    print("\n")

    print("The total amount of unique words:")
    print(getTotalUniqueWords())
    print("\n")

    print("The 20 most frequent words")
    print(get20MostFrequentWords())
    print("\n")

    print("The 20 most interesting frequent words")
    print(get20MostInterestingFrequentWords())
    print("\n")

    print("The 20 least frequent words")
    print(get20LeastFrequentWords())
    print("\n")

    print("Word Frequency")
    print("word = bennet")
    print(getFrequencyOfWord("bennet"))
    print("word = darcy")
    print(getFrequencyOfWord("darcy"))
    print("word = london")
    print(getFrequencyOfWord("london"))
    print("\n")


    print("Find the quote")
    print("Quote = 'dear sir'")
    print(getChapterQuoteAppears("DEAR SIR"))
    print("Quote = 'His plan did not vary on seeing them. Miss Bennet's lovely face confirmed his views, and established all his strictest notions of what was due to seniority'")
    print(getChapterQuoteAppears("His plan did not vary on seeing them. Miss Bennet's lovely face confirmed his views, and established all his strictest notions of what was due to seniority"))

    print("Quote = 'angry people are not always wise'")
    print(getChapterQuoteAppears("angry people are not always wise"))
    print("Quote = 'software is the best'")
    print(getChapterQuoteAppears("software is the best"))
    print("\n")


    print("Printing 3 generated sentences")
    print(generateSentence())
    print(generateSentence())
    print(generateSentence())



