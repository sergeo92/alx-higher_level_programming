#!/usr/bin/python3


def multiple_returns(sentence):
    if sentence is not None:
        lenght = len(sentence)
    
        if lenght == 0:
            return (lenght, None)
        else:
            return (lenght, sentence[0])


if __name__ == "__main__":
    sentence = "At school, I learnt C!"
    length, first = multiple_returns(sentence)
    print("Length: {:d} - First character: {}".format(length, first))

