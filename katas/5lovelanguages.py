#!/usr/bin/env python3

import unittest
import numpy as np
import random

# https://www.codewars.com/kata/5aa7a581fd8c06b552000177/train/python

# According to Gary Chapman, marriage counselor and the author of "The Five Love Languages" books, there are five major ways to express our love towards someone: words of affirmation, 
# quality time, gifts, acts of service, and physical touch. These are called the love languages. Usually, everyone has a main language: the one that he/she "speaks" and understands best. 
# In a relationship, it's import to find your partner's main love language, so that you get along better with each other.

# Your task
# Unfortunately, your relationship got worse lately... After a long discussion with your partner, you agreed to give yourself a few weeks to improve it, otherwise you split up...
# You will be given a partner instance, and n weeks. The partner has a .response method, and the responses may be: "positive" or "neutral". 
# You can try to get a response once a day, thus you have n * 7 tries in total to find the main love language of your partner!

# The love languages are: "words", "acts", "gifts", "time", "touch" (available predefined as LOVE_LANGUAGES)

# Note: your partner may (and will) sometimes give a positive response to any love language ("false positive"), but the main one has a much higher possibility. 
# On the other hand, you may get a neutral response even for the main language, but with a low possibility ("false negative").

# There will be 50 tests. Although it's difficult to fail, in case you get unlucky, just run the tests again. After all, a few weeks may not be enough...
# Examples

# main love language: "words"

# partner.response("words")  -->  "positive"
# partner.response("acts")   -->  "neutral"
# partner.response("words")  -->  "positive"
# partner.response("time")   -->  "neutral"
# partner.response("acts")   -->  "positive"    # false positive
# partner.response("gifts")  -->  "neutral"
# partner.response("words")  -->  "neutral"     # false negative
# etc.

# example class
class TestPartner:
    def __init__(self, main_lang):
        self.main = main_lang
    def response(self, language):
        r = random.random()
        if language == self.main:
            if r < 0.85: return 'positive'
            else:        return 'neutral'
        else: # language != self.main
            if r < 0.15: return 'positive'
            else:        return 'neutral'

LOVE_LANGUAGES = ["words", "acts", "gifts", "time", "touch"]
    
def love_language(partner: TestPartner, weeks: int):
    # your lovely code here
    love_dict = {}
    for language in LOVE_LANGUAGES:
        love_dict[language] = 0

    i = 1
    while i <= weeks*7:
        for l in LOVE_LANGUAGES:
            if partner.response(l) == 'positive':
                love_dict[l] += 1
        i += 1
    return max(love_dict, key=love_dict.get)

def love_languageChatGPT(partner: TestPartner, weeks: int) -> str:
    love_dict = {language: 0 for language in LOVE_LANGUAGES}

    for _ in range(weeks*7):
        for language in LOVE_LANGUAGES:
            if partner.response(language) == 'positive':
                love_dict[language] += 1

    return max(love_dict, key=love_dict.get)


def love_language_best(partner, weeks):
    rst = [0,0,0,0,0]
    for i in range (0, weeks*7):
        if(partner.response(LOVE_LANGUAGES[i%5]) == 'positive'):
            rst[i%5]+=1
    return LOVE_LANGUAGES[rst.index(max(rst))]

class TestLoveLanguage(unittest.TestCase):
    def test_function(self):
        partner = TestPartner('words')
        self.assertEqual(love_language(partner, 6), 'words')
        partner = TestPartner('gifts')
        self.assertEqual(love_language(partner, 6), 'gifts')
        partner = TestPartner('acts')
        self.assertEqual(love_language(partner, 6), 'acts')
        partner = TestPartner('time')
        self.assertEqual(love_language(partner, 6), 'time')
        partner = TestPartner('touch')
        self.assertEqual(love_language(partner, 6), 'touch')


if __name__ == '__main__':
    unittest.main()