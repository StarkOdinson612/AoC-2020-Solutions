import math


def trump_detector(trump_speech):
    # your code here
    num_extra = 0
    num_norm = 0
    output = 0
    ind = 0
    trumpness = 0

    for letter in trump_speech:
        if ind == 0:
            print(letter)
            past_letter = letter
            if vowel_check(letter.lower()) is True:
                num_norm = 1
            ind += 1
        else:
            if vowel_check(letter.lower()):
                print('Does ' + str(past_letter.lower()) + ' = ' + str(
                    letter.lower()) + '? ===> ' + str(letter.lower() == past_letter.lower()))
                print('Is Vowel')
                if letter.lower() == past_letter.lower():
                    num_extra += 1
                    print('Repeat --> Extra: ' + str(num_extra) + ', Norm: ' + str(num_norm))
                else:
                    num_norm += 1
                    print('Not Repeat --> ' + str(num_norm))
            past_letter = letter.lower()

    print(num_norm)
    print(num_extra)
    trumpness = num_extra / num_norm

    if trumpness - int(trumpness) == 0:
        return int(trumpness)
    return round(trumpness, 2)


def vowel_check(letter):
    switcher = {
        "a": True,
        "e": True,
        "i": True,
        "o": True,
        "u": True
    }

    return switcher.get(letter, False)


print(trump_detector(input("Insert Verification:")))
