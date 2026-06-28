###Chapter 13: Case Study in Data Structure Selection.

import string as s
from collections import defaultdict
import random as r
a = s.punctuation.replace('-','')
table = str.maketrans('\n',' ',a)

with open("moby.txt", encoding='utf-8') as book:
    w = book.read()
    translated = w.translate(table)
    translated = translated.lower()

words = tuple(translated.split(' '))
excerpt = "he was very clever be it sweetness or be angry ashamed or only amused at such a stroke she had never thought of hannah till you were never meant for me I cannot make speeches emma he soon cut it all himself"
wordlist = tuple(excerpt.split(' '))
#These are my two text samples. One is a phrase from Emma, the other is the words of Moby Dick. 

def make_dict(wordlist=words,prefix_len=2):
    distribution = defaultdict(tuple)    #Make empty dict.
    """
    - Set key for the first two, since counting using preceding can't start at the first two.
    - Set key for the last two, since nothing comes after the last two.
    - When the last word is used, the first word will be next, so there needs to be a 
        last_one+first_one that maps to the second_one
    """
    #Isolating slices
    first_two = wordlist[0:2]
    second_two = [wordlist[1:3]]
    last_two = wordlist[-2:]
    last_first = (wordlist[-1],wordlist[0])
    #Setting probabilities manually. This is redundant if the last words are used again, but critical if they are unique. 
    distribution[first_two] += (wordlist[2],)
    distribution[last_two] += (wordlist[0],)
    distribution[last_first] += (wordlist[1],)
    """
    - Starts at the third word, which will be the value
    - The key is the first value and the second value. Because [:] is endpoint uninclusive i works for the end point.
    """
    for i in range(2,len(wordlist)):
        val = wordlist[i]  # Starts on the third word.
        key = wordlist[i-2:i] #Starts on the first and second words
        distribution[key] +=(val,)
    return distribution

distribution = make_dict(words,2)

def generate_more(starting=('He was'),num_words=50,distribution=distribution):
    paragraph = []
    for word in starting.lower().split(' '):
        paragraph.append(word)
    prev1 = (wordlist[0],)
    prev2 = (wordlist[1],)
    while len(paragraph)<num_words:
        option_key = prev1 + prev2
        #print('Option Key\t',option_key)
        options = distribution[option_key]
        #print('Options\t',options)
        new_word = r.choice(options)
        #print('New word\t',new_word)
        paragraph.append(new_word)
        prev1 = prev2
        #print('Prev 1\t',prev1)
        prev2 = (new_word,)
        #print('Prev 2\t',prev2)
    return starting,paragraph

starting,paragraph = generate_more()

def make_pretty(starting=starting,paragraph=paragraph):
    final_str = starting+' '
    for word in paragraph:
        final_str = final_str + word + ' '
    return final_str

pretty = make_pretty()
        












    




















