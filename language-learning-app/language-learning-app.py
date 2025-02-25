from pprint import pprint
import random


common_words = [
    { "word": "السلام", "pronunciation": "as-salāmu", "translation": "peace" },
    { "word": "حب", "pronunciation": "hubb", "translation": "love" },
    { "word": "الله", "pronunciation": "allāh", "translation": "God" },
    { "word": "الكتاب", "pronunciation": "al-kitāb", "translation": "book" },
    { "word": "قلب", "pronunciation": "qalb", "translation": "heart" },
    { "word": "مدينة", "pronunciation": "madīnah", "translation": "city" },
    { "word": "شمس", "pronunciation": "shams", "translation": "sun" },
    { "word": "ماء", "pronunciation": "mā’", "translation": "water" },
    { "word": "جمال", "pronunciation": "jamāl", "translation": "beauty" },
    { "word": "فكر", "pronunciation": "fikr", "translation": "think" },
    { "word": "العمل", "pronunciation": "al-‘amal", "translation": "work" },
    { "word": "أب", "pronunciation": "ab", "translation": "father" },
    { "word": "أم", "pronunciation": "umm", "translation": "mother" },
    { "word": "طعام", "pronunciation": "ṭa‘ām", "translation": "food" },
    { "word": "سعادة", "pronunciation": "sa‘ādah", "translation": "happiness" },
    { "word": "مدرسة", "pronunciation": "madrasa", "translation": "school" },
    { "word": "طائر", "pronunciation": "ṭā’ir", "translation": "bird" },
    { "word": "صديق", "pronunciation": "ṣadīq", "translation": "friend" },
    { "word": "بيوت", "pronunciation": "buyūt", "translation": "houses" },
    { "word": "حياة", "pronunciation": "ḥayāh", "translation": "life" },
]
# keys = list(common_words.keys())
# values = list(common_words.values())
# words = keys,values # a tuple, containing 2 values

# pprint(common_words)

def quiz_user(words):
    random.shuffle(common_words)
    score = 0
    turn = 0
    concent = ''
    for word in words:
        print(f'What is the translation of "{word['word'], word['pronunciation']}"?')
        user_answer = input(': ').strip().lower()
        correct_answer = word['translation'].lower()
        if user_answer == correct_answer:
            print('correct!!!')
            score += 1
            turn += 1
        else:
            print('Wrong Idiot?!?!?!')
            print(f'The correct answer of "{word['word'], word['pronunciation']}" is "{correct_answer}"')
            turn += 1
        if turn == 5:
            print(f'"Right now your score is {score}"')
        concent = input('Do you want to continue the game, (yes:y/no:n): ').strip().lower()
        if concent == 'y':
            pass
        else:
            print('Hope to see you again!!, Bye.')
            break

        

def main():
    print('Welcome to Language Learning App')
    input('Press Enter to start the quiz.... ')
    quiz_user(common_words)

if __name__ == '__main__':
    main()
