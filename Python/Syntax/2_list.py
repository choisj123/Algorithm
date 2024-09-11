import random

# list
a = []
b = list()
c = [3,7,2,6,9]

print(type(a))
print(type(b))
print(type(c))

print(a)
print(b)
print(c)

print(c[0])

gifts = ['장난감', '케이크', '동화책', '운동화', '가방']

for gift in gifts:
    print(gift)

for i in range(len(gifts)):
    print(f"{i+1} 번째 선물 = {gifts[i]}")
  
print(gifts[1:4])

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(arr[1:8:2])
print(arr[::-1])

# 파이썬에서는 인덱스도 필요하고, 리스트의 요소도 필요한 경우 enumerate 라는 함수를 사용
# enumerate는 인덱스와 데이터 둘 다 필요할 때 인덱스와 데이터를 튜플 형태로 리턴


# 선물 리스트 프로그램 만들기

# 1 입력시 선물의 총 갯수를 확인한다
# 2 입력시 선물의 전체 리스트를 확인한다
# 3 입력시 보고싶은 순서의 선물을 확인한다
# 리스트의 인덱스를 입력하면 해당 선물을 보여준다
# 4 입력시 선물의 부분 리스트를 확인한다
# 리스트의 시작과 끝을 입력하면 주어진 범위의 선물을 보여준다
# 0을 입력하면 끝낸다

def print_menu():
    print("*" * 20)
    print("레오의 선물 리스트!!")
    print("무엇을 할까요?")
    print("1. 선물 갯수 보기")
    print("2. 선물 전체 보기")
    print("3. 정해진 순서의 선물 보기")
    print("4. 정해진 범위의 선물 보기")
    print("0. 끝내기")

num = 0

while num != 0:
    print_menu()
    num = int(input())

    if num == 1:
        print(len(gifts))
    elif num == 2:
        print(gifts)
    elif num == 3:
        i = int(input("몇 번째 선물을 볼까요?"))
        print(gifts[i - 1])
    elif num == 4:
        i = int(input("몇 번째 선물부터 확인할까요?"))
        j = int(input("몇 번째 선물까지 볼까요?"))
        print(gifts[i - 1 : j])
    elif num == 0:
        break;


# 리스트 추가하기
gifts.append('게임기') # 기존 리스트의 마지막에 추가됨
gifts.insert(1, "색얀필") # insert(추가할 인덱스, 추가할 항목)
print(gifts)

gifts[1] = '수정'
print(gifts)

# 리스트 값 삭제
del gifts[1] # del 리스트[인덱스]
print(gifts)

gifts.remove("동화책") # 리스트.remove(삭제할 요소)
print(gifts)

# 요소 찾기
if "색연필" in gifts:
    print("색연필이 있습니다.")
else:
    print("색연필이 없습니다.")

# 요소 꺼내고 삭제하기
arr = [1, 2, 3, 4, 5]
temp = arr.pop()
print(temp)
print(arr)
temp = arr.pop(0)
print(temp)
print(arr)

# 리스트 더하기
a1 = [1,2,3,4]
a2 = [5,6,7,8]

all = a1 + a2
a1.extend(a2)
print(all)
print(a1)


# 리스트 곱하기
arr = [0] * 100
# 0으로 초기화 되어 있는 100개의 데이터가 들어있는 리스트. 특정 값으로 초기화할 때 많이 사용

print(a1.count(3))

my_list = [i * i for i in range(1, 11)]
print(my_list) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

## 이차원 배열
num = 5
my_list = [[num * i + j for j in range(num)] for i in range(num)]
print(my_list)
# [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19], [20, 21, 22, 23, 24]]

num = 5
my_list = []
for i in range(num):
    row = []
    for j in range(num):
        row.append(num * i + j)
    my_list.append(row)
print(my_list)

# 리스트의 특징
# 리스트는 자료들의 모임입니다.
# 순서를 가지고 있어 순서를 가지고 항목에 접근할 수 있습니다.
# 어떠한 자료형도 넣을 수 있습니다.
# 자유롭게 변경이 가능하며 중복이 허용됩니다.


scores = [60, 95, 75, 85, 90]

print("1. 성적 보기") # 조회
print("2. 최고 점수 보기") # max
print("3. 최저 점수 보기") # min
print("4. 낮은 점수순으로 정렬해서 보기") # 오름차순
print("5. 높은 점수순으로 정렬해서 보기") # 내림차순
print("6. 점수 뒤집어서 보기") # 리스트 뒤집기(index 슬라이싱)

comm = int(input("무엇을 할까요?"))
if comm == 1:
    print("점수를 그대로 출력합니다.")
    print(scores)
elif comm == 2: # 최대값
    # print(max(scores))

    # 1. 최대값을 저장할 변수를 하나 만들어 배열의 첫 번째 값을 넣는다
    max_score = scores[0]
    # 2. 리스트의 값들과 하나하나 비교하면서 자신보다 큰 값을 만나면 그 값으로 변경한다
    for s in scores[1:]:
        if max_score < s:
            max_score = s
    # 3. 최종적으로 얻은 값이 최댓값
    print(max_score)

elif comm == 3: # 최소값
    # print(min(scores))
    
    min_score = scores[0]
    for s in scores[1:]:
        if min_score > s:
            min_score = s
    print(min_score)

elif comm == 4: # 오른차순
    scores.sort() ## sort는 원본 자체를 변경
    sorted_scores = sorted(scores) # 원본은 놔두고 정렬된 결과를 따로 얻고 싶을 때 사용
    print(scores)
elif comm == 5: # 내림차순
    scores.sort(reverse=True)
    sorted_scores = sorted(scores, reverse=True)
    print(scores)

elif comm == 6: # 리스트 뒤집기
    print(scores[::-1])

    scores.reverse()
    print(scores)

    reversed_scores = list(reversed(scores))
    print(reversed_scores)
    

## 리스트로 퀴즈 프로그램 만들기


i = 1
score = 0

while(i <= 5):
    a = random.randint(1, 10)
    b = random.randint(1, 10)

    result = int(input(f'{a} * {b} = ?'))
    if result == a * b:
        score += 20
        print("맞았습니다.")
    else:
        print("틀렸습니다.")
    i += 1

print(f"총 점수는 {score}점 입니다.")


# for i in range(len(a)):
#     result = int(input(f'{a[i]} * {b[i]} = ?'))
#     if result == a[i] * b[i]:
#         score += 20
#         print("맞았습니다.")
#     else:
#         print("틀렸습니다.")
# print(f"총 점수는 {score}점 입니다.")



arr = [[3,6], [7,8], [2,9], [6,4], [9,3]]

score = 0

for a, b in arr:
    result = int(input(f'{a} * {b} = ?'))
    if result == a * b:
        score += 20
        print("맞았습니다.")
    else:
        print("틀렸습니다.")
print(f"총 점수는 {score}점 입니다.")


# 튜플
tu1 = (1, 2, 3)
tu2 = 4, 5, 6
tu3 = ()
tu4 = tuple()

print(type(tu1), tu1)
print(type(tu2), tu2)
print(type(tu3), tu3)
print(type(tu4), tu4)

tup1 = (1)
tup2 = (2,)
tup3 = 3
tup4 = 4,
print(type(tup1), tup1) 
print(type(tup2), tup2)
print(type(tup3), tup3)
print(type(tup4), tup4)

# packing : 인자로 받은 여러 개의 값을 하나의 객체로 인식해서 사용할 수 있게 해줍니다.
# unpacking : packing 반대 개념으로 여러 개의 인자가 있는 하나의 객체를 여러 개로 풀어줍니다.
# 사실 packing과 unpacking은 리스트와 튜플 모두 사용할 수 있습니다. 
# 그런데도 리스트가 아닌 튜플을 언급한 이유는 튜플 생성 시 소괄호가 아닌 콤마( , ) 만으로 구분할 수 있다고 했습니다. 
# 그것을 통해 유연한 코딩이 가능합니다.


gift = '장난감', '운동화'
g1, g2 = gift # unpacking을 통해 gift를 풀어 각 변수에 대입
print(g1) # 장난감
print(g2) # 운동화
print(gift) # ('장난감', '운동화')
# 리스트나 튜플 앞에 *을 입력하면 unpacking 됩니다.
print(*gift) # '장난감', '운동화'

# 튜플인 gift를 사용해서 g1, g2에 각각 항목을 대입하였습니다. 
# 대괄호를 사용해 리스트로 만들어도 똑같이 동작합니다. 
# gift 앞에 * 을 붙여 unpacking 할 수도 있습니다.

toy, *gift = '장난감', '운동화', '게임기'
print(toy)
print(*gift)


# 두 값 바꾸기
a = 10
b = 20
print(a,b)
a, b = b, a
print(a,b)