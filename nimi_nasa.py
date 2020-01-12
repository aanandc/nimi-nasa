#!/usr/bin/python3

import argparse

from random import choice

#TODO anu en jo kama ken kepeken laso lon mu o pimeja poka walo seme sijelo sinpin tan
 
tp_nouns = ["akesi","ala","alasa","ale","ante","awen","esun","ijo","ike","ilo","insa","jaki","jan","jelo","kala","kalama",
            "kasi","kili","kiwen","ko","kon","kule","kulupu","kute","lape", "lawa" , "len","lete","lili", "linja", "lipu",
            "luka","lukin","lupa","ma","mama","mani","meli","mi","mije","moku","moli","monsi","mun","musi","mute", "nanpa",
            "nasa","nasin","nena","ni","nimi","noka","olin","ona","open","pakala","pali","palisa","pan","pana","pilin",
            "pini", "pipi" , "poki","pona", "sama","seli","selo","sewi","sike","sin","sina","sitelen","sona","soweli",
            "suli","suno","supa","suwi","tawa","telo","tenpo","toki","tomo","tu","unpa","uta","utala", "wan","waso","weka","wile"
]

tp_verbs = ["alasa","anpa","ante","awen","ike","jaki","kama","ken","kepeken","kute",
            "lape","lawa","len","lete","lili","lukin"

            
]

tp_prepos = ["lon","tan"]

size_tp_nouns = [2,2,2,2,2,2,2,3,1,2,1,2,1,2,1,2,1,2,1,2,2,1,1]

def get_compound_noun(n,word_list):
    answer = ""
    for i in range(0,n):
        answer = choice(word_list) + " " + answer
    answer = answer.strip()
    return answer

def get_noun():
    val = get_compound_noun(choice(size_tp_nouns),tp_nouns)
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

def first_portion(add_li):
    val = get_noun()
    v = val.split()
    if v[0] in ["mi","sina"]:
        return v[0] + " " +  get_verb()
    else:
        if add_li == True:
            val = val + " li " 
    return val

def mainstub():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--noun', action='store_true', 
    help="just generate a toki pona noun and exit")
    args = parser.parse_args()
    if args.noun:
        val = get_noun()
        print(val)
        return
    val = first_portion(True)
    print(val)

mainstub()    
