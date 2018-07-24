__author__ = 'Gyulnara'

def getWords():
    book = open("1342.txt", "r")
    book_lines = book.readlines()

    list_of_words = []

    for line in book_lines:
        line = line.strip("\n").split()
        for word in line:
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


            list_of_words.append(word.lower())

    return list_of_words

if __name__ == '__main__':
    print(getWords())