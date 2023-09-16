# O(n)

def spin_words(sentence):
    empty_string = []
    for word in sentence.split(): # O(n)
        if len(word) >= 5:# O(1)
            empty_string.append(word[::-1])# O(1)
        else:
            empty_string.append(word)#O(1)
    return ' '.join(empty_string)