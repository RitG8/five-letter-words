"""
distinct.py

Donald Knuth, Art of Computer Programming, Volume 4 Facsimile 0
Exercise #27

How many SGB words contain exactly k distinct letters, for 1 <= k <= 5?
"""
from get_words import get_words #calls this function from the file get_words

if __name__=="__main__":  #This is boilerplate code that allows the function to be run
    #as a main file and as something that can be imported.
    words = get_words()  #This is a string
    lengths = [[] for i in range(5+1)]

    for word in words:
        k = len(set(word))  #set() takes out any repeats
        lengths[k].append(word)  #This finds the length of each word after repeats are done 

    for i in range(1,5+1):
        print("-"*40)
        print("Number of words with {0:d} letters: {1:d}".format(i, len(lengths[i])))
        #This will take i and the length and put them in the {0:d} and {1:d} spots respectively
        print(", ".join(lengths[i][0:5]))

