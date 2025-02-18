import random
words = ['python','java', 'ruby', 'javascript', 'swift']

chosen_word = random.choice(words)
word_display = ['_' for _ in chosen_word] # Create a list of underscores
print(word_display)
print('Welcome to Hangman')
attempts = int(input('How many attempts you  want. 2 3 or 4? ')) # number of allowed attempts 
while attempts > 0 and '_' in word_display:
    print('\n' + ' '.join(word_display))
    guess = input('guess a letter: ').lower()
    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[index] = guess # reveling the letter
    else:
        print('That letter dosent appear in the word, STUUUUPID.')
        attempts -= 1
    