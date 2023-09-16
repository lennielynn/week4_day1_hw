#O(n)

def get_count(sentence):
    count = 0 # O(1)
    vowel = 'aeiou' # O(1)
    for letter in sentence: # O(N)
        if letter.lower() in vowel:  # O(1) + O(N)
          count += 1 # O(1)
    return count 
print(get_count('this is a sentence'))
