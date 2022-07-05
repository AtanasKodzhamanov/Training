#
# Complete the 'reverse_words_order_and_swap_cases' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#
import os

def reverse_words_order_and_swap_cases(sentence):
    wordsArray=sentence.swapcase().split(" ")
    wordsArray.reverse()
    output=' '.join(wordsArray)
    return output

reverse_words_order_and_swap_cases("the cow is milky")