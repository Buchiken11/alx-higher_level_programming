#``usr/bin/python3
def multiple_returns(sentence):
    for i in sentence:
        if not sentence:
            return None
        length = len(sentence)
        if length >= 0:
            first = sentence[0]
            return length, first
