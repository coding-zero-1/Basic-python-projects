"""this is a basic project making the word guess game 
you will have to guess a particular word to win the game 
if you guessed a wrong word then you will get a hint regarding the word you have to guess


"""
import random
words=["BOY","GIRL","HORSE","CALENDER","CHEETAH","PHOTOSYNTHESIS"]
hints={"BOY":"a young male,three letter word","GIRL":"a young female,four letter word","HORSE":"a fast animal with four legs that we can ride,five letter word","CALENDER":"a thing where you look at dates and events,eight letter word","CHEETAH":"a very fast wild animal,seven letter word","PHOTOSYNTHESIS":"a process through which plants make their food using sunlight,a fourteen letter word"}
word_to_guess=random.choice(words)
hint=hints[word_to_guess]
while True:
    print("YOUR HINT IS: ",hint)
    guessed_word=input("Enter your guessed word: ").upper()
    if guessed_word==word_to_guess:
        print("CONGRATS YOU GUESSED THE RIGHT WORD: ",word_to_guess)
        break
    else:
        print("YOU GUESSED THE WRONG WORD")