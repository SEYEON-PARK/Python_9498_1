# 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.

score=int(input()) # 사용자로부터 score 입력받기

if(score>=90): # 만약, score가 90 이상이라면
    print('A')
elif(score>=80): # 만약, score가 90 미만이고 80 이상이라면
    print('B')
elif(score>=70): # 만약, score가 80 미만이고 70 이상이라면
    print("C")
elif(score>=60): # 만약, score가 70 미만이고 60 이상이라면
    print('D')
else: # 만약, score가 60 미만이라면
    print('F')
