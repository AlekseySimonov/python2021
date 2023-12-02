import random

randomQuestion = False
randomAnswers = True

print("Ответы вводятся в формате 1 2 3")

class Task:
    def __init__(self):
        self.question = ""
        self.answers = []
        self.realAnswer = ""

lines = open("test.txt", "r", encoding='utf-8').read().split('\n')
test = []
startQuestion = True
for text in lines:
    #print(text)
    if text == '':
        continue
    if startQuestion:
        startQuestion = False
        test.append(Task())
        test[-1].question = text
    else:
        if text.startswith("Правильный ответ:"):
            text = text[len("Правильный ответ:"):len(text)]
            test[-1].realAnswer = text
            startQuestion = True
            valid = False
            for t in test[-1].answers:
                if test[-1].realAnswer == t:
                    valid = True
                    break
            if not valid:
                print(test[-1].question)
                break
        else :
            test[-1].answers.append(text.replace("1.", "").replace("2.", "").replace("3.", "").replace("4.", "").replace("5.", "").replace("6.", ""))

if randomQuestion:
    random.shuffle(test)

correct = 0
incorrect = 0

for task in test:
    print(task.question)
    if randomAnswers:
        random.shuffle(task.answers)
    for i in range(len(task.answers)):
        print(i + 1, " ", task.answers[i])
    print("Ответ: ", end='')
    ans = int(input()) - 1

    if task.realAnswer == task.answers[ans]:
        print("Верно!")
        correct += 1
    else:
        incorrect += 1
        print("Неверно! Верно: ", task.realAnswer)

print("\n\n\nВерно: ", correct)
print("\n\n\nВерно: ", incorrect)
