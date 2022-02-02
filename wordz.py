import eng_to_ipa as ipa
from random import randint
import json
import re

f = open('./sound.json')
sound = json.load(f)

def ipa_to_eng(w):
    w = w.replace('ˌ', '')
    w = w.replace("ˈ", "")
    char = list(w)
    length = len(char)
    index = 0
    regroup = []
    while index < length:
        phonetic = ""
        if char[index] == 'e' and index+1 < length and char[index+1] == 'ɪ':
            phonetic = 'eɪ'
            index += 1
        elif char[index] == 'a' and index+1 < length and char[index+1] == 'ʊ':
            phonetic = 'aʊ'
            index += 1
        elif char[index] == 'a' and index+1 < length and char[index+1] == 'ɪ':
            phonetic = 'aɪ'
            index += 1
        elif char[index] == 'ə' and index+1 < length and char[index+1] == 'r':
            phonetic = 'ər'
            index += 1
        elif char[index] == 'o' and index+1 < length and char[index+1] == 'ʊ':
            phonetic = 'oʊ'
            index += 1
        elif char[index] == 'ɔ' and index+1 < length and char[index+1] == 'ɪ':
            phonetic = 'ɔɪ'
            index += 1
        else:
            phonetic = char[index]
        
        index += 1
        if phonetic in sound:
            regroup.append(sound[phonetic][randint(0, len(sound[phonetic])-1)])
        else:
            regroup.append(phonetic)
    
    return "".join(regroup)

while True:
    print()
    line = input("Enter a sentence: \n")
    line = re.sub(r'[^\w\s]', '', line)
    arr = line.split(" ")
    output = []

    for word in arr:
        wordz = ipa.convert(word)
        output_word = ipa_to_eng(wordz)
        output.append(output_word)

    print()
    print(" ".join(output))
