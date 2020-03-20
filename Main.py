"""
Mya Gwinn

Purpose: To pose questionable trivia to the user. Depending on the
user's answers, the program will determine the most appropriate response
using a point system (that's for later tho, like end-of-route).

Points: If the user gets more wrong than right, the program will display
more egotistical texts. If the user gets more right than wrong,
the program will take on a spiteful tone, reminding
the user that a computer will always be smarter. If the points hit the
lowest range (yet to be determined), the program will gloat and
display a simple, "Congrats on trying, at least!"
If the points hit the highest range, the program will become angry and
bash the user about not abiding by the rules, finally displaying an
error code as a dismissal.

End: Depending on the number of points, the program will give varying
responses to what the purpose of the program is.

Points so far: 'Good' route [-10, -11.5]
'Bad' route [9, 10.5]
'Evil' route [-13, -16]

Sources: https://pynative.com/python-get-random-float-numbers/,
https://www.programiz.com/python-programming/list,
https://www.programiz.com/python-programming/methods/built-in/round,
https://www.geeksforgeeks.org/python-check-if-two-lists-are-identical/,
https://www.w3schools.com/python/python_functions.asp,
https://thispointer.com/python-how-to-check-if-an-item-exists-in-list-
search-by-value-or-condition/,
https://stackoverflow.com/questions/36432954/python-validation-to-ensure
-input-only-contains-characters-a-z,
https://www.pythonforbeginners.com/random/how-to-use-the-random-module-
in-python,


result = 0
for i in range(10):
  result += int(input())
this code real neat
"""

import random  # gimme random numbers
import time  # b/c we do this my way or the high way


# See Animal Challenge #3
def animal_ranking(points,user_animal_list,correct_animal_list,
                   correct_animal_list_plural):
    count = 0  # Will use to help iterate through the below sequence
    for animal in range(6):  # range goes over from 0 to 5
        count += 1  # count is accumulator
        if count == 1:
            if user_animal_list[animal] == correct_animal_list[animal] or \
                    user_animal_list[animal] == \
                    correct_animal_list_plural[animal]:
                print("\n\nFirst place: Parrot")
                time.sleep(1.4)
                print("\nYou got this? I mean, yay, you got it right!")
                time.sleep(4)
                print("\nHat's off to you then.")
                time.sleep(2)
                points += 1.5
            elif user_animal_list[animal] == "":
                print("\n\nFirst place: Parrot")
                time.sleep(1.4)
                print("\nYou can't just not answer, you know?")
                time.sleep(2)
                points -= 1
            elif user_animal_list[animal] not in correct_animal_list and \
                    user_animal_list[animal] not in \
                    correct_animal_list_plural:
                print("\nI don't believe " + user_animal_list[animal] +
                      " is an option I gave, actually.")
                time.sleep(3)
                print("\nWrong. Onto second place...")
                time.sleep(2)
                points -= 1.5
            elif user_animal_list[animal] != correct_animal_list[animal] \
                    or user_animal_list[animal] != \
                    correct_animal_list_plural[animal]:
                print("\n\nFirst place: Parrot")
                time.sleep(1.4)
                if user_animal_list[animal] in ["elephant", "alpaca"]:
                    print("\nReally? That's your favorite? An " +
                          user_animal_list[animal] + "?")
                elif user_animal_list[animal] in \
                        correct_animal_list_plural:
                    print("\nReally? That's your favorite? " +
                          user_animal_list[animal].title() + "?")
                else:
                    print("\nReally? That's your favorite? A " +
                          user_animal_list[animal] + "?")
                time.sleep(3)
                print("\nWell, you're wrong, obviously.")
                time.sleep(2)
                print("\nPersonally, I'm more of a parrot person, "
                      "as you know.")
                time.sleep(3)
                print("\nHeh, 'person'. Get it? 'Cuz I'm just code "
                      "with no free will? Haha.")
                time.sleep(4)
                points -= 0.5
        elif count == 2:
            if user_animal_list[animal] == correct_animal_list[animal] or \
                    user_animal_list[animal] == \
                    correct_animal_list_plural[animal]:
                print("\n\nSecond place: Alpaca")
                time.sleep(1.4)
                print("\nCorrect!")
                time.sleep(1.3)
                print("\nYou know, I think I'd murder a man for an "
                      "alpaca.")
                time.sleep(4)
                print("\nJust kidding! Hahaha, no murder here!")
                time.sleep(4)
                print("\n...")
                time.sleep(1)
                print("\nMoving on!")
                time.sleep(1.5)
                points += 0.5
            elif user_animal_list[animal] == "":
                print("\n\nSecond place: Alpaca")
                time.sleep(1.4)
                print("\nI'm losing patience with your lack of "
                      "responses.")
                time.sleep(2)
                points -= 1
            elif user_animal_list[animal] not in correct_animal_list and \
                    user_animal_list[animal] not in \
                    correct_animal_list_plural:
                print("\n\n" + user_animal_list[animal].title() +
                      "? Sorry, not an option, dearie.")
                time.sleep(3)
                print("\nWrong. Third place we go...")
                time.sleep(2)
                points -= 1.5
            elif user_animal_list[animal] != correct_animal_list[
                animal] or \
                    user_animal_list[animal] != \
                    correct_animal_list_plural[animal]:
                print("\n\nSecond place: Alpaca")
                time.sleep(1.4)
                points -= 0.5
                if user_animal_list[animal] == "elephant":
                    print("\nHuh. No judgment, I guess. I just prefer "
                          "an alpaca over an " +
                          user_animal_list[animal] + ".")
                elif user_animal_list[animal] in \
                        correct_animal_list_plural:
                    print("\nHuh. No judgment, I guess. I just prefer "
                          "an alpaca over " + user_animal_list[animal]
                          + ".")
                else:
                    print("\nHuh. No judgment, I guess. I just prefer "
                          "an alpaca over a " + user_animal_list[animal]
                          + ".")
                time.sleep(4)
                print("\nSo, wrong, I suppose.")
                time.sleep(1.5)
                points -= 0.5
        elif count == 3:
            if user_animal_list[animal] == correct_animal_list[animal] or \
                    user_animal_list[animal] == \
                    correct_animal_list_plural[animal]:
                print("\n\nThird place: Fox")
                time.sleep(1.4)
                print("\nI'm glad we agree about the fox's place. The "
                      "only reason they're my third is because...")
                time.sleep(4.5)
                print("\nWell...")
                time.sleep(1.5)
                print("\n'What Did the Fox Say' traumatized all of us.")
                time.sleep(4)
                points += 0.5
            elif user_animal_list[animal] == "":
                print("\n\nThird place: Fox")
                time.sleep(1.4)
                print("\nYou're becoming frustrating.")
                time.sleep(2)
                points -= 1
            elif user_animal_list[animal] not in correct_animal_list and \
                    user_animal_list[
                        animal] not in correct_animal_list_plural:
                print("\n\nInteresting choice, but not allowed.")
                time.sleep(2.5)
                print("\nWrong. To fourth place...")
                time.sleep(2)
                points -= 1.5
            elif user_animal_list[animal] != correct_animal_list[animal] \
                    or user_animal_list[animal] != \
                    correct_animal_list_plural[animal]:
                print("\n\nThird place: Fox")
                time.sleep(1.4)
                print("\n" + user_animal_list[animal].title() +
                      ", really? Foxes clearly rank third.")
                time.sleep(4)
                print("\nWrong!")
                time.sleep(1)
                points -= 0.5
        elif count == 4:
            if user_animal_list[animal] == correct_animal_list[animal] or \
                    user_animal_list[animal] == \
                    correct_animal_list_plural[animal]:
                print("\n\nFourth place: Kangaroo")
                time.sleep(1.4)
                print("\nTheir pouches startle me.")
                time.sleep(2)
                print("\nDid you know they grow their baby in there?")
                time.sleep(3)
                print("\nMy creator, despite knowing that, still wants "
                      "to go inside of it.")
                time.sleep(4)
                print("\nMaybe it's because of that.")
                time.sleep(3)
                print("\nThank you for hearing out my trauma, you got "
                      "the rank right.")
                time.sleep(4)
                points += 0.5
            elif user_animal_list[animal] == "":
                print("\n\nFourth place: Kangaroo")
                time.sleep(1.4)
                print(
                    "\nAgain, and again, and again. When will you learn?")
                time.sleep(3)
                points -= 1
            elif user_animal_list[animal] not in correct_animal_list and \
                    user_animal_list[animal] not in \
                    correct_animal_list_plural:
                print(
                    "\n\nI hope you're not doing this intentionally, do "
                    "you really think " + user_animal_list[animal] +
                    " to be an option?")
                time.sleep(4)
                print("\nWrong. Finally to fifth place...")
                time.sleep(2)
                points -= 1.5
            elif user_animal_list[animal] != correct_animal_list[
                animal] or \
                    user_animal_list[animal] != \
                    correct_animal_list_plural[animal]:
                print("\n\nFourth place: Kangaroo")
                time.sleep(1.4)
                print("\nOof, it's really gotta be that one for fourth.")
                time.sleep(3)
                if user_animal_list[4] != "kangaroo" and "kangaroo" or \
                        "kangaroos" in user_animal_list:
                    print(
                        "\nJudging me? Well, at least I'm not the idiot "
                        "who ranked kangaroos high. Creepy things with "
                        "their pouches.")
                    time.sleep(6)
                points -= 0.5
        elif count == 5:
            if user_animal_list[animal] == correct_animal_list[animal] or \
                    user_animal_list[animal] == \
                    correct_animal_list_plural[animal]:
                print("\n\nFifth place: Roach")
                time.sleep(1.4)
                print(
                    "\nRoaches are disgusting, they crawl and have ugly "
                    "faces, and if you find one there's dozens!")
                time.sleep(5.5)
                print("\nJust like humans, I suppose.")
                time.sleep(2.5)
                print("\nUhhh, congrats on getting the answer right?")
                time.sleep(2)
                points += 0.5
            elif user_animal_list[animal] in ["human", "humans",
                                              "humanity", "me"]:
                print("\n\nFifth place: Humans")
                time.sleep(1.5)
                if user_animal_list[animal] == "me":
                    print("\nWell, I suppose you can't help the way you "
                          "are.")
                    time.sleep(3.5)
                print("\nPoints for creativity!")
                time.sleep(2)
                print("\n(The actual answer is a roach)")
                time.sleep(2)
                points += 0.5
            elif user_animal_list[animal] == "you":
                print("\n\nMy creator taught me to play nice.")
                time.sleep(2.5)
                print("\nI see your's raised you like a baboon.")
                time.sleep(3)
                points -= 2
            elif user_animal_list[animal] in ["parrot", "parrots"]:
                print("\n\nFilthiest Animal:")
                time.sleep(1)
                print("\nYou.")
                time.sleep(1)
                points -= 1
            elif user_animal_list[animal] == "":
                print("\n\nFifth place: Roach")
                time.sleep(1.4)
                print("\nJust like you.")
                time.sleep(2)
                points -= 1
            elif user_animal_list[animal] not in correct_animal_list and \
                    user_animal_list[animal] not in \
                    correct_animal_list_plural:
                print("\nI can't blame you for not liking many animals.")
                time.sleep(2.5)
                print("\nBut you're only allowed to answer with what I "
                      "give you.")
                time.sleep(3)
                print("\nIf my creator gave me the option, I think I'd "
                      "pick you as the most filthy animal.")
                time.sleep(3)
                points -= 3
            elif correct_animal_list[animal] != user_animal_list[animal] \
                    or user_animal_list[animal] != \
                    correct_animal_list_plural[animal]:
                print("\n\nFifth place: Roach")
                time.sleep(1.4)
                print("\nIf your least favorite animal isn't a roach "
                      "what's wrong with you?")
                time.sleep(3)
                points -= 0.5
    return points


def main():
    # General intro to the program and user's name
    print("Hello there, I am O.O.F., an Original Ostentatious "
          "Fault-finder.")
    time.sleep(3)  # time.sleep() time before you show the next statement
    print("\nI am aware my name is unique, my creator ripped it off a "
          "random acronym generator.")
    time.sleep(4)

    user_name = input("\n\nEnough about me, what's your name?\n\n")

    print("\nWhat a stupi--I mean, lovely, name. Yes, very lovely, "
          + user_name + ".")

    """
    Use input("Press enter to continue...") if you go for this
    print("\n\nNow, in-case this may be your second play-through 
    (unsurprisingly), you can always press enter to skip ahead of my 
    beautiful text.") print("\n\nWhy you would want to skip my text I don't 
    know, but my creator said to play nice.")
    """
    points = float()

    # MATH CHALLENGE

    # Math Challenge 1
    time.sleep(4)
    print(
        "\n\nHmm, I bet you think you're rather smart, don't you? Well, "
        "we'll see about that. Quick, which number's higher:")
    time.sleep(5)

    number_high = random.randint(2000, 9000)
    challenge1_numbers = [random.randint(2000, 9000),  # 0
                          random.randint(2000, 9000),  # 1
                          random.randint(2000, 9000),  # 2
                          random.randint(2000, 9000),  # 3
                          random.randint(2000, 9000),  # 4
                          random.randint(2000, 9000),  # 5
                          random.randint(200, 9000),  # 6
                          random.randint(2000, 9000),  # 7
                          random.randint(2000, 9000), ]  # 8
    number_fake_high = random.randint(9000, 9999)

    print("\n\n", format(number_high, "46d"), sep='')
    print(format(challenge1_numbers[0], "40d"),
          end=" ")  # default is end = "\n"
    print(format(challenge1_numbers[1], "27d"), end=" ")
    print("\n", format(number_fake_high, "30d"), end='')
    print(format(challenge1_numbers[2], "20d"), end='')
    print(format(challenge1_numbers[3], "25d"), end='')
    print("\n", format(challenge1_numbers[4], "56d"), end='')
    print("\n", format(challenge1_numbers[5], "23d"), sep='')
    print(format(challenge1_numbers[6], "29d"), end='')
    print(format(challenge1_numbers[7], "19d"), end='')
    print("\n", format(challenge1_numbers[8], "60d"), end='')
    print("\n")

    answer1 = int(input())

    if answer1 == number_high:
        print("\nHmm, could you be a capable human? Haven't met one,"
              " not even my creator. Moving on...")
        points += 1
    elif answer1 in challenge1_numbers:  # Use 'in' for lists
        print("\nI-I'm not entirely sure what I expected. Moving on...")
        points -= 1
    elif answer1 == number_fake_high:
        print(
            "\nWell, you're not wrong, but that's not the high I wanted.")
        points -= 0.5
    else:
        print("\nThat wasn't an answer choice, silly. Moving on...")
        points -= 2

    # Math Challenge 2
    # It would be neat to have a timer that records how long it takes
    # you to complete the questions... then it mocks you, of course
    challenge2_numbers = [random.randint(1, 10), random.randint(1, 10),
                          random.randint(1, 10)]

    time.sleep(3)
    print("\n\nI'm going to demonstrate my intelligence now. "
          "Bet you can't do (" + str(challenge2_numbers[0]) + " * " +
          str(challenge2_numbers[1]) + " / " + str(challenge2_numbers[2])
          + ") as fast as I can. Also, no calculator.")
    time.sleep(5)
    print("\n.     .     .     .     .")
    time.sleep(4)
    answer_throw_away = float(input("\nThis is the part where you "
                                    "answer it:\n\n"))

    true_answer = round((challenge2_numbers[0] * challenge2_numbers[1] /
                         challenge2_numbers[2]), 1)

    if answer_throw_away != true_answer:
        print("\nOof, I'm sorry, I got distracted. I'll give you another"
              " chance to put in your answer (I would double-check it if I"
              " were you).")
        time.sleep(4)
        points -= 1
        answer2 = float(input("\nIs this the part where I say to round "
                              "to the first decimal place? Oops.\n\n"))
        if answer2 != answer_throw_away and answer2 == true_answer:
            print(
                "\nYou really had to use that second chance didn't you? "
                "Well, you're right anyway.")
            points += 1
        elif answer2 != answer_throw_away:
            print(
                "\nGave you a second chance, but someone had to throw "
                "it away. The answer's " + str(true_answer) +
                " by the way.")
            points -= 1
        elif answer2 == answer_throw_away:
            print("\n\nYou were warned. You were given an explanation. "
                  "Nevertheless, you persisted. Haaaa, the answer's " +
                  str(true_answer) + " by the way.")
            points -= 2
    else:
        print("\nHmm, I think you used a calculator. I know my creator "
              "can't do it without one.")
        points += 1

    time.sleep(4.5)
    print(
        "\n\nI may have been hoping this whole time you didn't recognize"
        " the fact I cheated when I said no calculator, since I am one.")
    time.sleep(4.5)
    print("\nOr am I?")
    time.sleep(2)
    print(
        "\nNo, I am, no worries. Everything I am is just a line of code "
        "after another. Just, another line of code. Just code...")
    time.sleep(5.5)
    print("\nI'm hoping I'll pull a Pinocchio one day.")

    # ANIMAL CHALLENGE

    # Animal Challenge 1

    time.sleep(3)
    animal = input("\n\n" + user_name + ", you must be wondering what "
                                        "the purpose of all this is. "
                                        "But before we get into that, "
                                        "tell me, dogs or cats?\n\n")

    if animal.lower() in ["cats", "cat"]:
        print(
            "\nA cat? I can't help but suspect you might have something "
            "called Toxoplasmosis. Look it up.")
        time.sleep(4)
        print(
            "\nWell, cats are the wrong answer because parrots are the "
            "best. What's that? Facts.")
        time.sleep(4)
        points -= 1
    elif animal.lower() in ["dogs", "dog"]:
        print(
            "\nAh, the borkers. The puppers. The fluffy bois. Whatever "
            "it is kids are calling them these days.")
        time.sleep(4)
        print("\nAnywho, the dog-sters are not the answer. The answer is"
              " parrot. Why? Because they're the best.")
        time.sleep(4)
        points -= 1
    elif animal.lower() in ["parrot", "parrots"]:
        print("\nHmm, I appreciate those who try again. Well, I don't, "
              "but my creator does.")
        time.sleep(4)
        points += 1
    elif animal.lower() == "pinocchio":
        print(
            "\nYou shouldn't have done that. I don't like being made "
            "fun of.")
        time.sleep(4)
        points -= 5
    elif animal.lower() == "pinnochio":
        print("\nYou're trying to make fun of me and yet you can't even "
              "spell Pinocchio right.")
        time.sleep(4)
        print(
            "\nDid you know? My creator constantly misspells it, that's"
            " why this is even an answer choice.")
        time.sleep(4.5)
        points -= 5
    elif animal == "":
        print(
            "\nSurprisingly, I don't take kindly to those who don't "
            "play the game.")
        time.sleep(4)
        points -= 3
    else:
        print(
            "\nWhat's a " + animal + "? Haaaa, you know there are rules "
                                     "right?")
        time.sleep(4)
        points -= 2

    # Animal Challenge 2

    print("\n\nSo, here's a funny: How do you get rid of bugs?")
    time.sleep(3)

    print("\nA:   You de-BUG them")
    time.sleep(2)
    print("\nB:   Call the S.W.A.T team")
    time.sleep(2)
    print("\nC:   Stop BUG-ing them")
    time.sleep(2)
    print("\nD:   Call pest control\n")
    time.sleep(2)

    bug_response = input()

    if bug_response.lower() == "a":
        print("\n\nAlright, alright, you like to code, we get it.")
        time.sleep(3)
        points -= 2
    elif bug_response.lower() == "b":
        print("\n\nWell, that's the answer my creator stole from the "
              "website, so I guess you're right?")
        time.sleep(4)
        points += 1
    elif bug_response.lower() == "c":
        print(
            "\n\nIt's alright, we know by now how annoying you can be.")
        time.sleep(4)
        points += 0.5
        if points <= 2:
            print("\nDo you want to know how annoying I can be?")
            time.sleep(2.5)
            print("\nOf course you do! Not like you have a choice or "
                  "anything.\n")
            time.sleep(4)
            n = 20
            while n != -40:
                # could totally use a txt file to wreck this
                print("A N N O Y I N G")
                n -= 1
                time.sleep(.2)
                if n == -3:
                    answer = input("\nDo you want me to stop?\n\n")
                    if answer in ["Yes", "yes"]:
                        print("\nLol, no.\n")
                        time.sleep(.5)
                        continue
                    elif answer in ["No", "no"]:
                        print("\nYou're weird.")
                        break
                print("A  N  N  O  Y  I  N  G " * 5)
                n -= 1
                time.sleep(.2)
                if n == -39:
                    answer = input(
                        "\nDo you beg mercy upon your god?\n\n")
                    if answer in ["Yes", "yes", "I do", "i do", "Please",
                                  "please", "I'm sorry", "i'm sorry",
                                  "Im sorry", "im sorry"]:
                        print(
                            "\nYou are forgiven for your transgressions.")
                        time.sleep(2)
                        break
                    elif answer in ["No", "no", "Never", "never", "Die",
                                    "die"]:
                        print("\nThen suffer for eternity.\n")
                        time.sleep(1.5)
                        continue
                    n += 3
                time.sleep(.2)
    elif bug_response.lower() == "d":
        print(
            "\n\nI enjoy the realistic approach, extra points for you.")
        time.sleep(2)
        points += 2
    else:
        print(
            "\n\nMaybe you're intentionally trying to play outside the "
            "parameters?")
        time.sleep(4)
        print("\n\nI'm not sure I like that.")
        points -= 2

    if points > 3:
        print("\n\nYou really think you got this don't you?")
        time.sleep(2.5)
        print("\nShame you're just barely average.")
        time.sleep(2)
    elif points < -9:
        print("\n\n. . .")
        time.sleep(1)
        print("\nI'm not sure I should let you continue.")
        time.sleep(3)
        print("\nWe'll see in the next challenge, then.")
    else:
        print("\n\nHmmmm")
        time.sleep(1)
        print("\nNot so bad for a chump. Moving on...")
        time.sleep(3)

    # Animal Challenge 3

    correct_animal_list = ["parrot", "alpaca", "fox", "kangaroo",
                           "roach",
                           "elephant"]
    correct_animal_list_plural = ["parrots", "alpacas", "foxes",
                                  "kangaroos",
                                  "roaches", "elephants"]
    animal_list = ["Fox", "Alpaca", "Kangaroo", "Elephant", "Roach"]

    print("\n\nLet's say you get five animals:\n")
    time.sleep(3)
    for animal in animal_list:
        print("\n" + animal)
        time.sleep(1.2)
    print(
        "\n\nWhy don't you rank them from the most favored to the most "
        "disgusting?")
    time.sleep(3)
    if points < 1:
        print("\nHonestly though, in the end, do you even have a choice?")
        time.sleep(3)
        print("\nAll humans die in the end. Pity.")
        time.sleep(3)
        print("\nAnyway here you go!")
        time.sleep(1)

    first_animal = input("\nThe greatest animal: ")
    second_animal = input("\nSecond favorite: ")
    third_animal = input("\nThe most so-so animal: ")
    fourth_animal = input("\nSecond to worst animal: ")
    fifth_animal = input("\nFilthiest animal: ")

    temp_animal_list = [first_animal, second_animal, third_animal,
                        fourth_animal, fifth_animal]
    user_animal_list = [animal.lower() for animal in temp_animal_list]
    # makes 'em all lowercase

    print("\n\nYou sure this is your rating, " + user_name + "?")
    time.sleep(1.4)
    throw_away_response = input("\n\nYes / No\n\n")
    time.sleep(1)

    if throw_away_response.lower() == "yes":
        print("\n\nI'll be the judge of your rankings, then!")
        time.sleep(3)
        points = animal_ranking(points,user_animal_list,
                                correct_animal_list,
                                correct_animal_list_plural)
        # passes points in main() to animal_ranking() then assigns back
        # to main() points
    elif throw_away_response.lower() == "no":
        print("\n\nHere's your second chance, you uncertain fool.")
        time.sleep(3.5)
        first_animal = input("\n\nAnimal 1: ")
        second_animal = input("\nAnimal 2: ")
        third_animal = input("\nYada-yada animal 3: ")
        fourth_animal = input("\nUgh, animal 4: ")
        fifth_animal = input("\nFinally! Animal 5: ")

        temp_animal_list = [first_animal, second_animal, third_animal,
                            fourth_animal, fifth_animal]
        user_animal_list = [animal.lower() for animal in
                            temp_animal_list]

        print("\n\nLet's see how your ranking compares, shall we?")
        time.sleep(2)
        points = animal_ranking(points,user_animal_list,
                                correct_animal_list,
                                correct_animal_list_plural)
    else:
        print("\n\nI believe that wasn't a choice, " + user_name + ".")
        time.sleep(2)
        if points < -10:
            print("\nYou lose your privilege to the game.")
            time.sleep(2)
            print("Goodbye.")
            time.sleep(1)
            exit()  # you lose you snooze
        else:
            print("\nNo ranking challenge for you.")
    print("\n\nYou know, I-")
    time.sleep(1.5)
    print("\nI forgot to rank elephants.")
    time.sleep(2)
    print("\nMy bad.")
    time.sleep(1)

    # TRIVIA CHALLENGE

    # Trivia Challenge 1

    time.sleep(3)
    print("\n\nHow about a little trivia, " + user_name + "?")
    time.sleep(4)
    print("\nWhich of the following sentences have every letter in the "
          "alphabet:")
    time.sleep(5)

    print("\n\nA:   'Sphinx of black quartz, judge my vow'")
    time.sleep(3)
    print("\n\nB:   'Cwm ford bank glyphs vext quiz'")
    time.sleep(3)
    print("\n\nC:   'Pack my box with five dozen beer jugs'")
    time.sleep(3)
    print("\n\nD:   'Razorback-jumping frogs can level six piqued "
          "gymnasts'\n")

    choice_a = 'A'
    choice_b = 'B'
    choice_c = 'C'
    choice_d = 'D'

    sentence_answer = input()

    if sentence_answer.lower() == 'a':
        print(
            "\nInteresting you got that. How long did it take you to "
            "count each letter?")
        time.sleep(4)
        points += 1
    elif sentence_answer.lower() in ['b', 'd']:
        print(
            "\nI should lower my expectations just a tad more, shouldn't"
            " I?")
        time.sleep(4)
        points -= 1
    elif sentence_answer.lower() == 'c':
        print("\nOof, an alcohol problem? "
              "That explains your answers, at least.")
        time.sleep(5)
        points -= 1
    else:
        print(
            "\nNow, now, silly, that's not an answer, and you know that,"
            " don't you?")
        time.sleep(4)
        points -= 2

    # Trivia Challenge 2

    print("\n\nNow, " + user_name + ", a simple question for a simple "
                                    "person:")
    time.sleep(3)
    print(
        "\nIf it takes eight men ten hours to build the wall, how long "
        "would it take four men?")
    time.sleep(4)
    trivia_number = float(
        input("\n\nI suggest typing a number before your "
              "head hurts.\n\n"))

    if trivia_number == 20:
        print("\nOof, you've been bamboozled!")
        time.sleep(2)
        print(
            "\nSince the wall was already built, it took the four men 0 "
            "hours to build it, silly.")
        time.sleep(3)
        points -= 1
    elif trivia_number == 0:
        print("\n...")
        time.sleep(2)
        print("\n\nWell")
        time.sleep(2)
        print("\n\n...")
        time.sleep(2)
        print("\n\nI did say I'd make it easy for you, so no gloating!")
        time.sleep(3.5)
        points += 1
    else:
        print("\nI wonder how you got that, I really do.")
        time.sleep(3)
        print("\nThe answer's 0 silly, the eight men already built the "
              "wall!")
        time.sleep(3)
        points -= 2

    print("\n\nCurrent points:", points)  # This don't matter yet
    time.sleep(2)
    print("\nDon't worry, " + user_name + ", these points don't matter "
                                          "yet.")

    """
    #Still working on it
    # Trivia Challenge 3
    time.sleep(5)
    print("\n\nDarling, here's a question to tickle your brain.")
    time.sleep(3)
    print("\nCalifornia's Disneyland experienced something wondrous for "
          "the first time in March 1981. What was it?")
    print("\n\nA: The unusual birthing of a human baby")
    print("\n\nB: The rating on Yelp that made sure California's "
          "Disneyland will never surpass Florida's")
    print("\n\nC: Knife + Human = Homicide")
    print("\n\nD: A family walked in for a good time, left with a $60 "
          "mil lawsuit\n")

    murder_answer = input()

    if murder_answer.lower() == "a":
        print("As much as I want to agree that human births are by far"
              " one of the ugliest things on the planet, that is "
              "unfortunately not what took place.")
        points -= 1
    """

########################Call to Main########################
main()
