import sys


level = input("Wybierz poziom trudności (easy, medium, hard):")
if level == 'easy':
    no_of_tries = 5
if level == 'medium':
    no_of_tries = 3
if level == 'hard':
    no_of_tries = 1
else:
    print("Wpisz nazwe poprawnie")



word = "Olivia".lower()
used_letters = []
user_word = []
for _ in word:
    user_word.append("_")

# Przechodzimy- iterujemy po słowie (word) i sprawdzamy index i litere dla niego.
def find_indexes(word, letter):
    indexes = []
    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)

    return indexes

def show_state_of_game():
    print(user_word)
    print("Pozostało prób:", no_of_tries)
    print("Uzyte litery: ", used_letters)
    print()

def valid(letter):
    if len(letter) >= 1:
        print("Podaj jedna litere")


# Początek
while True:
    letter = input("Podaj litere: ")
    if len(letter) > 1:
        print("Podaj jedna litere")

    if letter in used_letters:
        print("Nie można użyć drugi raz tej litery")
        print("Podaj nową litere")
    else:
        used_letters.append(letter)
        found_indexes = find_indexes(word, letter)

    if len(found_indexes) == 0:
        print("Nie ma takiej litery")
        no_of_tries -= 1
        if no_of_tries == 0:
            print("Koniec szans")
            sys.exit(0)

    else:
        for index in found_indexes:
            user_word[index] = letter


        if "".join(user_word) == word:
            print("To jest to słowo!")
            sys.exit(0)

    show_state_of_game()


