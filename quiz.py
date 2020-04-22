import sys
import random

path = sys.argv[1]

def file_to_dict(text):
    d = {}
    lines = [x for x in text.split("\n") if x]
    for line in lines:
        a = line.split("     ")
        d[a[0].strip()] = a[1].strip()
    return d

text = open(path,"r")

quiz = file_to_dict(text.read())

score = 0

while True:
    question = list(quiz.keys())[random.randint(0,len(quiz.keys())-1)]
    print("Question: {}".format(question))
    answer  = input()
    if quiz[question] == answer:
        print("you got it!")
        score += 1
    else:
        print("sorry, that's not it")
    print("score: {}\n".format(score))
