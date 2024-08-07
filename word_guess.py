"""this is a basic project making the word guess game 
you will have to guess a particular word to win the game using a hint
if you guessed a wrong word then you will get a hint regarding the word you have to guess
"""

import random
words=["BOY","GIRL","HORSE","CALENDER","CHEETAH","PHOTOSYNTHESIS","CAT","LION","DOG","ZEBRA","CHAMELEON","SMARTPHONE","LAPTOP"]
hints={"BOY":"a young male,three letter word","GIRL":"a young female,four letter word","HORSE":"a fast animal with four legs that we can ride,five letter word","CALENDER":"a thing where you look at dates and events,eight letter word","CHEETAH":"a very fast wild animal,seven letter word","PHOTOSYNTHESIS":"a process through which plants make their food using sunlight,a fourteen letter word","CAT":"a small domestic pet, three letter word","DOG":"called the most loyal pet or man's best friend,three letter word","LION":"an animal known as the king of the jungle,four letter word","CHAMELEON":"an animal which is known to change its colour,nine letter word","ZEBRA":"a wild animal with white and black stripes on its body, five letter word","SMARTPHONE":"what are new modern phone's called,ten letter word","LAPTOP":"a desktop computer that you can take anywhere and even use it on your lap,six letter word"}
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