# input : all you have to do is adding or removing words from the list
words = ["stair","pilot","train","might","cross","crane","flint","bread","plant","shine","Micky","shrek","simba",
         "luffy","panda","horse","chair","phone","clock","tokyo","shark","drive","paris","grape","zebra"]

# output : all codes bellow works automateclly according to input
import random
import Games.Design as Design

num = len(words)
print(f"{Design.shape1(f"Wellcome to wordle{Design.hands("hi")}")} ")
print("    I will give you a word from 5 letters and you have to guess it by writing another word\n" \
"from 5 letters only until you reach to the secret word, also I will help you to make it easy by:")
print(f"\n{Design.circle("green")} Green  : the letter is right and in the right place" \
f"\n{Design.circle("yellow")} Yellow : the letter is right but in the wrong place" \
f"\n{Design.circle("red")} Red    : the letter is wrong ")

choice = random.choice(words)
print(f"{Design.shape1(f"Word is choosen let's begin {Design.emojies("smile")}")}")
try_num = 0
while try_num <= 4:
    guess = input(f"\nguess the word from five letters only ({5-try_num} tries remaining): ").lower().strip()
    if try_num <=4 and len(guess.lower())==5 and guess.lower().isalpha():
        if choice == guess:
            print(f"\ncongratulations {Design.hands("clap")} ! you guessed the word correctely. \n")
            break

        else:
            let = 0
            print()
            while let <= 4:
                if choice[let] == guess[let]:
                    print(f"{Design.circle("green")} {guess.lower()[let]} " , end="   " )
                    let += 1
                elif guess[let] in choice:
                    print(f"{Design.circle("yellow")} {guess.lower()[let]} " , end="   " )
                    let +=1
                else:
                    print(f"{Design.circle("red")} {guess.lower()[let]} " , end="   " )
                    let +=1
            print()
            
    else:
        if len(guess) != 5:
            print(f"{Design.shape1("I said 5 letters only!")}")
            try_num -=1
        else:
            print(f"{Design.shape1("Are you stuped? I said letters only!")}")
            try_num -=1
    try_num +=1
    if try_num == 5:
        print(f"{Design.shape1(f"Unfortunatelu, you lost in cause of out of tries {Design.emojies("tear")}  ! the word was {choice}")}")