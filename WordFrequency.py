#7) WordFrequency.py - Write a program that reads the contents of a text file (you can use this file - AI.txt Download AI.txt ). 
#The program should create a dictionary in which the keys are the individual words found in the file and the values are the number of times each word appears. 
# For example, if the word “the” appears 128 times, the dictionary would contain an element with 'the' as the key and 128 as the value. 
# The program should display the frequency of each word.

def main():
    infile = open("AI.txt", "r")
    words = infile.read()
    no_special = words.replace("(", "")
    no_special = no_special.replace(")", "")
    no_special = no_special.replace('"', "")
    no_special = no_special.replace(",", "")
    no_special = no_special.replace(".", "")
    no_special = no_special.replace("'", "")
    no_special = no_special.replace("-", "")
    no_special = no_special.replace("]", "")
    no_special = no_special.replace("[", "")
    no_special = no_special.replace("  ", " ")

    lower_case = no_special.lower()
    AIwords = lower_case.split(" ")
    FreqDict = {}

    for word in AIwords:
        if word in FreqDict:
            FreqDict[word] += 1
        else:
            FreqDict[word] = 1

    for key in FreqDict:
        print(key, ": ", FreqDict[key])

    #Close the File
    infile.close()

main()