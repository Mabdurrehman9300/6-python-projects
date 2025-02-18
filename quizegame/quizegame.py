questions = [
    {
        'prompt': 'What is the capital of america?',
        'options': ['A. paris', 'B. jakarta', 'C. toronto', 'D. Washington D.C'],
        'answer': 'D'
    },
    {
        'prompt': 'Which is a mammal?',
        'options': ['A. dolphin', 'B. spider', 'C. elephant', 'D. sea horse'],
        'answer': 'C'
    },
    {
        'prompt': 'which one is a prime number?',
        'options': ['A. 10', 'B. 3', 'C. 12', 'D. 100'],
        'answer': 'B'
    },
    {
        'prompt': 'how many continents?',
        'options': ['A. 6', 'B. 7', 'C. 8', 'D. 9'],
        'answer': 'B'
    }
]

def run_quiz(questions):
    score = 0
    for questions in questions:
        print(questions['prompt'])
        for option in questions['options']:
            print(option)
        user_answer = input('enter your answer: ')
        if user_answer == questions['answer']:
            print('HORRAY!!!\n')
            score += 1
        else:
            print('STUUUUUUUPID!!!!!!!\n')
    if score >= 2:
        print(f'you could have done better, you score is:{score}')
    elif score == 4:
        print(f'you did a perfect job, you score is: {score}')
    elif score < 2:
        print(f'idiot you dont know this much, your fail score is:{score}')


        
run_quiz(questions)