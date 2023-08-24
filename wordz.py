import eng_to_ipa as ipa
import random
import json
import re

f = open('./sound.json')
sound = json.load(f)
replacement_ratio = 0.6

def assign_probabilities(input_list):
    total_items = len(input_list)
    probabilities = [1 / (i + 1) for i in range(total_items)]
    return probabilities

def ipa_to_eng(w, actual_word):
    w = w.replace('ˌ', '')
    w = w.replace("ˈ", "")
    chars = list(w)
    length = len(chars)
    index = 0
    regroup = []
    while index < length:
        phonetic = ""
        if chars[index] == 'e' and index+1 < length and chars[index+1] == 'ɪ':
            phonetic = 'eɪ'
            index += 1
        elif chars[index] == 'a' and index+1 < length and chars[index+1] == 'ʊ':
            phonetic = 'aʊ'
            index += 1
        elif chars[index] == 'a' and index+1 < length and chars[index+1] == 'ɪ':
            phonetic = 'aɪ'
            index += 1
        elif chars[index] == 'ə' and index+1 < length and chars[index+1] == 'r':
            phonetic = 'ər'
            index += 1
        elif chars[index] == 'o' and index+1 < length and chars[index+1] == 'ʊ':
            phonetic = 'oʊ'
            index += 1
        elif chars[index] == 'ɔ' and index+1 < length and chars[index+1] == 'ɪ':
            phonetic = 'ɔɪ'
            index += 1
        else:
            phonetic = chars[index]
        
        index += 1
        if phonetic in sound:
            weighted_probability = assign_probabilities(sound[phonetic])
            selected = random.choices(sound[phonetic], weights=weighted_probability, k=1)[0]
            regroup.append(selected)
        elif phonetic == 'ɪ':
            for char in actual_word:
                if char == 'i':
                    regroup.append('i')
                    break
                elif char == 'o':
                    regroup.append('o')
                    break
        else:
            regroup.append(phonetic)
    
    return "".join(regroup)

try:
    while True:
        print()
        line = input("Enter a sentence: \n")
        line = re.sub(r'[^\w\s]', '', line)
        arr = line.split(" ")
        output = []

        for word in arr:
            wordz = ipa.convert(word)
            output_word = ipa_to_eng(wordz, word)
            output.append(output_word) if random.random() <= replacement_ratio else output.append(word)

        print()
        print(" ".join(output))
except KeyboardInterrupt:
    print()
    print("cya")
