"""
Word Occurrences
Estimate: 20 minutes
Actual: 21:08

"""

text = "this is a collection of words of nice words this is a fun thing it is"

word_to_count = {}
print(text)
text = text.split()
for word in text:
    try:
        word_to_count[word] += 1
    except KeyError:
        word_to_count[word] = 1
longest_word = max((len(word)) for word in word_to_count)

for word in sorted(word_to_count):
    print(f"{word:{longest_word}} : {word_to_count[word]}")
