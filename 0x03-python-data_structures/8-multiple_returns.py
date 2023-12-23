#!/usr/bin/python3
def multiple_returns(sentence):
    for i in sentence:
        if len(sentence) < 0:
            return None
        length = len(sentence)
        if length >= 0:
            first = sentence[0]
            return length, first
