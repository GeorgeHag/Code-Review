###Chapter 13: Case Study in Data Structure Selection.

import string as s
from collections import defaultdict
#from Chapter_9 import strip_whitespaces as sw
##d = s.whitespace.replace(' ','')
##d = d.replace('-','')
##d = d.replace('\n','')
a = s.punctuation.replace('-','')
table = str.maketrans('\n',' ',a)
#b = str(sw())[0:300]
#print(b.translate(table))

start = """CHAPTER 1. Loomings.

Call me Ishmael. Some years ago—never mind how long precisely—having
little or no money in my purse, and nothing particular to interest me
on shore, I thought I would sail about a little and see the watery part
of the world. It is a way I have of driving off the spleen and
regulating the circulation. Whenever I find myself growing grim about
the mouth; whenever it is a damp, drizzly November in my soul; whenever
I find myself involuntarily pausing before coffin warehouses, and
bringing up the rear of every funeral I meet; and especially whenever
my hypos get such an upper hand of me, that it requires a strong moral
principle to prevent me from deliberately stepping into the street, and
methodically knocking people’s hats off—then, I account it high time to
get to sea as soon as I can. This is my substitute for pistol and ball.
With a philosophical flourish Cato throws himself upon his sword; I
quietly take to the ship. There is nothing surprising in this. If they
but knew it, almost all men in their degree, some time or other,
cherish very nearly the same feelings towards the ocean with me."""



with open("moby.txt", encoding='utf-8') as book:
    w = book.read()
    translated = w.translate(table)
    translated = translated.lower()
#split: iterable.split(seperator)
#join: seperator.join(iterator)
words = tuple(translated.split(' '))

histogram = {}
for word in words:
    histogram[word] = histogram.setdefault(word,0)+1
frequencies = defaultdict(list)
for key,value in histogram.items():
    frequencies[value].append(key)

highest_freq = max(histogram.values())
frequency_list = list(histogram.values())
high = sorted(frequency_list)[-1:-400:-1]
most_common = frequencies[highest_freq]




# Markov Analysis: A poor attempt :)
import string as s
from collections import defaultdict
import random as r
  
excerpt = "he was very clever be it sweetness or be angry ashamed or only amused at such a stroke she had never thought of hannah till you were never meant for me I cannot make speeches emma he soon cut it all himself"
wordlist = tuple(excerpt.split(' '))

with open("moby.txt", encoding='utf-8') as book:
    w = book.read()
    translated = w.translate(table)
    translated = translated.lower()

words = tuple(translated.split(' '))

def make_dict(wordlist=words,prefix_len=2):
    distribution = defaultdict(tuple)    #Make empty dict.

    first_two = wordlist[0:2]
    second_two = [wordlist[1:3]]
    last_two = wordlist[-2:]
    distribution[first_two] += (wordlist[2],)#Set key for the first two, since counting using preceding can't start at the first two.
    distribution[last_two] += (wordlist[0],) #Set key for the last two, since nothing comes after the last two.
    last_first = (wordlist[-1],wordlist[0])
    """ When the last word is used, the first word will be next,
        so there needs to be a last_one+first_one that maps to the second_one"""
    distribution[last_first] += (wordlist[1],)
    for i in range(2,len(wordlist)):
        val = wordlist[i]  #Starts at the third word, which will be the value
        key = wordlist[i-2:i]#The key is the first value and the second value. Because [:] is endpoint uninclusive i works for the end point.
        distribution[key] +=(val,)
    return distribution

distribution = make_dict(words,2)
print(distribution)

def generate_more(starting=('He was'),num_words=50,distribution=distribution):
    paragraph = []
    for word in starting.lower().split(' '):
        paragraph.append(word)
    prev1 = (wordlist[0],)
    prev2 = (wordlist[1],)
    while len(paragraph)<num_words:
        option_key = prev1 + prev2
        print('Option Key\t',option_key)
        options = distribution[option_key]
        print('Options\t',options)
        new_word = r.choice(options)
        print('New word\t',new_word)
        paragraph.append(new_word)
        prev1 = prev2
        print('Prev 1\t',prev1)
        prev2 = (new_word,)
        print('Prev 2\t',prev2)
    return starting,paragraph
#print('generated')

starting,paragraph = generate_more()

def make_pretty(starting=starting,paragraph=paragraph):
    final_str = starting+' '
    for word in paragraph:
        final_str = final_str + word + ' '
    return final_str

pretty = make_pretty()
        












    




















