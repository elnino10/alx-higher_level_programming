#!/usr/bin/python3

def multiple_returns(sentence):
    count = 0
    if sentence == "":
        return (count, None)
    for char in sentence:
        count += 1
    return (count, sentence[0])
