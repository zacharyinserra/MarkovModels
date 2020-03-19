"""
Scentence generator based on song lyrics from different music genres
By Zachary Inserra
"""
from numpy.random import *
import logging
import random

logging.basicConfig(filename = 'lyricList.log', level = logging.DEBUG)

wordNum = 1500

wordList = []
transitions = {}
traa = {}
country = open("Country", "rt")
hiphop = open("R&BHip-Hop", "rt")
rock = open("Rock", "rt")
testSet = open("Test", "rt")

class genLyric():

    def __init__(self, lyrics):
        """Populates list of words from sample lyrics"""
        words = []
        wordO = []
        count = 0
        for line in lyrics:
            for i in line.split(" "):
                if len(i) == 1:
                    count += 1
                if i not in words:
                    words.append(i.replace("\n", "."))
                    wordO.append(0)
                wordList.append(i.replace("\n", "."))
        num = {}
        for i in wordList:
            if i not in num:
                num[i] = wordList.count(i)
        # print(len(wordList), wordList)
        # print(str(num))
        # print(count)
        """Counts word transitions"""
        for i in range(len(wordList)-1):
            if wordList[i][-1] == ".":
                tra = wordList[i]
            else:
                tra = wordList[i] + " " + wordList[i+1]
            if tra not in transitions:
                transitions[tra] = 1
            else:
                transitions[tra] += 1
        long = {}
        for key in transitions:
            long[key] = transitions[key]
        # print("most common transitions:" + str(long))
        """"""
        for key in sorted(transitions):
            traa[key] = transitions[key]
        for key in traa:
            first = key.split(" ")[0]
            if first in words:
                index = words.index(first)
                wordO[index] += traa[key]
        for key in traa:
            first = key.split(" ")[0]
            index = words.index(first)
            traa[key] = round(traa[key] / wordO[index], 3)
        print(len(words), words)
        # print(len(wordO), wordO)
        # print(len(traa), traa)

        self.genLine(words, traa, wordNum)

        wordList.clear()
        transitions.clear()
        traa.clear()

    def makeLine(self, words, traa):

        startWord = random.choice(words)

        nextWord = startWord
        lineProb = 1
        while nextWord[-1] != ".":
            possible = self.getPoss(traa, nextWord)
            prob = self.getProb(traa, nextWord)
            # print(possible)
            # print(prob)

            nextWord = choice(possible, 1, prob)[0]
            l = possible.index(nextWord)
            p = prob[l]
            lineProb *= p
            startWord += " " + nextWord
        return startWord, lineProb

    def getPoss(self, traa, nextWord):
        possible = []
        for key in traa:
            first = key.split(" ")
            if first[0] == nextWord:
                possible.append(first[1])
        return possible

    def getProb(self, traa, nextWord):
        prob = []
        for key in traa:
            first = key.split(" ")
            if first[0] == nextWord:
                prob.append(traa[key])
        if prob is None:
            prob = [0]
        return prob

    def getRepeats(self, lList):
        repeats = set([i for i in lList if lList.count(i) > 1])
        if repeats:
            print("Repeats:       " + str(repeats))
            logging.info("Repeats:       " + str(repeats))
        else:
            print("There are no repeating words.")

    def getShort(self, lList, pList):
        shortest = min([(len(i.split(" ")), i) for i in lList])
        spot = lList.index(shortest[1])
        prob = pList[spot]
        print("\n"+"Shortest word: " + str(shortest))
        print("Probability:   " + str(prob))
        logging.info("\n"+"Shortest word: " + str(shortest))
        logging.info("Probability:   " + str(prob))

    def getLong(self, lList, pList):
        longest = max([(len(i.split(" ")), i) for i in lList])
        spot = lList.index(longest[1])
        prob = pList[spot]
        print("\n"+"Longest word:  " + str(longest))
        print("Probability:   " + str(prob) + "\n")
        logging.info("\n"+"Longest word:  " + str(longest))
        logging.info("Probability:   " + str(prob) + "\n")

    def getOneWordCount(self, lList):
        count = 0
        for i in lList:
            if len(i.split(" ")) == 1:
                count += 1
        return count

    def genLine(self, words, traa, wordNum):
        lList = []
        pList = []
        for i in range(wordNum):
            newLine = self.makeLine(words, traa)
            lList.append(newLine[0])
            pList.append(newLine[1])
        print("Lyrics:       " + str(lList))
        sum = 0
        for i in pList:
            sum += i
        print(sum/len(pList))
        print("Probabilities:" + str(pList))
        # for i in lList:
        #     logging.info(i)
        self.getRepeats(lList)
        self.getShort(lList, pList)
        self.getLong(lList, pList)
        print("One words: " + str(self.getOneWordCount(lList)))

# def classify(testSet):
#
#     def __init__(self, lyrics):
#         """Populates list of words from sample lyrics"""
#         words = []
#         wordO = []
#         count = 0
#         for line in lyrics:
#             for i in line.split(" "):
#                 if len(i) == 1:
#                     count += 1
#                 if i not in words:
#                     words.append(i.replace("\n", "."))
#                     wordO.append(0)
#                 wordList.append(i.replace("\n", "."))
#         num = {}
#         for i in wordList:
#             if i not in num:
#                 num[i] = wordList.count(i)
#         # print(len(wordList), wordList)
#         # print(str(num))
#         # print(count)
#         """Counts word transitions"""
#         for i in range(len(wordList)-1):
#             if wordList[i][-1] == ".":
#                 tra = wordList[i]
#             else:
#                 tra = wordList[i] + " " + wordList[i+1]
#             if tra not in transitions:
#                 transitions[tra] = 1
#             else:
#                 transitions[tra] += 1
#         long = {}
#         for key in transitions:
#             long[key] = transitions[key]
#         # print("most common transitions:" + str(long))
#         """"""
#         for key in sorted(transitions):
#             traa[key] = transitions[key]
#         for key in traa:
#             first = key.split(" ")[0]
#             if first in words:
#                 index = words.index(first)
#                 wordO[index] += traa[key]
#         for key in traa:
#             first = key.split(" ")[0]
#             index = words.index(first)
#             traa[key] = round(traa[key] / wordO[index], 3)
#         print(len(words), words)
#
#     def comp(traa):


print("Country")
genLyric(country)
print("R&B Hip-Hop")
genLyric(hiphop)
print("Rock")
genLyric(rock)
# classify(testSet)