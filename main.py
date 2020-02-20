from logic import match

print("-------Welcome To The Multiple Choice Quiz------")
flag = True
while flag:
    count = 1
    user_choice = input(">>>To start test type 'S' : ")
    if user_choice == 's' or user_choice == 'S':
        points = match()
        print("your score is: ", points)
        retest = input("do you want to give the test again type Y/N: ")
    if retest == 'Y' or retest == 'y':
        points = match()
        print("your score is: ", points)
    elif retest == 'N' or retest == 'n':
        print("Thanking you !!!")
        break
    else:
        print("invalid key !!!")
