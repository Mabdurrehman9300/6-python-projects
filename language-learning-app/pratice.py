import random

common_words = {
    "السلام": {
        "pronunciation": "as-salāmu",
        "translation": "peace"
    },
    "حب": {
        "pronunciation": "hubb",
        "translation": "love"
    },
    "قلب": {
        "pronunciation": "qalb",
        "translation": "heart"
    }
}
keys = list(common_words.keys())
values = list(common_words.values())
words = keys, values
print(keys[0][6:0:-1]) # revers

# uncommon_words = random.shuffle(common_words)
# print(uncommon_words)
