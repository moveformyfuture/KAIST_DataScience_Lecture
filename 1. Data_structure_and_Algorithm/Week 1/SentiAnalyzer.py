import math

class SentiAnalyzer:

    # Make the method signature to accept "sentidata" and "word"
    def __init__(self):
        print('This is a senti analyzer')

    def probWordPositiveAndNegative(self, sentidata, word, idxWord):
        pointedWord = word[idxWord]
        reviews = [int(float(row[-1])) for row in sentidata] # 긍정 부정 데이터
        occurrence = [int(float(row[idxWord])) for row in sentidata] # 단어 유무 데이터

        # Calculate the number of positive review occurrence with the pointed word, and assign the calculated value to 'positive'
        positive = 0
        for i in range(len(occurrence)):
            positive = positive + occurrence[i] * reviews[i] # 1번

        # Calculate the number of positive reviews from the entire review set
        numPositiveReviews = sum(reviews)# 2번

        # Calculate the number of negative review occurrence with the pointed word, and assign the calculated value to 'negative'
        negative = 0
        for i in range(len(occurrence)):
            negative = negative + occurrence[i] * (1 - reviews[i]) # 3번

        rowCount = len(sentidata)
        positiveProb = float(positive) / float(numPositiveReviews)
        negativeProb = float(negative) / float(rowCount - numPositiveReviews)

        if positiveProb == 0:
            positiveProb = 0.00001
        if negativeProb == 0:
            negativeProb = 0.00001
        return pointedWord, positiveProb, negativeProb

    def probPositiveAndNegative(self, sentidata):
        positive = sum([int(float(row[-1])) for row in sentidata])
        numReviews = len(sentidata)
        negative = numReviews - positive
        positiveProb = float(positive) / float(numReviews)
        negativeProb = float(negative) / float(numReviews)
        return positiveProb, negativeProb

    def findUsedWords(self, sentidata, word, idx):
        # Return the index of the used words in 'idx'th review
        temp = [int(float(x)) for x in sentidata[idx][:-1]]
        idxUsedWords = [index for index, value in enumerate(temp) if value == 1]
        # Return the actual words in 'idx'th review
        usedWords = [word[idx] for idx in idxUsedWords]
        return idxUsedWords, usedWords

    def runAnalysis(self, sentidata, word, idxReview):
        probLogPositive = 0
        probLogNegative = 0
        idxUsedWords, usedWords = self.findUsedWords(sentidata, word, idxReview)

        # Make a for-loop to run from the first word to the last word
        for i in range(len(idxUsedWords)): # 4번
            # get the first word from the used word set
            idxWord = idxUsedWords[i] # 5번
            # calculate the word's probability to be positive or negative
            pointedWord, positive, negative = self.probWordPositiveAndNegative(sentidata, word, idxWord) # 6번
            probLogPositive += math.log(positive)
            probLogNegative += math.log(negative)

        positiveProb1, negativeProb1 = self.probPositiveAndNegative(sentidata)
        probLogPositive += math.log(positiveProb1)
        probLogNegative += math.log(negativeProb1)

        if probLogPositive > probLogNegative: # 7번
            sentiment = 'Positive'
            print('Positive')
        else:
            sentiment = 'Negative'
            print('Negative')

        return probLogPositive, probLogNegative, sentiment

