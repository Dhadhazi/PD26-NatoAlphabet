import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_word_dict = {row.letter:row.code for (index, row) in data.iterrows()}

user_word = input("Enter a word: ")

nato_coded_word = [nato_word_dict[word.upper()] for word in user_word if word != ' ']

print(nato_coded_word)