"""
Given a long text string, count the number of occurrences of each word. Ignore case. Assume the boundary of a word is whitespace - a " ", or a line break denoted by "\n". Ignore all punctuation, such as . , ~ ? !. Assume hyphens are part of a word - "two-year-old" and "two year old" are one word, and three different words, respectively.

Return the word counts as a string formatted with line breaks, in alphanumeric order.

Example:
"I do not like green eggs and ham,
I do not like them, Sam-I-Am"

Output:
i 2
do 2
not 2
like 2
green 1
eggs 1
and 1
ham 1
them 1
sam-i-am 1

Also Valid:
and 1
do 2
eggs 1
green 1
ham 1
i 2
like 2
not 2
sam-i-am 1
them 1
"""
def count_words(text):
    word_table = {}
    for word in text.split():
        word = word.strip(".,~?!").lower()
        if word_table.get(word) == None:
            word_table[word] = 1
        else:
            word_table[word] += 1
    return '\n'.join(f'{word} {freq}' for word, freq in word_table.items())


text = "I do not like green eggs and ham, \nI do not like them, Sam-I-Am"
# print(text)
# text_arr = text.split()
# print(text_arr)
# text_arr = [word.strip(".,~?!").lower() for word in text_arr]
# print(text_arr)
# text = ''.join(text_arr)
# print(text)
print(count_words(text))