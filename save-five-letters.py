from get_words import get_words

if __name__=="__main__":
    words = get_words()
    lengths = []
    for word in words:
        k = len(set(word))
        if k==5:
            lengths.append(word)
    with open("no-repeat-words.txt", mode = "a") as f:
        for word in lengths:
            f.write(word + "\n")
            
