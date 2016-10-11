# __author__ = 'Scott Businge'

# -*- coding: utf-8 -*-

import unicodedata


def words(words):
    total_words = []
    words_list = words.split()
    for word in words_list:
        count = 0
        for word2 in words_list:
            if word == word2:
                count += 1
        total_words.append(count)
    # print unicodedata.normalize('NFKD', u'\xc2\xbfQu\xc3\xa9')
    return dict(zip(words_list, total_words))


print(words('word'))  # 1
print(words("one of each"))  # {'one': 1, 'of': 1, 'each': 1}
print(words("one fish two fish red fish blue fish"))  # {'one': 1, 'fish': 4, 'two': 1, 'red': 1, 'blue': 1}
print(words('car : carpet as java : javascript!!&@$%^&'))  # {'car': 1, ":": 2, 'carpet': 1, 'as': 1, 'java': 1, 'javascript!!&@$%^&': 1}
print(words('testing 1 2 testing'))  # {'testing': 2, 1: 1, 2: 1}
print(words('go Go GO'))  # {'go': 1, 'Go': 1, 'GO': 1}
print(words('¡Hola! ¿Qué tal? ??????!'))  # {"¡Hola!": 1, "¿Qué": 1, "tal?": 1, "??????!": 1}
print(words('hello\nworld'))  # {'hello': 1, 'world': 1}
print(words('hello\tworld'))  # {'hello': 1, 'world': 1}
print(words('hello  world'))  # {'hello': 1, 'world': 1}
