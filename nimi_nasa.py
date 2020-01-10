#!/usr/bin/python3

from random import choice

#TODO anu en jo kama ken kepeken

tp_nouns = ["akesi","ala","alasa","ale","ante","awen","esun","ijo","ike","ilo","insa","jaki","jan","jelo","kala","kalama",
            "kasi","kili","kiwen","ko","kon","kule","kulupu","kute",

]

tp_verbs = ["alasa","anpa","ante","awen","ike","jaki","kama","ken","kepeken","kute",
            "lape","lawa","len","lete","lili","lukin"

]

tp_prepos = [ ]

size_tp_nouns = [2,2,2,2,2,2,2,3,1,2,1,2,1,2,1,1,1,2,1,1,2]

def get_compound_noun(n):
    answer = ""
    for i in range(0,n):
        answer = choice(tp_nouns) + " " + answer
    return answer

def get_noun():
    val = get_compound_noun(choice(size_tp_nouns))
    val = val.strip()
    return val


def get_verb():
    return choice(tp_verbs)

def make_sentence1():
    val = get_noun() + " li " + get_noun()
    return val

def make_sentence2():
    val = get_noun() + " li " + get_verb() + " e " + get_noun()
    return val

def mainstub():
    val = make_sentence2()
    print(val)

mainstub()    
