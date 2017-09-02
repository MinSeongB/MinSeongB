br = ("=" * 100)

# 열번 찍어 안넘아가는 나무가 없으니까 ㅎ 나무를 열번 찎어서 나무를 넘겨보자 우찬차 괜찮아 울어도되 사실 만렙나무는 없거든 A

treeHit = 0
while treeHit < 10:
    treeHit = treeHit + 1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무가 넘어가유 ")
# 위의 예에서 while문의 조건문은 treeHit < 10 이다. 즉, treeHit가 10보다 작은 동안에 while문 안의 문장들을 계속 수행한다.
# whlie문 안의 문장을 보면 제일 먼저 treeHit = treeHit + 1로 treeHit 값이 계속 1씩 증가한다.
# 그리고 나무를 treeHit번만큼 찍었음을 알리는 문장을 출력하고 treeHit가 10이 되면 "나무 넘어갑니다."라는 문장을 출력한다.
# 그러고 나면 treeHit < 10 이라는 조건문이 거짓이 되므로 while문을 빠져나가게 된다.
#
# (※ treeHit = treeHit + 1 은 프로그래밍을 할 때 매우 자주 사용하는 기법이다. treeHit의 값을 1만큼씩 증가시킬 목적으로 사용되며, treeHit +=1 처럼 사용되기도 한다.)

print(br)



# while문은 조건문이 참인 동안 계속해서 while문 안의 내용을 반복적으로 수행한다.
# 하지만 강제로 while문을 빠져나가고 싶을 때가 있다. 예를 들어 커피 자판기를 생각해 보자. 자판기 안에 커피가 충분히 있을 때에는 동전을 넣으면 커피가 나온다.
# 그런데 자판기가 제대로 작동하려면 커피가 얼마나 남았는지 항상 검사해야 한다. 만약 커피가 떨어졌다면 판매를 중단하고 "판매 중지"라는 문구를 사용자에게 보여주어야 한다.
# 이렇게 판매를 강제로 멈추게 하는 것이 바로 break문이다.
#
# 다음의 예는 커피 자판기 이야기를 파이썬 프로그램으로 표현해 본 것이다.

coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줌 ㅇㅅㅇ")
    coffee = coffee -1
    print("남은 커피 양은 %d개입니다." % coffee)

    if not coffee:
        print("커피 다 떨어짐 ㅇㅅㅇ ")
        break
print(br)


# break문 이용해 자판기 작동 과정 만들기
#
# 하지만 실제 자판기는 위의 예처럼 작동하지는 않을 것이다. 다음은 자판기의 실제 작동 과정과 비슷하게 만들어 본 예이다.
# 이해가 안 되더라도 걱정하지 말자. 아래의 예는 조금 복잡하니까 대화형 인터프리터를 이용하지 말고 에디터를 이용해서 작성해 보자.

coffee = 10
while True:
    money = int(input("돈을 넣어 주세요: "))
    if money == 300:
        print("커피를 줍니다.")
        coffee = coffee -1
        print("남은 커피의 양은 %d개 입니다." % coffee)
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다." % (money -300))
        coffee = coffee -1
        print("남은 커피의 양은 %d개 입니다." % coffee)
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
    if not coffee:
        print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
        break


