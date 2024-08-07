'''
This is my first actual project in python.
In this project i will try to make a basic password generator.
-->basic password generator done dated 27 Jan 2024 stored in (password generator copy)
-->added functionality of user input password length and choice for alphanumeric characters and choice of numbers dated 27 Jan 2024
-->Fixed the extra password length issue dated 28 Jan 2024

'''
import random
Alphabets=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
Alphanumeric=["@","#","&","$","%","!"]
num=int(input("Enter your password length: "))
alphanum=input("Do you want alphanumeric characters(Y or N): ")
numbers=input("Do you want add numbers in your password(Y or N): ")
numbers=numbers.upper()
alphanum=alphanum.upper()
c=""
while num>0:
    a=random.choice(Alphabets)
    b=random.choice(Alphanumeric)
    d=str(random.randint(1,10))
    c+=a
    num-=1
    if num>0:
        if alphanum=="Y":
            c+=b
            num-=1
        if numbers=="Y":
            if num>0:
                c+=d
                num-=1
            else:
                continue
        else:
            continue
    else:
        continue
print(c)