from mmap import ACCESS_DEFAULT
from random import randint

def favorite_programming_language(list_of_languages):
    # Write a function that takes in a list of programming languages and prompts the user for their favorite language.
    # If that language is in the list, return it and print it to the console
    user_input = input("What is your favorite programming language?")
    if user_input in list_of_languages:
        print(user_input)
        return user_input
    else:
        return None

def random_number_between_max_and_min(max, min):
    # return a random number between max and min
    return randint(max - 1, min + 1)

def reverse_word(word):
    new_word = [word[-i] for i in range(1, len(word)+1)]
    return "".join(new_word)

def flamingo_banana():
    # fizzbuzz, but flamingo for 7 and banana for 4
    for i in range(100, 1, -1):
        if i % 7 == 0 and i % 4 == 0:
            print("Flamingo-Banana!")
        elif i % 4 == 0:
            print("banana")
        elif i % 7 == 0:
            print("flamingo")
        else:
            print(i)

def only_less_than_five(old_list):
    return [number for number in old_list if number < 5]

def only_less_than_five_no_duplicates(old_list):
    new_list = []
    for number in old_list:
        if number < 5 and number not in new_list:
            new_list.append(number)

def when_will_you_turn_100():
    user_name = input("What is your name?")
    user_age = int(input("How old are you?"))
    current_year = 2021
    year_user_turns_100 = current_year + (100 - user_age)

    print(f"{user_name} will be 100 in the year {year_user_turns_100}!")

def common_values_of_two_lists(list1, list2):
    common_values = []
    for value in list1:
        if value in list2 and value not in common_values:
            common_values.append(value)
    for value in list2:
        if value in list1 and value not in common_values:
            common_values.append(value)

    return common_values

def are_words_anagrams(word1, word2):
    if len(word1) != len(word2):
        return False
    extra_letters1 = [letter for letter in word1 if letter not in word2]
    extra_letters2 = [letter for letter in word2 if letter not in word1]
    if len(extra_letters1) > 0 or len(extra_letters2) > 0:
        return False

    else:
        return True

def reverse_every_word(phrase):
    split_phrase = phrase.split(" ")
    for word in split_phrase:
        word = reverse_word(word)

    return " ".join(split_phrase)

def inverted_pyramid():
    top_row_count = int(input("How many stars do you want in the first row?"))
    output = ""
    for i in range(0, top_row_count, 2):
        output = output + (" " * (i//2)) + ("*" * (top_row_count - i)) + (" " * (i//2)) + "\n"

    print(output)

def main():
    print("Starting program")

    list_of_programming_languages = ["C#", "Java", "Javascript", "Python", "Ruby", "R", "Pascal", "Perl", "C++", "C", "F#", "Swift", "Objective-C", "PHP"]
    favorite_programming_language(list_of_programming_languages)

    print(random_number_between_max_and_min(0, 100))
    print(random_number_between_max_and_min(10, 20))
    print(random_number_between_max_and_min(0, 9001))

    print(reverse_word("hello"))
    print(reverse_word("world"))
    print(reverse_word("python"))

    flamingo_banana()

    less_than_five_list = [1, 5, 8, 9, 3, 2, 56, 78, 3456, 3, 5, 8, 2, 1, 4, 0]
    only_less_than_five(less_than_five_list)

    only_less_than_five_no_duplicates(less_than_five_list)

    when_will_you_turn_100()

    common1 = [1, 2, 3, 4, 5, 6, 7, 8]
    common2 = [0, 9, 8, 7, 6, 5]
    print(common_values_of_two_lists(common1, common2))

    print(are_words_anagrams("this", "hits"))
    print(are_words_anagrams("yes", "no"))
    print(are_words_anagrams("", ""))

    print(reverse_every_word("sphinx of black quartz hear my vow"))
    print(reverse_every_word("hello world"))

    inverted_pyramid()
    inverted_pyramid()
    inverted_pyramid()

main()