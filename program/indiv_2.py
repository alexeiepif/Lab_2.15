#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Ученикам, желающим запомнить правила написания слов в английском языке,
# часто напоминают следующее рифмованное одностишие:
# «I before E except after C» (I перед E, если не после C).
# Это правило позволяет запомнить, в какой последовательности
# писать буквы I и E, идущие в слове одна за другой, а именно:
# буква I должна предшествовать букве E, если непосредственно
# перед ними не стоит буква C. Если стоит – порядок гласных будет обратным.
# Примеры слов, на которые действует это правило:
# believe, chief, fierce, friend, ceiling и receipt. Но есть и исключения
# из этого правила, и одним из них является слово weird (странный).
# Напишите программу, которая будет построчно обрабатывать текстовый файл.
# В каждой строке может присутствовать много слов, а может и не быть ни одного.
# Слова, в которых буквы E и I не соседствуют друг с другом,
# обработке подвергать не следует. Если же такое соседство присутствует,
# необходимо проверить, соответствует ли написание анализируемого слова
# указанному выше правилу. Создайте и выведите на экран два списка.
# В первом должны располагаться слова, следующие правилу,
# а во втором – нарушающие его. При этом списки не должны содержать
# повторяющиеся слова. Также отобразите на экране длину каждого списка,
# чтобы пользователю было понятно, сколько слов в файле не отвечает правилу.

import re


if __name__ == "__main__":
    words_follow_rule = set()
    words_break_rule = set()

    # Функция для проверки слова на соответствие правилу
    def check_word(word):
        if "cie" in word:
            return False
        if "cei" in word:
            return True
        if "ie" in word:
            return True
        if "ei" in word:
            return False

    with open("Lab_2.15/program/file_ind_2.txt", "r") as file:
        for line in file:
            for word in re.findall(r"\b\w*(?:ei|ie)\w*\b", line, re.I):
                if word.lower() == "weird":  # Исключение
                    words_follow_rule.add(word.lower())
                elif word.lower() == "wierd":  # Неправильное исключение
                    words_break_rule.add(word.lower())
                elif check_word(word.lower()):
                    words_follow_rule.add(word.lower())
                else:
                    words_break_rule.add(word.lower())

    print("Слова, следующие правилу:")
    for word in words_follow_rule:
        print(word)
    print("Количество слов:", len(words_follow_rule))

    print("\nСлова, не следующие правилу:")
    for word in words_break_rule:
        print(word)
    print("Количество слов:", len(words_break_rule))
