import random
from hangman_words import word_list
word=random.choice(word_list)
lives=6
from hangman_art import logo
print(logo)
display=[]
for _ in word:
    display+="_"
print(display)
x=True
while x:
    guess=input("Guess a letter : ").lower()
    if guess in display:
        print(f"You've already guessed {guess}")
    for i in range(len(word)):
        if word[i] == guess:
            display[i]=guess
    if guess not in word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives-=1
        if lives==0:
            x=False
            print("you lose")
            print("the word was "+ word)
    print(f"{' '.join(display)}")
    if "_" not in display:
        x=False
        print("you win")
    from hangman_art import stages
    print(stages[lives])
    