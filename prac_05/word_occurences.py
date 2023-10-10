"""
Word Occurences
Estimate: 20 minutes
Actual:

"""

text = "this is a collection of words of nice words this is a fun thing it is"

word_to_count = {}

text = text.split()
for word in text:
    try:
        word_to_count[word] += 1
    except KeyError:
        word_to_count[word] = 1
