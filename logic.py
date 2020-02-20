from questions import quest, answerKey, scoreSheet


def score(mark):
    score = 0
    for item in mark:  # her marks let  [correct,wrong ,wrong, correct ,correct]
        if item == 'Correct':
            score += 1
        elif item == 'wrong':
            score += 0
    data = [score, mark]
    with open('scoresheet.txt', 'a') as fopen:
        fopen.write(str(data) + '\n')
    return score


def testScore(takeAnswer, key):
    if takeAnswer == answerKey[key]:  # takeAnswer of 1st question  == answer[key] (the value of answer key (o) index)
        scoreSheet.append('Correct')
    else:
        scoreSheet.append('wrong')
    return scoreSheet


def match():
    for key in quest:
        # print(quest[key])
        for q in quest[key]:
            print(quest[key][q])
        takeAnswer = input(">>>Enter Your Answer : ")
        result = testScore(takeAnswer, key)
    return score(
        result)  # here result can be [correct,wrong ,wrong, correct ,correct] and this is pass to marks  # and then
    # final value of score is temperary scored at there and finally send to main.py points
