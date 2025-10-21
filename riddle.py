import random

score = 0

riddles = {
    "What has to be broken before you can use it?": "An egg",
    "I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?": "An echo",
    "The more of me you take, the more you leave behind. What am I?": "Footsteps",
    "What can travel around the world while staying in the same corner?": "A stamp",
    "I’m tall when I’m young, and I’m short when I’m old. What am I?": "A candle"
}

question = random.choice(list(riddles.keys()))
answer = riddles[question]

def riddle(question, answer):
    global score
    running = True
    while running:
        print(question)
        guess = input('enter answer:')
        if guess == answer:
            print('riddle solved')
            score += 1
            running = False
        elif guess != answer:
            print('incorrect')
for i in range(10):
    riddle(question, answer)

    print("Score:", score)
    question = random.choice(list(riddles.keys()))
    answer = riddles[question]
