# -*- coding: utf-8 -*-
"""
Created on Thu May 28 14:15:19 2020

@author: Alex
"""

class wordscapes:
    total_matches=[]
    def wordtodict(self, word):
        letterdict={}
        for i in range(len(word)):
            if word[i] != '-':
                letterdict[i]=word[i]
        return letterdict
    def solve_daily(self, myword, available_letters):
        worddict=wordscapes.wordtodict(myword)
        with open('C:\\Users\\Alex\\Documents\\Python\\dictionary.txt', 'r') as dict_file:
            for line in dict_file.readlines():
                tempdict=wordscapes.wordtodict(line)
                match1, match2, match3=(True, True, True)
                templetters=list(tempdict.values())
                templetters=templetters[:-1]
                if len(myword) != len(line)-1:
                    match1=False
                for num, letter in worddict.items():
                    try:
                        if tempdict[num] != letter:
                            match2=False
                    except:
                        pass
                for templetter in templetters:
                    if templetters.count(templetter) > available_letters.count(templetter):
                        match3=False
                if match1==True and match2==True and match3==True:
                    wordscapes.total_matches.append(line[:-1])
    def solve_normal(self, available_letters):
        with open('C:\\Users\\Alex\\Documents\\Python\\dictionary.txt', 'r') as dict_file:
            for line in dict_file.readlines():
                tempdict=wordscapes.wordtodict(line)
                match1, match2=(True, True)
                templetters=list(tempdict.values())
                templetters=templetters[:-1]
                lengths=list(range(3, len(available_letters)))
                if not len(line) in lengths:
                    match1=False
                for templetter in templetters:
                    if templetters.count(templetter) > available_letters.count(templetter):
                        match2=False
                if match1==True and match2==True:
                    wordscapes.total_matches.append(line[:-1])
