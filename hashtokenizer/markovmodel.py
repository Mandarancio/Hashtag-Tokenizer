#! /usr/bin/python3
"""Simple algorith to determine the language of the tag."""


def __load_dict__(lang):
    path = "resources/{}_markov_wn.csv".format(lang)
    fdict = {}
    with open(path) as file:
        for line in file.readlines():
            line = line.strip()
            name = line.split(',')[0]
            freq = float(line.split(',')[1])
            fdict[name] = freq
    return fdict


def test_word(word, langs):
    max_f = 0
    max_c = 'None'
    word = word if len(word) < 3 else word[:3]
    for lang in langs:
        fdict = langs[lang]
        if word in fdict and fdict[word] > max_f:
            max_c = lang
            max_f = fdict[word]
    return max_c

        


if __name__ == "__main__":
    langs = ['eng', 'ita', 'fra', 'spa']
    freqs = {}
    for lang in langs:
        freqs[lang] = __load_dict__(lang)

    word = "hello world"
    print(test_word(word, freqs))