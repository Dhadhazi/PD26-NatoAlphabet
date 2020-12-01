import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_word_dict = {row.letter:row.code for (index, row) in data.iterrows()}


def generate_nato_word():
    user_word = input("Enter a word: ").upper()
    try:
        nato_version = [nato_word_dict[word] for word in user_word if word != ' ']
    except KeyError:
        print("Only alphabet letters please")
        generate_nato_word()
    else:
        print(nato_version)


generate_nato_word()