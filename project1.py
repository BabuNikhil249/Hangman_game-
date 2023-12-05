import random
import string

def hangman():
    words=['bangalore','mysore','mandya']
    word=random.choice(words).upper()
    word_letters=set(word)
    alphabet=set(string.ascii_uppercase)
    used_letters=set()

    
    lives=5
    while len(word_letters)>0 and lives > 0:
        print("you have",lives,"lives left and you have used those letters :"," ".join(used_letters))
        word_list=[letter if letter in used_letters else '-' for letter in word]
        print("current word is : "," ".join(word_list))

        user_letter=input("guess a letter ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives=lives-1
                print(f"your letter {user_letter} is not present in the word selected")

        elif user_letter in used_letters:
            
            print("you have already choose this letter please choose anothe letter")
        else:
            print("invalid") 
    if lives==0:
        print("sorry you have lost the game")
    else:
        print("super you have guessed the word correctly")
    return 0
hangman()