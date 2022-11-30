# 숫자 카드 더미에 카드가 총 100장 있으며, 각 카드에는 1부터 100까지 숫자가 하나씩 적혀있다.
# 2 이상 100 이하의 자연수를 하나 정해서 그 수 보다 작거나 같은 숫자 카드들을 준비하고,
# 준비한 카드의 수만큼 작은 상자를 준비하면 게임을 시작한다.
# <<게임 방법>>
# 준비된 상자에 카드를 한장씩 넣고, 상자를 무작위로 섞어 일렬로 나열한다.
# 상자가 일렬로 나열되면 상자가 나열된 순서에 따라 1번부터 순차적으로 증가하는 번호를 붙인다.
# 그 다음 임의의 상자를 하나 선택하여 상자 안의 숫자 카드를 확인한다.
# 다음으로 확인한 카드에 적힌 번호에 해당하는 상자를 열어 안에 담긴 카드에 적힌 숫자를 확인한다.
# 마찬가지로 계속 반복을 하다가, 열어야 하는 상자가 이미 열려있을 때 멈춘다.

# 이렇게 연 상자들은 1번 그룹이다. 1번 그룹은 다른 상자들과 섞이지 않도록 따로 둔다.
# 만약 1번 그룹을 제회하고 남는 상자가 없으면 게임이 종료되고, 이때 획득하는 점수는 0점이다.

# 그렇지 않으면 남은 상자 중 다시 임의의 상자 하나를 골라 같은 방식으로 진행한다.
# 이렇게 연 상자들은 2번 그룹이다. 1번 그룹에 속한 상자의 수와 2번 그룹에 속한 상자의 수를 곱한 값이 게임의 점수이다.

# 상자안에 들어있는 카드 번호가 순서대로 담긴 카드 배열 cards가 매개변수로 주어질 때,
# 이 게임에서 얻을 수 있는 최고점수를 구해서 return하는 solution함수를 만들어라.

# ===
#  - 2<= cards의 길이 <=100
#  - cards의 원소는 cards길이 이하인 임의의 자연수
#  - cards에는 중북되는 원소 존재 안함
#  - cards[i]는 i+1 상자에 담긴 카드에 적힌 숫자 의미함

#  입력 cards : 8 6 3 7 2 5 1 4
#  출력 result : 12

import random

n = int(input('값을 입력하세요 :'))

cards = []
for i in range(1, n+1):
    cards.append(i)

random.shuffle(cards)   
print(cards)

def solution(cards):
    answer = []
    for i in range(0,len(cards)):
        c = 0
        list = []
        list.append(cards[i])
        while True:
            if  cards[list[c]-1] in list :
                break
            else:
                list.append(cards[list[c]-1])
                c += 1
        for j in [x for x in cards if x not in list]:
            d = 0
            c_list = list.copy()
            c_list.append(j)
            while True:
                if  cards[c_list[c+1+d]-1] in c_list :
                    break
                else:
                    c_list.append(cards[c_list[c+1+d]-1])
                    d += 1               
                    answer.append((c+1)*(d+1))
    if len(answer) == 0:
        answer.append(0)
    return max(answer)

print(solution(cards))