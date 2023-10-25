"""
Word Occurrences
Estimate: 20 minutes
Actual:

"""
text = input(": ")
word_to_count = {}
strings = text.split()  # should be words, better consistency
for string in strings:
    try:
        word_to_count[string] += 1
    except KeyError:
        word_to_count[string] = 1

longest_word = max((len(word)) for word in word_to_count)  # doesn't sound like a number
for word in sorted(word_to_count):
    print(f"{word:{longest_word}} : {word_to_count[word]}")
print(type(word_to_count))
